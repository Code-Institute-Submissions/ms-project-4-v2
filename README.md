[Link to the live project](https://ip-school-lunch-co-v-2.herokuapp.com/)


# The School Lunch Co - Forth Milestone Project

This project was created for an imaginary business providing lunch delivery service to local schools.

## User Experience (UX)

### Project Goals

The primary Project Goal is to create a marketing website for 'The School Lunch Co'.

The target audience are parents of school-aged children who are looking for school lunch delivery service.

### User Stories

#### Registration and User Accounts

* As a Site User I want to be able to
    * easily register for an account so that I can view my profile.
    * receive an email confirmation to verify that the account registration was successful.
    * easily reset my password in case I forget it so that I can recover access to my account.
    * use my username and password to login into the application.
    * logout of my account.

#### Viewing and Navigation

* As a Customer I want to be able to
    * view a list of available products.
    * view individual product details, e.g. the product image, price and description.
    * view the total cost of the items selected for purchase.

#### Product Sorting

* As a Customer I want to be able to
    * sort a specific category of product so that I can find products in a specific category.

#### Purchasing and Checkout

* As a Customer I want to be able to
    * view items in my bag so that I can see what items I have selected and what is the total cost of products to be purchased.
    * update or remove products so that I can make changes to items in the bag before checkout.
    * easily enter my payment information.
    * view a confirmation of order after checkout.


### Design choices

* I used [Bootstrap](https://getbootstrap.com/) CSS framework because it allows to design websites quickly and effectively.

* Cookie font from [Google fonts](https://fonts.google.com/) was chosen for the logo. Cookie is a script typeface based on brush calligraphy. It is sweet and friendly - but not too decorative.

### Wireframes

Wireframes are available [here ](https://github.com/ip69719/ms-project-4-v2/tree/main/documents/wire_frames)


## Features

* All pages have Navigation Bar which was created using [Bootstrap](https://getbootstrap.com/) navbar component. 
* The Mobile Collapse Button will appear on smaller screens. The navigation bar will show as a dropdown when the button is clicked.
* Home page contains a short message briefly describing the service provided by the organisation.
* Users have the ability to register for an account, log in and out.
* Customers can view all the available products by clicking on the "All Products" dropdown option from the "Menu Options" navbar link on the main menu.
* Customers can view products in a specific category by selecting product category from the "Menu Options" dropdown on the main navbar.
* By clicking on the product image the Customer is redirected to the product detail page where the information about the product including the price is displayed.
* Users can easily add products to the shopping bag. The content of the shopping bag can be viewed at any point.
* Users can edit the quantity of products in the bag and also have the ability to remove selected products from the bag.
* The checkout page displays the summary of the order and invites the Customer to complete the purchase by filling out the order form and inputting card details.
* The Customer is presented with a confirmation message if the order was successfully processed.


## Features Left to Implement
* User's profile page for registered users that would store customer details and keep a history of customer orders.
* Admin and Store management system that would allow to add, edit or delete products.

## Technologies used

### Languages used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) used to create the structure of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) used to style the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) used for add interactive behavior.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) used to created logic of the website.
* [Django Template Language](https://docs.djangoproject.com/en/4.0/ref/templates/language/) used for template inheritance, loops and if statements in the html files.


### Frameworks, Libraries & Programs Used

* [Django](https://www.djangoproject.com/) web framework was used to create the application.
* [Bootstrap](https://getbootstrap.com/) used to style the website.
* [Amazon Web Services s3](https://aws.amazon.com/) used to store our static files and images.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) is used to store the projects code after being pushed from Git.
* [Balsamiq Wireframes](https://balsamiq.com/) was used to create wireframes for the project.
* [Google fonts](https://fonts.google.com/) were used to import the 'Cookie cursive' and 'Roboto' fonts into the style.css file.
* [Font Awesome](https://fontawesome.com/) was used to obtain the icons.


## Testing

### Code Validation

* The W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no syntax errors.

    * W3C Markup Validator - [Results](https://github.com/ip69719/ms-project-4-v2/tree/main/documents/testing/w3c_markup_validator)

    * W3C CSS Validator - [Results](https://github.com/ip69719/ms-project-4-v2/tree/main/documents/testing/w3c_css_validation)


### User Story testing

* **As a User I want to be able to easily register for an account so that I can view my profile.**
    * New User can register by clicking on the "sign up" link on the login page. Alternatively, the User can click on the Register dropdown option from Account navbar link on the main menu [test_01](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_01.pdf).

* **As a User I want to be able to receive an email confirmation to verify that the account registration was successful.**
    * New user is required to confirm their e-mail address before an account is created [test_02](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_02.pdf).

* **As a User I want to be able to easily reset my password in case I forget it so that I can recover access to my account.**
    * User can reset password by clicking on the "Forgot Password?" link on the login page [test_03](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_03.pdf).

* **As a User I want to be able to use my username and password to login into the application.**
    * By clicking on the login navbar link the user is presented with a log in form where the user can enter their username and password.
    * Confirmed that existing User can log in to application by clicking on the Sign In button after inputting credentials into username and password fields.

* **As a User I want to be able to logout of my account.**
    * User can log out of the application by clicking on the Logout navbar link on the main menu [test_04](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_04.pdf).

* **As a Customer I want to be able to view a list of available products.**
    * Customers have the ability to view all the available products by clicking on the "All Products" dropdown option from the "Menu Options" navbar link on the main menu. Product image and brief description is displayed for every product [test_05](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_05.pdf).

* **As a Customer I want to be able to view individual product details, e.g. the product image, price and description.**
    * By clicking on the product image the Customer is redirected to the product detail page where the information about the product and price can be found. [test_06](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_06.pdf).

* **As a Customer I want to be able to view the total cost of the items selected for purchase.**
    * The total costs are recalculated after each product is added to shopping bag and the amount is displayed in the top right corner of the main navbar. [test_07](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_07.pdf).

* **As a Customer I want to be able to sort a specific category of product so that I can find products in a specific category.**
    * Customers have the ability to view products in a specific category by selecting product category from the "Menu Options" dropdown on the main navbar. [test_08](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_08.pdf).

* **As a Customer I want to be able to view items in my bag so that I can see what items I have selected and what is the total cost of products to be purchased.**
    * Customers can view the content of the shopping bag at any point by clicking on the icon in the top right corner of the main navbar. The shopping bag page contains the list of products selected, quantity of each item to be purchased and displays the total cost of the order. [test_09](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_09.pdf).

* **As a Customer I want to be able to update or remove products so that I can make changes to items in the bag before checkout.**
    * The Customer has the ability to adjust items in the shopping bag by updating product quantity and clicking on the 'update' link. Alternatively, the Customer can remove products from the bag by clicking on 'remove' link. The total cost of the order is recalculated on adjustments. [test_09](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_09.pdf).

* **As a Customer I want to be able to easily enter my payment information.**
    * The Customer is redirected from the shopping bag to the checkout page when the 'Go to Checkout' button is clicked. Here the Customer is invited to fill out the order form. The Customer can enter card details in the payment section of the form and submit the order [test_10](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_10.pdf).

* **As a Customer I want to view a confirmation of order after checkout.**
    * The Customer is presented with a confirmation message when the order was successfully processed [test_11](https://github.com/ip69719/ms-project-4-v2/blob/main/documents/testing/test_evidence/test_11.pdf).


* Known Bugs

    * The site is not fully responsive on smaller screens.


## Deployment

### Heroku

The project was deployed to Heroku using the following steps:

1. Log in to Heroku
1. Click New in the top right corner and select "Create a New App"
1. Give the app a name and select the closest region, then click 'Create App'
1. Click on Resource tab Add-On Heroku Progres database
1. Select a Development plan
1. Configure variables for:
    * AWS_ACCESS_KEY_ID   
    * AWS_SECRET_ACCESS_KEY
    * DATABASE_URL
    * EMAIL_HOST_PASS
    * EMAIL_HOST_USER
    * SECRET_KEY
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET
    * USE_AWS
1. Note that the automatic deployment from GitHub repository is currently unavailable.
1. From the Gitpod terminal run heroku login -i command and login to Heroku
1. Initialise Heroku app: heroku git:remote -a (followed by Heroku app name)
1. Run git push heroku main command.
1. Click "Open app" to launch the app from the Heroku website once the deplayment has completed or use the link provided in the terminal.


### Amazon Web Services S3 

1. Go to [Amazon Web Services](https://aws.amazon.com/) and create a free accout.
1. Create S3 Bucket, enable static website hosting add permissions (Cross-origin resource sharing (CORS)), add Bucket policy and update Access control list (ACL)
1. Navigate to Identity and Access Management (IAM) and create user group.
1. Create an access policy giving the group access to the S3 bucket.
1. Assign the user to the group.


## Credits

### Content

* Content of READ.md was written with reference to [Example README.md template](https://github.com/Code-Institute-Solutions/SampleREADME).

### Media

* Images were sourced from [Shutterstock](https://www.shutterstock.com/home) and [Dreamstime](https://www.dreamstime.com/)

### Code

* Used Code Institute Boutique Ado Project tutorial as a reference to implement project idea.

### Acknowledgements

* Special thanks to Code Institute for exellent leaning materials.