<h1 align="center">Apple-gate Property Services LTD - Handyman Services</h1>

[View the live project here]()

Apple-gate Property Services LTD is your trusted solution for all household maintenance and handyman needs. We specialize in providing a wide range of services, including:

Painting: Transform your space with professional-grade painting, priced between £100 - £200.
Tiling: Enhance your floors or walls with expert tiling services at £250.
Assembling Various Units/Drawers: Get your furniture assembled effortlessly, with prices ranging from £50 - £100.
Carpentry: High-quality carpentry services, with prices ranging between £100 - £400, ensuring precision and reliability.
Our user-friendly website ensures seamless booking of these services. The My Bookings feature allows customers to easily book, view, update, or cancel their appointments, ensuring a hassle-free experience. Customers can provide key information such as their name, email, phone number, preferred service, and additional booking details.

With efficient functionality and a responsive design, the website operates smoothly, ensuring that no two bookings clash. From registration to booking confirmations, Applegate Property Services LTD offers a streamlined, easy-to-use platform for all your home service needs.



![Mockup](documentation/supp-images/amiresponsive.png)

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
  - *Acceptance criteria 2:* Bookings are only allowed for open days and times (Mon-Sat, 9 AM - 9 PM).

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

Applegate Property Services LTD is a full-fledged web application built using the Django framework, designed to offer a seamless user experience for customers looking to book handyman services. This project offers services such as painting, tiling, assembling furniture, and carpentry, with an efficient booking system that prevents scheduling conflicts. Users can create, read, update, and delete their bookings and manage their accounts.

### Existing Features

__F01 Homepage with Hero Section and Services Grid__

 - *__Hero Section:__* The homepage features a large, visually appealing hero image accompanied by a catchy caption that conveys the essence of Applegate Property Services.

- *__Services Grid:__* Below the hero section, users can see all available services (painting, tiling, assembling drawers, and carpentry) in a grid format. Each service displays a brief description and price range.

- *__Navigation Bar:__* Includes links to other important pages like "Home," "Services," "My Bookings," "Register," and "Login/Logout," enabling easy navigation.

__F02 Service Detail Pages__

- *__Dynamic Service Pages:__* Each service has its own dedicated page with a more detailed description of the service and its pricing.

- *__Booking Button__* From this page, users can choose to book the service after logging in. This ensures that only authenticated users can make bookings.

__F03 User Authentication (Register, Login, Logout)__

- *__Register:__* Users can create an account by providing their name, email, and phone number. This registration process is simple and secure.

- *__Login/Logout__* After registration, users can log in to their accounts to access their personal dashboard. The navbar dynamically updates to show "Logout" when a user is authenticated.
    
- *__Session Management:__* Django's authentication system manages user sessions, ensuring that only logged-in users can access certain features, like booking and managing appointments.

__F04 Booking System__

- *__Booking Form:__* Users can book services by filling out a form that captures their name, email, phone number, service type (via radio buttons), preferred booking date and time, and any additional details.

- *__Service Selection with Prices:__* Radio buttons allow users to select the desired service, with the associated price clearly shown.

- *__Date and Time Validation:__* The booking system checks for time conflicts, ensuring that no two bookings can occur at the same time, maintaining efficient scheduling.
   
- *__Business Hours:__* Booking is only allowed from Monday to Saturday, 9 AM - 9 PM, with validation in place to prevent bookings outside of business hours.


- *__CRUD (Create, Read, Update, Delete) Functionality:__* Users can create new bookings, read existing bookings, update the details, or cancel a booking.

__F05 My Bookings Page__ 

- *__Booking Management:__* Users can visit the "My Bookings" page to view all their bookings, both upcoming and past, with details such as the service type, date, time, and additional comments.
Update and Delete: Users can update or cancel bookings directly from this page. For instance, they may reschedule a booking or remove it entirely if their plans change.

__F06 Quotations Page (Services Overview)__

- *__Service Carousel:__* The "Quotations" page displays a carousel of available services. Each service slide in the carousel includes a brief description, price, and an image representing the service.

- *__Coherent Service Prices:__* Customers can see exactly how much each service costs, allowing for easy price comparisons.

__F07 Responsive Design with Bootstrap__

- *__Bootstrap Integration:__* The project uses Bootstrap to ensure that the website is fully responsive and mobile-friendly, providing a smooth experience across devices.

- *__Form Styling:__* Bootstrap's grid system and form elements are utilized to create professional and responsive forms for booking, registration, and login.

__F08 About Us Page__

- *__Eye-Catching Theme:__* The About Us page is designed to be visually appealing, with coherent branding, images, and a short description that explains the company’s mission.

- *__Content Focused on Trust:__* The content on this page emphasizes the reliability, expertise, and customer-focused approach of Applegate Property Services.

__F09 PostgreSQL Database__

- *__Database Intergration:__* All data related to services, user accounts, and bookings is stored in a PostgreSQL database, ensuring data integrity and scalability.




### Features which could be implemented in the future

  __Automated Confirmation Emails__
    
- *__Booking Confirmation Emails:__* Once a booking is completed, the system sends an automated email to the customer, including their booking details and a friendly message confirming the service. This ensures professional communication between the business and its clients.

- __Django Email Backend:__* The email system is configured using Django’s email backend, ensuring reliability and ease of setu


## Design

-   ### Wireframes

    The wireframe diagrams below describe the Home, Hike Detail, My Bookings, Sign in, Sign out and Register pages.  Wireframes are not provided for the Django Admin pages used by the application to create data records, publish hike data, approve comments and bookings.

    <details>
    <summary>Desktop Wireframes</summary>

    ![Desktop Wireframes](documentation/wireframes/desktop.png)
    </details>
    <details>
    <summary>Tablet Wireframes</summary>

    ![Tablet Wireframes](documentation/wireframes/ipad.png)
    </details>
    <details>
    <summary>Smartphone Wireframes</summary>

    ![Smartphone Wireframes](documentation/wireframes/smartphone.png)
    </details>

-   ### Entity-Relationship diagrams for DBMS
    
      Notes on the ER diagrams :

      - The ER diagrams provided show the logical data model.  The many-to-many relationship between hikes and their 'likes' is represented as normalized tables to clarify the relationship.  In the models.py file the 'likes' data item is declared as part of the Hike class, with django handling how this relationship is represented in the physical database tables in the background.

      - The Users table in the ER diagrams is also a logical representation of the data captured during user registration and how it relates to the application data model.  The Users table itself is not declared in the models.py file, but is handled by the django modules and this logical view does not reflect all columns and constraints etc. used by the physical data tables in the database.

      - The data model tables are split into two diagrams so that the relationships between the tables can be easily read.

      - A booking is a many-to-many relationship between Schedule and Users but because it also has its own data - places_reserved, it is declared in its own separate class in models.py

      - Because there could be multiple guided hikes on the same hike trail in a single day, the schedule table needs a composite primary key of the hike_id and 'starts' column.  This is handled using a constraint in models.py.

    <details>
    <summary>ER Diagrams - Hike-Comment-Likes</summary>

    ![ER Diagrams1](documentation/entity-relationship-diagrams/hike-comment-likes.png)
    </details>
    <details>
    <summary>ER Diagrams - Hike-Schedule-Booking</summary>

    ![ER Diagrams2](documentation/entity-relationship-diagrams/hike-schedule-booking.png)
    </details>

## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project.  User Stories with acceptance criteria were defined using GitHub Issues and development of code for these stories was managed using a Kanban board.  All of the User Stories were linked to a 'parent' Epic issue to show how they all supported the over-arching goal of the project.  The acceptance criteria were tested as each story moved to 'Done' and were also included in the final pre-submission manual testing documented in the Testing section of this README.

The Epic, User Stories and Kanban board can be accessed here : [Wayfarers Agile Tool](https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/projects/1)


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

-   [Google Fonts:](https://fonts.google.com/) used for the Lato font
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
-   [Summernote](https://pypi.org/project/django-summernote/) used to provide WYSIWYG editing on the Hike editing screen
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering
-   [jquery library](https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js) used to fade out alert messages
-   [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) used for python mvt testing
-   [Jest](https://jestjs.io/) - used to test jquery in script.js
-   [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) used to check how much of the python code has been covered by 
automated tests

## Testing

### Validator Testing 

- [HTML Validator](https://validator.w3.org/)

    - As this project uses Django templates the html has been validated by manually clicking through the application pages, copying the source of the rendered pages and then validating this version of the html using the W3C Validator (link shown above).  HTML  for the Django admin site pages was not edited so has not been validated here.  The Signup, Login and Logout pages from Django allauth were customized and so have been validated, with results below.

    - results for index.html
      - <details>
        <summary>Index Page - Summary</summary>

        ![Index Page - Summary](documentation/testing/validation/html-validation-img-rendered-index-page.png)
      </details>

      - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/7c58bd1b37673c319886014673d484dabf7299f2/documentation/testing/validation/html-validation-rendered-index-page.pdf" target="_blank">Index Page - Full HTML Validation Results</a>

    - results for hike_detail.html
      - <details>
        <summary>Hike Detail Page - Summary</summary>

        ![Hike Detail Page - Summary](documentation/testing/validation/html-validation-img-rendered-detail-page.png)
      </details>

      - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/7c58bd1b37673c319886014673d484dabf7299f2/documentation/testing/validation/html-validation-rendered-detail-page.pdf" target="_blank">Hike Detail Page - Full HTML Validation Results</a>

    - results for hike_mybookings.html
      - <details>
        <summary>My Bookings Page - Summary</summary>

        ![My Bookings Page - Summary](documentation/testing/validation/html-validation-img-rendered-bookings-page.png)
      </details>

      - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/7c58bd1b37673c319886014673d484dabf7299f2/documentation/testing/validation/html-validation-rendered-bookings-page.pdf" target="_blank">My Bookings Page - Full HTML Validation Results</a>

    - results for signup.html
      - <details>
        <summary>Signup/Register Page - Summary</summary>

        ![Signup/Register Page - Summary](documentation/testing/validation/html-validation-img-rendered-register-page.png)
      </details>

      - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/7c58bd1b37673c319886014673d484dabf7299f2/documentation/testing/validation/html-validation-rendered-signup-page.pdf" target="_blank">Signup/Register Page - Full HTML Validation Results</a>

    - results for login.html
      - <details>
        <summary>Login/Sign in Page - Summary</summary>

        ![Login/Sign in Page - Summary](documentation/testing/validation/html-validation-img-rendered-login-page.png)
      </details>
      
      - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/7c58bd1b37673c319886014673d484dabf7299f2/documentation/testing/validation/html-validation-rendered-login-page.pdf" target="_blank">Login/Sign in Page - Full HTML Validation Results</a>

    - results for logout.html
      - <details>
        <summary>Logout/Sign out Page - Summary</summary>

        ![Logout/Sign out Page - Summary](documentation/testing/validation/html-validation-img-rendered-logout-page.png)
      </details>
      
      - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/7c58bd1b37673c319886014673d484dabf7299f2/documentation/testing/validation/html-validation-rendered-logout-page.pdf" target="_blank">Logout/Sign out Page - Full HTML Validation Results</a>  
  

- [CSS Validator](https://jigsaw.w3.org/css-validator/)

    - <details>
      <summary>style.css validation results</summary>

      ![style.css](documentation/testing/validation/css-validation-img1.png)
      </details>

    - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/7c58bd1b37673c319886014673d484dabf7299f2/documentation/testing/validation/css-validation-full-report.pdf" target="_blank">CSS Validation - Full Results</a> 


- [Javascript Validator](https://jshint.com/)

  <details>
    <summary>script.js validation results</summary>

    ![Script JS](documentation/testing/validation/jquery-code-validation.png)
  </details>
  <details>
    <summary>script.test.js validation results</summary>

    ![Script Test JS](documentation/testing/validation/jquery-test-validation.png)
  </details>

- [Python Validator](http://pep8online.com/)

  <details>
    <summary>project urls.py validation results</summary>

    ![Project urls.py](documentation/testing/validation/pep8-validation-project-urls.png)
  </details>
  <details>
    <summary>project settings.py validation results</summary>

    ![Project settings.py](documentation/testing/validation/pep8-validation-project-settings.png)
  </details>
  <details>
    <summary>application urls.py validation results</summary>

    ![Application urls.py](documentation/testing/validation/pep8-validation-app-urls.png)
  </details>
  <details>
    <summary>admin.py validation results</summary>

    ![admin.py](documentation/testing/validation/pep8-validation-admin.png)
  </details>
  <details>
    <summary>forms.py validation results</summary>

    ![forms.py](documentation/testing/validation/pep8-validation-forms.png)
  </details>
  <details>
    <summary>models.py validation results</summary>

    ![models.py](documentation/testing/validation/pep8-validation-models.png)
  </details>
  <details>
    <summary>views.py validation results</summary>

    ![views.py](documentation/testing/validation/pep8-validation-views.png)
  </details>
  <details>
    <summary>test_admin.py validation results</summary>

    ![test_admin.py](documentation/testing/validation/pep8-validation-test_admin.png)
  </details>
  <details>
    <summary>test_forms.py validation results</summary>

    ![test_forms.py](documentation/testing/validation/pep8-validation-test_forms.png)
  </details>
  <details>
    <summary>test_models.py validation results</summary>

    ![test_models.py](documentation/testing/validation/pep8-validation-test_models.png)
  </details>
  <details>
    <summary>test_views.py validation results</summary>

    ![test_views.py](documentation/testing/validation/pep8-validation-test_views.png)
  </details>
  

### Automated Testing

  - [Jest](https://jestjs.io/) was used to test the application javascript and jquery code.  The functionality tested was the code to fade out, slide up and remove any raised alert messages after a 5 second delay.  The code is located in [Script JS](static/js/script.js), the test is located in [Test JS](static/js/tests/script.test.js)

  - Jest test results :     
    ![JS Test Results](documentation/testing/results/jquery-test-results.png)

   - [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) were used to test the application python code.  
   - DB tests were run in the development environment against a local SQLite3 database. 
   - Tests were written for the following files :

      - [forms.py](hikebooker/forms.py)  test file: [test_forms.py](hikebooker/test_forms.py)
      - [models.py](hikebooker/models.py)  ters file: [test_models.py](hikebooker/test_models.py)
      - [views.py](hikebooker/views.py)  test file: [test_views.py](hikebooker/test_views.py)
      - [admin.py](hikebooker/admin.py)  test file: [test_admin.py](hikebooker/test_admin.py)  (tests were added for the customizations made to the django admin functionality)

  - Django test results and coverage :   
    ![Python Test Results](documentation/testing/results/python-coverage-test-results.png)


### Browser Compatibility

- Chrome DevTools was used to test the responsiveness of the application on different screen sizes.  In addition, testing has been carried out on the following browsers :
    - Google Chrome version 9.0.4606.81 (64-bit)
    - Firefox version 93.0 (64-bit)
    - Microsoft Edge 94.0.992.38 (64-bit)
 
    
### Manual Testing Test Cases and Results

- The link below details the test cases that were used, the results, and a cross-reference to the Feature ID that each test case exercised (click link to open pdf).  The test cases are primarily based on the User Story acceptance criteria that were used to test iterations of the code during development.
  
  - <a href="https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes/blob/517f5abbe2b0bd575b9da340f0560d13466340a4/documentation/testing/results/test-cases.pdf" target="_blank">Manual Testing - Test Cases and Results</a>

### Known bugs

- Currently no known bugs.

## Deployment

Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application.  Code Institute also provides a summary of similar process steps here : [CI Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

1. How to Clone the Repository
2. Create Application and Postgres DB on Heroku
3. Configure Cloudinary to host images used by the application
4. Connect the Heroku app to the GitHub repository
5. Executing automated tests
6. Final Deployment steps

### How to Clone the Repository 

- Go to the https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
- To install the packages required by the application use the command : pip install -r requirements.txt
- When developing and running the application locally set DEBUG=True in the settings.py file
- Changes made to the local clone can be pushed back to the repository using the following commands :

  - git add *filenames*  (or "." to add all changed files)
  - git commit -m *"text message describing changes"*
  - git push

- N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku

### Create Application and Postgres DB on Heroku
- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
- Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up. 
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

  - SECRET_KEY = os.environ.get('SECRET_KEY')

- In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate 
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

### Configure Cloudinary to host images used by the application
- Log in to Cloudinary - create an account if needed.  To create the account provide your name, email and set up a password.  For "primary interest" you can choose "Programmable Media for image and video API".  Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
- From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
- Log in to Heroku and go to the Application Configuration page for the application.  Click on Settings and click on the "Reveal Config Vars" button.
- Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string. 
- In order to be able to run the application on localhost, also add the CLOUDINARY_URL environment variable and value to env.py

### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/elainebroche-dev/pf4-wayfarers-guided-hikes) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://pf4-wayfarers.herokuapp.com/)

### Executing automated tests
- The existing automated jquery/javascript test can be executed using jest as follows :
  - If jest is not installed then run the command : npm install --save-dev jest
  - Run the js test file using the command : npm test

- The existing automated django/python tests are executed using unittest as follows :
  - Run the python tests using the command : python3 manage.py test
  - To run just a subset of the tests, then append the application and test file name to the command, e.g. : python3 manage.py test hikebooker.test_models

- Test coverage for the django/python tests can be reviewed using the coverage tool :
  - If coverage is not installed then run the command : pip3 install coverage
  - Execute the following series of commands to determine test coverage :
    - coverage run --source=hikebooker manage.py test
    - coverage report
    - coverage html
    - python3 -m http.server  (detailed results can be viewed via the browser in the htmlcov directory)


### Final Deployment steps
Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :
- Set DEBUG flag to False in settings.py
- Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
- Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
- Push files to GitHub
- In the Heroku Config Vars for the application delete this environment variable :  DISABLE_COLLECTSTATIC
- On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch

#### The live link to the application can be found here - [P4 Wayfarers Hikes](https://pf4-wayfarers.herokuapp.com/) 


## Credits 

### Code 
- Much of the coding and testing relies heavily on information in the "Hello Django" and "I Think Therefore I Blog" walkthroughs in the Code Institue Full Stack Frameworks module. 
- Code on how to implement data model constraints was based on information found here : [Constraints](https://docs.djangoproject.com/en/3.2/ref/models/constraints/)
- Information on errors when a foreign key field was included in search field list was found here : [Search Forgein Key](https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains)
- Code to restrict data value range : [Min Max Values](https://stackoverflow.com/questions/65416042/max-and-min-values-for-a-django-model-field-according-to-the-values-already-int)
- Information on how to round decimal field to 2 places : [Round Decimals](https://stackoverflow.com/questions/37958130/automatically-round-djangos-decimalfield-according-to-the-max-digits-and-decima)
- Information on how to implement jumbotron images : [Jumbotron](https://stackoverflow.com/questions/22000754/responsive-bootstrap-jumbotron-background-image)
- Code on how to remove trailing zeroes from decimal fields : [Normalize function](https://stackoverflow.com/questions/40135464/django-remove-trailing-zeroes-for-a-decimal-in-a-template)
- Setting to turn off auth email verification : [EMAIL VERIFICATION](https://stackoverflow.com/questions/53968044/django-user-registration-error-with-django-rest-auth-package)
- Some ideas on how to format the authentication/Sign in/Registration pages came from : [Page layout demo](https://www.bootstrapdash.com/product/free-bootstrap-login/#product-demo-section)
- Code to 'bold' active navbar link : [Active Link](https://stackoverflow.com/questions/32931436/active-tag-on-bootstrap-with-django)
- Code to remove class from base.html : [Override class](https://stackoverflow.com/questions/34232936/dry-method-to-add-a-class-to-body-in-the-base-template)
- Code to help with order_by for composite foreign key : [Composite order](https://stackoverflow.com/questions/1474135/django-admin-ordering-of-foreignkey-and-manytomanyfield-relations-referencing-u)
- Code to help filter upcoming bookings : [Date handling](https://stackoverflow.com/questions/21576727/django-records-greater-than-particular-date)
- Code to build dropdown for schedule : [Drop-down control](https://stackoverflow.com/questions/57533058/django-how-to-add-items-to-bootstrap-dropdown)
- Code on how to build dropdown : [Additional Drop-down information](https://getbootstrap.com/docs/5.0/components/dropdowns/)
- Code on how to convert number string to list : [Python lists](https://stackoverflow.com/questions/4395230/building-a-list-in-django-templates)
- Code on how to display messages to user : [Alert messages](https://stackoverflow.com/questions/28240746/django-how-to-implement-alertpopup-message-after-complete-method-in-view)
- Additional code on alert message handling : [Fade and Slide](https://stackoverflow.com/questions/23101966/bootstrap-alert-auto-close)
- Code to test automatically generated dates : [Date Mocking](https://stackoverflow.com/questions/49874923/how-to-test-auto-now-add-in-django)
- Code on how to use setUpTestData : [Test Data generation](https://stackoverflow.com/questions/29428894/django-setuptestdata-vs-setup)
- Code on how to create a user reference and log them in : [Test User login](https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests)
- Code to help with naive date : [Timezone aware dates](https://stackoverflow.com/questions/4530069/how-do-i-get-a-value-of-datetime-today-in-python-that-is-timezone-aware)
- Code to help with testing admin.py customizations : [Custom Admin test](https://newbedev.com/testing-custom-admin-actions-in-django)
- Code on how to delay jest test : [Jest Delay](https://stackoverflow.com/questions/46077176/jest-settimeout-not-pausing-test)
- Code on how to stop jquery animations for jest testing : [De-activate animations](https://stackoverflow.com/questions/61295452/jest-test-jquery-fadein-fadeout-on-specific-elements)

### Content 
- Information on individual hikes was found on the Government of Canada - Parks Canada website : [Parks Canada](https://www.pc.gc.ca/en/pn-np/ab/banff/activ/randonee-hiking)

### Media 
- The Lato font used was imported from [Google Fonts](https://fonts.google.com/)
- Fontawesome was used for icons, including icons for like, comments, user - [Font Awesome](https://fontawesome.com/)
- The applicaiton favicon was created from the "exchange" icon image on [Font Awesome](https://fontawesome.com/) 
- The default hike image : Photo by <a href="https://unsplash.com/@sickhews?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Wes Hicks</a> on <a href="https://unsplash.com/s/photos/hiking-boots?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Jumbotron background image : Photo by <a href="https://unsplash.com/@stephenleo1982?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Stephen Leonardi</a> on <a href="https://unsplash.com/s/photos/hiking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@caraventurera?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Cara Fuller</a> on <a href="https://unsplash.com/s/photos/hike-waterfall?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@larisabirta?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Larisa Birta</a> on <a href="https://unsplash.com/s/photos/hike?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@kalenemsley?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kalen Emsley</a> on <a href="https://unsplash.com/s/photos/hiking-canada?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@kalenemsley?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kalen Emsley</a> on <a href="https://unsplash.com/s/photos/hiking-canada?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@hollymandarich?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Holly Mandarich</a> on <a href="https://unsplash.com/s/photos/hiking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@toomastartes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Toomas Tartes</a> on <a href="https://unsplash.com/s/photos/hiking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@kalenemsley?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kalen Emsley</a> on <a href="https://unsplash.com/s/photos/hike?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@guernseyphotographer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Simon English</a> on <a href="https://unsplash.com/s/photos/hiking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@wanderingteddybear?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ted Bryan Yu</a> on <a href="https://unsplash.com/s/photos/hiking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Hike image : Photo by <a href="https://unsplash.com/@hiking_corgi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Vlad D</a> on <a href="https://unsplash.com/s/photos/hike-meadow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- Background for Register, Sign in and Sign out : Photo by <a href="https://unsplash.com/@baileyzindel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Bailey Zindel</a> on <a href="https://unsplash.com/s/photos/mountains?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
  
### Acknowledgments

- Thank you to my mentor Brian Macharia for his continuing help and feedback. His advice and tips have been very beneficial, especially in the area of coding standards and best practice.