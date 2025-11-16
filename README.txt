Flex Living – Reviews Dashboard
================================

This project is an implementation of the Flex Living Reviews Dashboard
assessment. It includes:

• Mocked Hostaway reviews integration  
• A full manager dashboard  
• Per-property performance analytics  
• Review approval workflow  
• Public property review display  
• Google Reviews exploration (mock endpoint)

The system provides a modern, clean UI inspired by Flex Living’s brand.


--------------------------------------------------
1. FEATURES
--------------------------------------------------

1) Hostaway Integration (Mocked)
   • The provided Hostaway API sandbox contains no real review data.
   • The project uses the supplied mock JSON file (hostaway_mock.json).
   • Reviews are normalized and exposed through:
       /reviews/api/hostaway/

2) Manager Dashboard
   URL: /reviews/dashboard/

   Dashboard features:
   • Sort by date or rating
   • Filter by category, minimum rating, or date range
   • Automatic detection of recurring issues
   • Ability to approve / hide reviews
   • Per-property analytics table
   • Clean UI with responsive layout

3) Property Review Display
   URL example:
       /reviews/property/?name=PROPERTY_NAME

   • Shows only approved reviews
   • Matches simplified Flex Living property layout

4) Google Reviews (Exploration)
   • A mock endpoint is provided at /reviews/api/google-demo/
   • Real Google API requires billing; not usable for this assessment.

--------------------------------------------------
2. PROJECT STRUCTURE
--------------------------------------------------

flex_living/
│   manage.py
│   requirements.txt
│
├── flex_living/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── reviews/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── hostaway_mock.json
│   ├── templates/reviews/dashboard.html
│   ├── templates/reviews/property_page.html
│   └── templates/home.html
│
└── staticfiles/ (created automatically if needed)


-----------------------------------------------------
DEPLOYMENT & TEST LINKS
-----------------------------------------------------

Live Application (Render):
- Home Page:        https://flex-app-5.onrender.com/
- Dashboard:        https://flex-app-5.onrender.com/reviews/dashboard/
API Endpoints:
- Hostaway Reviews API (Normalized JSON):
  https://flex-app-5.onrender.com/reviews/api/hostaway/
- Google Reviews Demo (Mock):
  https://flex-app-5.onrender.com/reviews/api/google-demo/
- Import Hostaway Data:
  https://flex-app-5.onrender.com/reviews/import-hostaway/

Admin Panel:
- Django Admin: https://flex-app-5.onrender.com/admin/
  Username: admin
  Password: adminadmin

GitHub Repository (Source Code):
https://github.com/nikisimaei00/Flex-App

-----------------------------------------------------
Notes:
- All routes are live on Render.
- Reviewer can click links to test UI, API, and dashboard functionality.
- No additional setup required to view the running version.

--------------------------------------------------
3. LOCAL SETUP
--------------------------------------------------

1) Clone repository:
   git clone <your-github-repo-url>
   cd flex_living

2) Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3) Install dependencies:
   pip install -r requirements.txt

4) Run migrations:
   python manage.py migrate

5) Import mocked Hostaway reviews (optional):
   python manage.py import_hostaway
   OR open in browser:
   http://127.0.0.1:8000/reviews/import-hostaway/

6) Start server:
   python manage.py runserver

7) Open pages in browser:
   Home:              http://127.0.0.1:8000/
   Dashboard:         http://127.0.0.1:8000/reviews/dashboard/
   Property page:     http://127.0.0.1:8000/reviews/property/?name=NAME
   Hostaway API:      http://127.0.0.1:8000/reviews/api/hostaway/
   Google demo API:   http://127.0.0.1:8000/reviews/api/google-demo/
   Admin:             http://127.0.0.1:8000/admin/



