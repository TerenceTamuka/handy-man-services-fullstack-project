<h1 align="center">Apple-gate Property Services LTD - Handyman Services</h1>

[View the live project here](https://handyman-services-fullstackapp-ba60a0c4d688.herokuapp.com/)

Apple-gate Property Services LTD is your trusted solution for all household maintenance and handyman needs. We specialize in providing a wide range of services, including:

__Painting:__ Transform your space with professional-grade painting, price starting from £100. 
__Assembling Various Units/Drawers:__ Get your furniture assembled effortlessly, with price starting from £40.
__Assistance in packing__ when moving in and out the house, price from £50.
Our user-friendly website ensures seamless booking of these services. The My Bookings feature allows customers to easily book, view, update, or cancel their appointments, ensuring a hassle-free experience. Customers can provide key information such as their name, email, phone number, preferred service, and additional booking details.

With efficient functionality and a responsive design, the website operates smoothly, ensuring that no two bookings clash. From registration to booking confirmations, Applegate Property Services LTD offers a streamlined, easy-to-use platform for all your home service needs.



![Mockup](static/images/all-devices-view.png)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories :

* __US01__: As a **registered user**, I can **view all my past and upcoming bookings,** so that **I can keep track of my service requests.**
  - *Acceptance criteria 1:* Bookings are displayed in a list or table format.
  - *Acceptance criteria 2:* The list shows the service name, date, time, and additional information.

* __US02__: As a **registered user,** I can **create a new booking,** so that **I can schedule a service based on my preferences.**
  - *Acceptance criteria 1:* A booking form allows users to select a service, provide details, and choose an available date and time.
 

* __US03__: As a **registered user,** I can **update an existing booking,** so that **I can change the service details or reschedule it.**
  - *Acceptance criteria 1:* An “Edit” button next to each booking opens the booking form pre-filled with existing data.
  - *Acceptance criteria 2:* Validation ensures the new date and time do not conflict with existing bookings.

* __US04__: As a **registered user,** I can **delete a booking,** so that **I can remove a scheduled service that I no longer need.**
  - *Acceptance criteria 1:* A “Delete” button is available for each booking, with a confirmation prompt.
  - *Acceptance criteria 2:* The booking is permanently removed from the database after deletion.

* __US05__: As a **registered user,** I can **filter my bookings,** so that **I can easily find upcoming or past bookings.**
  - *Acceptance criteria 1:* The bookings list includes a filter or search bar for upcoming or past services.
  - *Acceptance criteria 2:* The filter works based on service type, date, or status.

* __US06__: As a **registered user,** I can **register for an account,** so that **I can manage my bookings on the platform.**
  - *Acceptance criteria 1:* A registration form asks for the user’s name, email, and phone number.
  - *Acceptance criteria 2:* Users must verify their email before accessing booking features.

* __US07__: As a **registered user,** I can **log in to my account,** so that **I can access my bookings and make changes.**
  - *Acceptance criteria 1:* Users are prompted for their username and password to log in.
  - *Acceptance criteria 2:* Users who are logged in are redirected to the homepage with personalized options like "My Bookings."

* __US08__: As **an authenticated user,** I can **log out,** so that **I can securely end my session on the platform.**
  - *Acceptance criteria 1:* The navigation bar shows a “Logout” button when the user is logged in.
  - *Acceptance criteria 2:* After logout, the user is redirected to the homepage, and booking features are no longer accessible.

* __US09__: As a **website visitor,** I can **view details of services before booking,** so that **I can understand the services and their pricing.**
  - *Acceptance criteria 1:* The homepage displays a grid of services with a brief description and price.
  - *Acceptance criteria 2:* Clicking on a service leads to a detailed page with more information and the option to book.

* __US10__: As a **registered user,** I can **see notifications for booking conflicts,** so that **I can select another available date or time.**
  - *Acceptance criteria 1:* The booking system checks for existing appointments at the selected time.
  - *Acceptance criteria 2:* If there is a conflict, the user is informed and prompted to select another available slot.

## Features

Applegate Property Services LTD is a full-fledged web application built using the Django framework, designed to offer a seamless user experience for customers looking to book handyman services. This project offers services such as painting,assembling furniture, and packing and moving, with an efficient booking system that prevents scheduling conflicts. Users can create, read, update, and delete their bookings and manage their accounts.

### Existing Features

 - __F01 Navigation Bar:__

The navigation bar provides a consistent design and placement across all pages, ensuring easy and intuitive access to key sections of the site. It features a company logo alongside a link to the homepage for quick navigation. When a user is not logged in, options to register or sign in are prominently displayed. Once a user is signed in, the navigation adjusts to show links for My Bookings and Sign Out, alongside a personalized touch with the user's name and a user icon.

Designed with responsiveness in mind, the navigation bar adapts seamlessly to various screen sizes. On smaller devices, it transforms into a compact 'hamburger' menu, allowing for smooth access to all the necessary links without cluttering the interface.

![Navbar view for an unregistered user](static/images/navbar-unregistereduser-view.png)
![Navbar view for a registered user](static/images/navbar-registereduser-desktop-view.png)
![Navbar responsive view on smaller devices](static/images/navbar-responsive-view.png)

<hr>

-__F02 Landing page, name & text__

At the top of the landing page (home page) there is an area that includes an AI generated handyman photograph simulating the activities of given services and a text overlay which together clearly identify the purpose of the site as a place to find and book household services from a company called Apple-gate Property Services LTD.

![Landing page with hero image and text](static/images/landingpage-name-text.png)
<hr>

- __Booking Button__

When an authenticated user is logged in, a __Book a Service__ button will be displayed at the bottom of each service column that displays a feature service image, service description and service price information.

![Booking button for authenticated user feature](static/images/book-button.png)

<hr>

__F03 User Authentication (Register, Login, Logout)__

User authentication methods were implemented to ensure that if a user wants to book a service, they would either have to login if they are already registered or register first then make a booking request. The registration form also has an option for if user wants to view their password if they click on the __eye icon__.

Login and logout pages were created to facilitate full and secure authentication. Each time a user logs in or out, a session message feedback displays below the navbar. If a user trys to login with either an incorrect password or username, an on-screen feedback will be given for them to enter correct username or password. 

A required feature was also implemented to ensure a user has provided both their username and password fields.

- *__Register or Sign in to book a service:__* 
![Registration form](static/images/registration-form.png)

![Prompt for if user wants to book a service](static/images/sign-in-prompt-to-book.png)

- *__Login/Logout__* 
![login form](static/images/login-form.png)
![logout form](static/images/secure-logout-form.png)

-*__On-screen alerts__*
![User login authentication - on screen message for incorrect details](static/images/on-screen-message-user-details-incorrect.png)
![Required information message](static/images/required-user-details-message.png)

- *__Session Management:__*
![feedback messsage for when user signs in](static/images/user-sign-in-feedback.png)

![feedback for when user logs out](static/images/logout-feedback-message.png)

<hr>

__F04 Booking System__

The booking form page has a corresponding service feature image and the description together with the associated price information.
When a user wants to create a booking, they will have to provide their Name, Email, Contact Number, Service type, Date and time, Approved tickbox and any additional required customer information regarding the service they want assistance with.

If a user books the same date and time that has already been booked into the system, a feedback message will be displayed to the user for them to choose a different time or date.

A *Confirm Booking* submit button is displayed at the bottom of the booking form to trigger a service booking action.

Summernote was also implemented to allow authenticated users to use rich text when inputting their additional information regarding the booking.


- *__Booking Conflict:__*
![Booking conflict message](static/images/bookingConflict-message.png)

- *__Customised Date and time picker__*
![Customised date and time picker graphic](static/images/date-time-picker-graphic.png)

-*__Summernote Rich Text Input panel__*
![Summernote Rich Text input panel graphic](static/images/summernote-richtext-input.png)

<hr>


__F05 My Bookings Page__ 

My bookings page contains two main sub headings of __Your Upcoming Service Bookings__ and __Past Bookings__. These two panes will ammend dependant on the frequency of authenticated user bookings. Each upcoming service ticket will be displayed in the respective row from the aforementioned sub headings. Each service ticket that has already been attended to and carried out will be appended under the Past bookings row. 

Each scheduled ticket will display key information such as __Service Title__, __Service Info__, __Service Price__, __Customer Additional Info__, and __Date and Time__ fields. A blue phone icon will be displayed together with customer contact number and a green confirm tickbox icon will appear next to a __Confirmed__ text to alert the user that the service has been confirmed. Once a user confirms their booking, effectively an orange __Awaiting Confirmation__ will be attached to the ticket until the super user who has access to the __approved__ check button has checked to confirm booking.

The __Create, Read, Update and Delete__ functionality was implemented to ensure that if a user wants to cancel a ticket, a red __Cancel Booking__ nav button is shown at the top of the ticket. An __Edit Button__ was implemented incase a user wants to change the ticket information and once they confirm, the ticket information updates accordingly. Both the *Cancel Booking* and *Delete* buttons once they are clicked, a confirmation dialog is shown at the top modal window.


- *__Booking Management:__* 
![My Bookings Page Overview](static/images/my-bookings-page.png)

![Customer ticket info and Confirmed booking feature](static/images/customer-ticket-confirmed.png)

![Customer ticket info and Awaiting Confirmation booking feature](static/images/customer-ticket-awaiting-confirmation.png)



- *__CRUD (Create, Read, Update, Delete) Functionality:__*
![Cancel booking nav button](static/images/cancel-booking.png)

![Edit or Delete ticket Button](static/images/edit-or-delete-buttons.png)

__Super User - Booking Form with Approved Field View__
![Super User Booking Form](static/images/superUser-BookAservice-view.png)

__Super User - Edit Booking Form with Approved Field View__
![Super User Edit Booking Form](static/images/superUser-EditBooking-view.png)

__Non Super User - Booking Form View__
![Non Super User Booking Form](static/images/nonSuperUser-BookAservice-view.png)

__Non Super User - Edit Booking Form View__
![Non Super User Edit Booking Form](static/images/nonSuperUser-EditBooking-view.png)

__Booking On Screen Confirmation Message__
![Booking confirmation on screen message](static/images/booking-confirmation-message.png)

__Booking Deletion Confirmation Message__
![Deletion confirmation on screen message](static/images/confirm-delete-message.png)

<hr>

__F06 PostgreSQL Database & Super User Creation__

The admin interface provides a graphical user interface (GUI) for managing the data related to Service and Booking models. Administrators can easily create, read, update, and delete services and bookings without needing to interact directly with the database.
Admins can add new services (like Painting, Assembling, Packing) with relevant details (price, description, featured image) and manage existing services.
Similarly, they can manage bookings, approve pending bookings, and modify or cancel them as needed.

Non-technical users (such as business managers or customer service representatives) can use the Django admin interface to manage services and bookings without needing to understand the underlying code.
The admin panel’s auto-generated forms make it simple to add, edit, or delete entries, significantly reducing the learning curve.

- *__Database Intergration:__* 
![Django full site Administration Page](static/images/django-site-administration.png)

*__User Booking a service using Django admin page__*
![Django admin page for customer booking a service](static/images/django-admin-booking-form.png)

*__User feedback to confirm that a booking was successful__*
![Django admin successful booking confirmation feedback](static/images/django-admin-booking-success-feedback.png)

*__Django Admin Page for manipulating bookings__*
![Django admin Service bookings manipulation page](static/images/django-admin-manipulate-bookings.png)

__F07 Responsive Design with Bootstrap__

Responsive design ensured that the website functions and looks good on all devices, from desktops to smartphones. By using Bootstrap, which provides a grid system and pre-built classes for styling, the website automatically adjusts based on the screen size. In the project base code, the below headings highlight a more indepth summary of responsive design with Bootstrap and why content focuses on trust also.

*__Navbar__*: The navbar-toggler is implemented to collapse the menu on smaller screens, enhancing usability for mobile users.
Container-fluid: This class helps make sure the content adapts to different screen widths.
Bootstrap classes (col-md-8, offset-md-2) are used for layout, ensuring that elements are correctly spaced on different screen sizes.

 - Form styling is critical for user experience and accessibility. In the code:

 - Bootstrap form controls (form-control, form-group): These ensure that the forms are styled consistently and responsively, with inputs adapting to different devices.

 - CSRF Token: Security is integrated using Django’s CSRF protection to keep the forms secure.

 - Button Styling: Buttons like "Sign in" use Bootstrap's btn classes, making them clear and recognizable as actionable elements.

 - Eye-Catching Theme
An eye-catching theme engages users and sets the tone for the handyman property services brand.

 - Google Fonts: Fonts like Josefin Sans, Kanit, and Raleway are loaded, creating a modern and professional appearance.

 - Font Awesome icons (e.g., user icons, social media icons) are used to create visual interest, aiding both aesthetics and usability.

 - Branding: The custom logo and favicon help maintain brand identity.

 - Content Focused on Trust
Building trust through content is vital for user engagement and retention. The website builds trust by:

 - Clear Navigation: The navbar directs users to essential pages like "Sign in," "Register," and "My Bookings," ensuring transparency and ease of access.

 - Personalized Experience: Displaying the logged-in user's name in the navbar ({{ user.username }}) reassures users they are securely signed in.

 - Social Proof: Linking to social media pages like GitHub, LinkedIn, and Twitter shows users that the company is connected to trusted networks.

 - Secure Practices: Use of security best practices, such as user authentication and form validation, adds credibility.

 <br>

__Bootstrap Integration:__
![Bootstrap responsive design on smaller screens](static/images/bootstrap-responsive-design.png)

__Social Proof with Hover Effect__
![Social Media Nav Links with hover effect](static/images/social-nav-links.png)


__Eye-Catching Theme:__
![Hover effect with theme color effect](static/images/styling-theme.png)

<hr>


-__How Existing Features Support User Stories__

The User Stories in the [User Experience (UX)](#user-experience-ux) part of this document are numbered 1 to 10. The existing features are listed above as F01 to F07. Below is a traceability matrix cross-referencing the user stories with the features, illustrating which features support which stories :

![User Story Feature Matrix](static/images/traceability-matrix-features-userstories.png)






### Features which could be implemented in the future

There are quite a number of features which could come in handy for future development and some of them are:

__1. Enhanced Booking Management System__

  - __Booking Reminders and Notifications:__ Add email or SMS notifications to remind users of upcoming service appointments or booking changes.

  - __Service Availability Calendar:__ Implement a calendar view where users can see available dates and times for different services before they book, ensuring greater convenience in selecting their preferred times.

  - __Recurring Bookings:__ Allow users to create recurring bookings for periodic services (e.g., weekly cleaning), making it easier to schedule regular appointments.

__2. Service Reviews and Ratings__

  - __User Ratings & Reviews:__ After completing a service, users can leave a rating and review for the service provider. This can help new users in choosing services based on feedback and improve the overall trust and credibility of the platform.

  - __Review Management:__ Allow administrators to monitor, manage, or respond to reviews for service providers, ensuring that the feedback system is constructive and fair.

__3. Loyalty and Referral Programs__

  - __Loyalty Points System:__ Implement a rewards system where users earn points for booking services, leaving reviews, or referring new customers. Points can be redeemed for discounts on future services.

  - __Referral Program:__ Add a referral feature that allows users to invite others to the platform and earn discounts or rewards when their referrals book a service.

__4. Service Provider Profiles and Portfolio__

  - __Service Provider Pages:__ Create dedicated pages for service providers, where users can view details about the provider, including their experience, reviews, and portfolio of past work.

  - __Portfolio Display:__ Allow service providers to showcase their previous projects or services with images and descriptions, giving users more information when deciding which provider to choose.

__5. Advanced Filtering and Sorting for Bookings__

  - __Advanced Search and Filter Options:__ Users can filter services by price range, rating, availability, or type of service. This will help users quickly find the most relevant service.

  - __Sort Booking History:__ Allow users to sort their past bookings by date, type of service, or status (confirmed, canceled, awaiting confirmation).

__6. Multiple Payment Integration__

  - __Payment Gateway Integration:__ Support multiple payment methods (credit card, PayPal, Apple Pay, etc.) to provide flexibility to users during the booking process.

  - __Payment History:__ Create a section in user accounts where users can view and download receipts or payment history for completed services.

__7. Discount Codes and Promotions__

  - __Promo Codes:__ Introduce the ability for administrators to create promotional codes that users can apply during booking to receive discounts.

  - __Seasonal Promotions:__ Run time-limited promotions (e.g., holiday sales) that offer discounted services for a certain period.

__8. User Account Enhancements__

  - __Profile Management:__ Allow users to update their account information such as profile picture, phone number, or preferred payment methods.

  - __Multiple Addresses:__ Give users the ability to store multiple service addresses (e.g., home, office) for faster and more convenient booking.

__9. Customer Support Integration__

  - __Live Chat Support:__ Implement a real-time chat feature so that users can ask questions or get assistance directly from the platform without needing to call or email.

  - __Help Desk and FAQs:__ Add a comprehensive help center with FAQs and articles to assist users with common questions or booking issues.

__10. Mobile App Development__

  - __Mobile Application:__ Develop a mobile app version of the platform for both iOS and Android to make booking services and managing bookings easier for users on the go.

  - __Push Notifications:__ Send push notifications for reminders, booking confirmations, and special promotions to users who have the mobile app installed.

<hr>


## Design

### Wireframes

<details>
<summary>Desktop Wireframes</summary>

  -__Desktop-View - Home Page Unregistered user view__

![Desktop view of an unregistered user](static/images/desktop-view-homepage-unregistered-user-view.png)

<hr>

  -__Desktop-View - Home Page Registered user view__
![Desktop view of a registered user](static/images/desktop-view-homepage-registered-user-view.png)

<hr>

__Desktop-View - My Bookings Page__
![Desktop view of My Bookings page](static/images/desktop-view-mybookings-page.png)

<hr>

__Desktop-View - Edit Booking Page__
![Desktop view of Edit Booking page](static/images/desktop-view-editbooking-page.png)

<hr>

__Desktop-View - Register Page__
![Desktop view of Registration form page](static/images/desktop-view-registrationform-page.png)

<hr>

__Desktop-View - Login Page__
![Desktop view of Login page](static/images/desktop-view-loginpage.png)

<hr>

__Desktop-View - Logout Page__
![Desktop view of Logout page](static/images/desktop-view-logoutpage.png)

<hr>

__Desktop-View - Book a service Page__
![Desktop view of Book a service Page](static/images/desktop-view-bookaservice-page.png)

  
</details>

<details>
<summary>iPad View Wireframes</summary>

__Homepage view for registered, unregistered user & Edit Booking pages__
![ipad view for registered, unregistered user and edit booking pages](static/images/ipad-view-homepages-editbooking-page.png)

__My bookings, Registration Form & Booking form Pages__
![ipad view for my bookings, registration form and booking form page](static/images/ipad-view-mybookings-registrationform-bookingform-page.png)

__Sign Out, Non Super User Booking Form & Super User Booking Form View__
![ipad view for sign out, non super user booking form and super user booking form view](static/images/ipad-view-signOut-NonSuperUserBookAService-SuperUserBookAservice-view.png)

__Sign In Page View__
![Ipad view Sign in page](static/images/iPad-view-SignIn-page.png)

</details>
<hr>

-   ### Entity-Relationship diagrams and summarisation for DBMS
    
      __Entity-Relationships Schematic__
      ![Graphic of the Entity-Relationships Diagram](static/images/ER-Diagram.png)

      <hr>

      __ER Diagram Breakdown__

      __Entities:__

      -__User:__ Represents the customer who makes the booking. This is a foreign key referencing Django's built-in User model.

      -__Service:__ Represents different services like "Painting", "Assembling", and "Packing & Moving". Each service has attributes such as:
      *__name__* (the type of service),
      *__price__* (cost of the service),
      *__description__* (details about the service), and the
      *__featured_image__* (an optional image associated with the service).

      -__Booking:__ Represents a customer's booking of a service. Key attributes include:
      *__customer_name,__*
      *__customer_email,__*
      *__customer_phone_number,__*
      *__date_time__* (when the booking is scheduled),
      *__additional_info__* (optional additional booking details or specific requirements), and
      *__approved__* (whether the booking is confirmed or not).

      -__Relationships:__

      __User to Booking:__ This is a one-to-many relationship. A user can have multiple bookings, but a booking is associated with one user.

      __Service to Booking:__ This is a one-to-many relationship. A service can be booked multiple times, but a booking is associated with one service.

      -__Unique Constraint:__

      The Booking model has a unique constraint combining __date_time and service,__ meaning a particular service cannot be booked multiple times at the same date and time (to prevent double-booking).

      -__Summary Methodology:__

      __Service:__ Manages a list of services offered, each with a name, price, and optional image. The service choices are predefined in the system.

      __Booking:__ Handles customer bookings for the services. The customer details, booking time, and additional info are stored in the booking. The approved field is used to track whether a booking is confirmed or pending approval.

      __User:__ Utilizes Django’s built-in User model for customer authentication and identification, linked via a foreign key in the Booking model.


## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project.  User Stories with acceptance criteria were defined using GitHub Issues and development of code for these stories was managed using a Kanban board.  All of the User Stories were linked to a 'parent' Epic issue to show how they all supported the over-arching goal of the project.  The acceptance criteria were tested as each story moved to 'Done' and were also included in the final pre-submission manual testing documented in the Testing section of this README.

The Epic, User Stories and Kanban board can be accessed here : [Handyman Services Agile Tool](https://github.com/users/TerenceTamuka/projects/5)


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

-   [Google Fonts:](https://fonts.google.com/) used for the Josefin Sans font
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
-   [dbdiagram.io](https://dbdiagram.io/home) was used to create the Entity Relationship diagrams for the application data model
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application
-   [Bootstrap](https://getbootstrap.com/) was used to build responsive web pages
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku
-   [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow database urls to connect to the postgres db
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db
-   [Cloudinary](https://cloudinary.com/) used to store the images used by the application
-   [Summernote](https://pypi.org/project/django-summernote/) used to have rich text for users when creating or editing their booking for a service in the ADDITIONAL TEXT filed.
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering
-   [jquery library](https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js) used to fade out alert messages
-   [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) used for python mvt testing
-   [Jest](https://jestjs.io/) - used to test jquery in script.js
-   [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) used to check how much of the python code has been covered by 
automated tests

## Testing

### Validator Testing 

- 

### Automated Testing

  - 

### Browser Compatibility

- Chrome DevTools was used to test the responsiveness of the application on different screen sizes.  In addition, testing has been carried out on the following browsers :
    - Google Chrome version 9.0.4606.81 (64-bit)
    - Firefox version 93.0 (64-bit)
    - Microsoft Edge 94.0.992.38 (64-bit)
 
    
### Manual Testing Test Cases and Results

- 
### Known bugs

- Currently no known bugs.

## Deployment



### How to Clone the Repository 


### Create Application and Postgres DB on Heroku
- 
### Configure Cloudinary to host images used by the application
- 
### Connect the Heroku app to the GitHub repository


### Executing automated tests
- 

### Final Deployment steps
Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :
- Set DEBUG flag to False in settings.py
- Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
- Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable :  DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch

#### The live link to the application can be found here - []() 


## Credits 

- Used this README https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/main/README.md as a base skeleton for my README.

- [Chat GPT](https://chatgpt.com/) - AI tool used to generate the images used in the project website.

### Code 
- 

### Content 

### Media 
- The Josefin Sans font used was imported from [Google Fonts](https://fonts.google.com/)

  
  
### Acknowledgments

- 