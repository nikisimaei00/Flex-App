
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Review(models.Model):
    listing_name = models.CharField(max_length=255)
    guest_name = models.CharField(max_length=255)
    overall_rating = models.IntegerField()
    cleanliness_rating = models.IntegerField()
    communication_rating = models.IntegerField()
    respect_house_rules_rating = models.IntegerField()
    public_review = models.TextField()
    submitted_at = models.DateTimeField()
    approved = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='reviews')
    channel = models.CharField(max_length=50, default="Hostaway")

    def __str__(self):
        return f"Review for {self.listing_name} by {self.guest_name}"
