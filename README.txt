Flex Living – Reviews Dashboard
================================

This project implements the Flex Living Reviews Dashboard assessment.
It includes a mocked Hostaway integration, a full manager dashboard,
a property review display page, and a demo Google Reviews API endpoint.


-----------------------------------------------------
1. FEATURES
-----------------------------------------------------

1) Hostaway Integration (Mocked)
   - Reads hostaway_mock.json
   - Normalizes reviews (listing, guest, ratings, date)
   - API endpoint:
       /reviews/api/hostaway/

2) Manager Dashboard
   URL:
       /reviews/dashboard/

   Features:
   - Per-property performance analytics
   - Filters: category, date range, minimum rating
   - Sorting: newest or highest rating
   - Highlights recurring issues (cleanliness, communication, rules)
   - Approve / Reject review flow
   - Modern UI inspired by Flex Living brand

3) Property Page Review Display
   URL:
       /reviews/property/?name=PROPERTY_NAME

   Shows only approved reviews.

4) Google Reviews Exploration (Mock)
   URL:
       /reviews/api/google-demo/

   Google Places API cannot be used without billing.
   Therefore a realistic mock response is provided.


-----------------------------------------------------
2. PROJECT STRUCTURE
-----------------------------------------------------
flex_living/
│   manage.py
│   requirements.txt
│
├── flex_living/              (Django project)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── reviews/                  (Main dashboard app)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── hostaway_mock.json
│   ├── templates/reviews/dashboard.html
│   ├── templates/reviews/property_page.html
│   └── templates/home.html
│
└── static/                   (assets if needed)


-----------------------------------------------------
3. LOCAL SETUP
-----------------------------------------------------

1) Clone repo
   git clone <your-repo-url>
   cd flex_living

2) Create virtual environment
   python3 -m venv venv
   source venv/bin/activate

3) Install dependencies
   pip install -r requirements.txt

4) Run migrations
   python manage.py migrate

5) Import mocked Hostaway reviews (optional)
   python manage.py import_hostaway
   OR open browser at /reviews/import-hostaway/

6) Start server
   python manage.py runserver


-----------------------------------------------------
4. RUNNING VERSION (DEPLOYMENT)
-----------------------------------------------------

Add this once deployed on Railway:
https://yourproject.up.railway.app


-----------------------------------------------------
5. API ENDPOINTS
-----------------------------------------------------

/reviews/api/hostaway/         → Normalized Hostaway data
/reviews/api/google-demo/      → Mocked Google Reviews
/reviews/dashboard/            → Manager dashboard
/reviews/property/             → Approved reviews per listing


-----------------------------------------------------
6. LICENSE
-----------------------------------------------------

This was created for an assessment. Not licensed for production.
