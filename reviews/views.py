from datetime import datetime
from pathlib import Path
import json
from django.conf import settings
from django.db.models import Avg, Count
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .models import Review


# HOME PAGE

def home(request):
    return render(request, "home.html")


# ADMIN DASHBOARD VIEW

def dashboard(request):
    reviews = Review.objects.all()

    if request.method == "POST":
        review_id = request.POST.get("review_id")
        action = request.POST.get("action")

        if review_id and action:
            try:
                review = Review.objects.get(id=review_id)
                if action == "approve":
                    review.approved = True
                elif action == "reject":
                    review.approved = False
                review.save()
            except Review.DoesNotExist:
                pass

        return redirect("dashboard")

    # Filters (GET) 
    sort_by = request.GET.get("sort_by", "date")         
    category = request.GET.get("category", "overall")    
    min_rating = request.GET.get("min_rating", "")
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")
    channel = request.GET.get("channel", "")            

    # Filter by channel
    if channel:
        reviews = reviews.filter(channel=channel)

    # Filter by min rating depending on category
    if min_rating:
        try:
            val = int(min_rating)
            if category == "cleanliness":
                reviews = reviews.filter(cleanliness_rating__gte=val)
            elif category == "communication":
                reviews = reviews.filter(communication_rating__gte=val)
            elif category == "rules":
                reviews = reviews.filter(respect_house_rules_rating__gte=val)
            else:  # overall
                reviews = reviews.filter(overall_rating__gte=val)
        except ValueError:
            pass

    # Filter by date range
    if start_date:
        reviews = reviews.filter(submitted_at__date__gte=start_date)
    if end_date:
        reviews = reviews.filter(submitted_at__date__lte=end_date)

    # Sorting
    if sort_by == "rating":
        reviews = reviews.order_by("-overall_rating")
    else:
        reviews = reviews.order_by("-submitted_at")

    # Per-property performance (based on filtered reviews)
    property_stats_qs = (
        reviews.values("listing_name")
        .annotate(
            avg_rating=Avg("overall_rating"),
            avg_cleanliness=Avg("cleanliness_rating"),
            avg_communication=Avg("communication_rating"),
            avg_rules=Avg("respect_house_rules_rating"),
            review_count=Count("id"),
        )
        .order_by("-avg_rating")
    )

    property_stats = []
    for p in property_stats_qs:
        issues = []
        if p["avg_cleanliness"] is not None and p["avg_cleanliness"] < 8:
            issues.append("cleanliness")
        if p["avg_communication"] is not None and p["avg_communication"] < 8:
            issues.append("communication")
        if p["avg_rules"] is not None and p["avg_rules"] < 8:
            issues.append("house rules")
        p["issues"] = issues
        property_stats.append(p)

    # Distinct channels for dropdown
    channels = Review.objects.values_list("channel", flat=True).distinct()

    context = {
        "reviews": reviews,
        "sort_by": sort_by,
        "category": category,
        "min_rating": min_rating,
        "start_date": start_date,
        "end_date": end_date,
        "channel": channel,
        "channels": channels,
        "property_stats": property_stats,
    }

    return render(request, "reviews/dashboard.html", context)


# HOSTAWAY MOCKED API ENDPOINT

def hostaway_reviews_api(request):
    """
    Mocked Hostaway Reviews API
    Reads hostaway_mock.json and returns normalized data.
    """
    json_path = Path(settings.BASE_DIR) / "reviews" / "hostaway_mock.json"

    with open(json_path) as f:
        raw = json.load(f)

    normalized = []
    for item in raw["result"]:
        normalized.append({
            "id": item["id"],
            "listing_name": item["listingName"],
            "guest_name": item["guestName"],
            "type": item["type"],              
            "channel": "Hostaway",             
            "status": item["status"],
            "submitted_at": item["submittedAt"],
            "public_review": item["publicReview"],
            "categories": item["reviewCategory"],
        })

    return JsonResponse({"reviews": normalized})



# IMPORT HOSTAWAY JSON 

def import_hostaway_to_db(request):
    """
    Import mocked Hostaway JSON into the Review table.
    This version always creates new Review rows.
    Run it once, or delete old reviews before re-running.
    """
    json_path = Path(settings.BASE_DIR) / "reviews" / "hostaway_mock.json"

    with open(json_path) as f:
        raw = json.load(f)

    created_count = 0

    for item in raw["result"]:
        
        categories = {c["category"]: c["rating"] for c in item.get("reviewCategory", [])}

        cleanliness = categories.get("cleanliness", 0)
        communication = categories.get("communication", 0)
        respect = categories.get("respect_house_rules", 0)

        if item.get("rating") is not None:
            overall = item["rating"]
        else:
            scores = [cleanliness, communication, respect]
            scores = [s for s in scores if s is not None]
            overall = round(sum(scores) / len(scores)) if scores else 0

        submitted_at = datetime.strptime(item["submittedAt"], "%Y-%m-%d %H:%M:%S")

        Review.objects.update_or_create(
        listing_name=item["listingName"],
        guest_name=item["guestName"],
        submitted_at=submitted_at,   
        defaults={
            "overall_rating": overall,
            "cleanliness_rating": cleanliness,
            "communication_rating": communication,
            "respect_house_rules_rating": respect,
            "public_review": item["publicReview"],
            "approved": False,
            "channel": "Hostaway",
        }
    )


        created_count += 1

    return HttpResponse(f"Imported {created_count} reviews from Hostaway JSON.")




# goole_reviews

def google_reviews_demo(request):
    """
    Demo endpoint that simulates Google Reviews data.
    This does NOT call the real Google API – it just shows
    how Google reviews would be normalized and returned.
    """
    example = {
        "listing_name": "Penthouse Suite - Kensington",
        "google_rating": 4.8,
        "google_reviews_count": 2,
        "reviews": [
            {
                "guest_name": "Google User A",
                "rating": 5,
                "text": "Fantastic stay, loved the location and amenities.",
                "time": "2 weeks ago",
                "channel": "Google",
            },
            {
                "guest_name": "Google User B",
                "rating": 4,
                "text": "Very nice apartment, a bit noisy on Friday night.",
                "time": "1 month ago",
                "channel": "Google",
            },
        ],
    }
    return JsonResponse(example)
