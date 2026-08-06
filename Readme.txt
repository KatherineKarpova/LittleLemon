Little Lemon Web Application
==============================

Project directory:
workspace/littlelemon

Run the application:
python manage.py migrate
python manage.py runserver

Static homepage
---------------
GET /

User registration and authentication
------------------------------------
POST /auth/users/
POST /auth/token/login/
POST /auth/token/logout/

Menu API
--------
GET  /api/menu-items/
POST /api/menu-items/

GET    /api/menu-items/<id>/
PUT    /api/menu-items/<id>/
PATCH  /api/menu-items/<id>/
DELETE /api/menu-items/<id>/

Table booking API
-----------------
GET  /restaurant/booking/tables/
POST /restaurant/booking/tables/

GET    /restaurant/booking/tables/<id>/
PUT    /restaurant/booking/tables/<id>/
PATCH  /restaurant/booking/tables/<id>/
DELETE /restaurant/booking/tables/<id>/

Protected test endpoint
-----------------------
GET /api/message/

Authentication
--------------
For protected endpoints, add the following header in Insomnia:

Authorization: Token <authentication-token>

Use the ID returned by a POST or GET response when testing detail,
update, and delete endpoints.