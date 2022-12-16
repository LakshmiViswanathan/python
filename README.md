# python
# trial commit 10629129

INTRODUCTION

An online flat booking system is a platform that allows users to search for and book apartments or flats for rent. This system can be used by individuals looking for a place to live, as well as property managers and landlords who want to make their rentals available to a wider audience.
 
With an online flat booking system, users can browse listings and filter their search based on criteria such as location, price, and number of bedrooms. They can view detailed information about each property, including photos, amenities, and availability. Once they have found a property that meets their needs, they can easily book it online and securely pay for their rental.Therefore, an online flat booking system provides a convenient and efficient way for people to find and book rental properties, saving time and effort for both renters and landlords.In addition to the features described above, an online flat booking system can be built using a combination of technologies, such as python for the backend, bootstrap for the frontend, and a MySQL database to store information about the properties and user accounts.

This project includes website design and implementation. acquisition of new tenants for condominiums and related properties Facility Management.
The project itself serves as an example to see how websites are built and maintained the database and, consequently, how to connect the frontend to the backend. To do so, Frontend refers to her website visited by her web users during the backend. It refers to databases created with Object Relational Model and is a graphical user interface.(GUI) Access the SQLite database provided by the Django server.The language which connects the sqlite database to the website is Python.
Django Inbuilt Authentication is implemented in the system. The seller can Create, Read, Update and Delete the Flat Record with using google map API. Seller post the postal code and with the help of pgeocode library of python it’ll automatically converted to the latitude and longitude.
The front-end design languages used in this project are mainly HTML, CSS, Bootstrap and some JavaScript coding.
 
Overall, using these technologies together can provide a robust and efficient platform for an online flat booking system, allowing users to easily search for and book rental properties.


Project Overview

Home Page:-

A landing page is the page that everyone navigates to on the Home tab of the navigation bar. You will be redirected as described in the introduction. This "home" page is primarily 10 divisions or so-called sections.

	 A navigation bar at the top end of the page
	About Section
	Services Section
	Rent a Flat Section
	Contact Section

About:-

About page for brief explaintion of the website, Header and Footer remains the same as the home page for all other pages.

Service:-

A dynamic service page for showing the services which are added from the admin panel and shows on a detail service page.

All Flats:-

A Dynamic page for showing all flats available on the website added from the admin panel and view the flat on flat detail page. In flat detail page there are map integration which shows the location of the flat and below this there are a booking form where tenants can book the flat and information saves into the database which reflects to the admin, seller and user panel.

Contact:-

In the Contact Page we have a Contact form by this any seller or user if have any issue regarding to the website then they can contact to the admin by sending the contact message.

Signup:-

In the signup page we have signup form which help to register the user on the website after signup page will redirects to the home page.

Login:-

There are two login pages one for the tenants which is above and another for seller login which is  the below at footer seller panel.

Seller Panel:-

In this seller can post an advertisement for the rent of flat, view the advertisement, edit the advertisement and delete the advertisement.

Seller got the details of booked flats from users on the dashboard also he can delete the booked flat by user.

User Panel:- 

User can check their booked flats on the user dashboard, update the booking information on user panel
and also delete the booking

Admin Panel:-

Here’s the django’s inbuilt admin panel in which admin can do create, read, update and delete operations on all the tables under the project. 


Architecture:

The flow starts with the user. The user over the internet surfs the website. The request is received on Apache server which directly interacts with the user. Then request goes to Django Application inside first request goes to urls then it’ll match a url pattern according to the enterd user url then request goes to the views function and called the matched function in views after that request integrate the corresponding models which perform CRUD operation with database then function return templates with static files and last presents to the user.

Technology and Libraries used:

1.	Backend Technologies
•	Python
•	Django
•	Pgeocode
•	Pillow


2.	Database Technologies
•	MySQLite


3.	Frontend Technologies
•	HTML,
•	CSS
•	Javascript
•	Bootstrap


4.	Version Control and Testing Technologies
•	Git
•	Postman


