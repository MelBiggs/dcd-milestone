[Link to Deployed Website]( link )

# Code Institute Milestone Project 
## Recipe App - The Constant Cookbook 

The objective of this project was to build a MongoDB-backed Flask project for a recipe website. The purpose of this project is to "Create a web application that allows users to store and easily access cooking recipes", allowing users to **create**, **update**, and **delete** for their own recipes and to **read** those of others.

The Home page shows a logo header, with a navbar. Following that there are two cards. One generates a random recipe, while the other highlights the function of the website and gives some quick links. The navbar displays a link to the recipe page, login, registration, about and logout. If the user is logged in, it will also display a link to their profile and to the Create a Recipe page, and the login button will be removed. 

Clicking onto the Recipes page will bring them to a list of the recipes on cards. They can also filter by category e.g. dinner or dessert and search the database for a particular dish. Here they can click into individual recipes and view them by one. 

If they wish to create a recipe, following the link will bring them to a form they can enter to complete this. They can add fields to the ingredients and steps to facilitate a dish of any length. A user profile is available for them to see the dishes they have created.

The user can log in or register also and can view an About page to know more about the project. 

Social media links are included. 


## UX

The main goal in the design of this project was to build a recipe website that visualised the database information in an easily navigable way. 

I wanted to implement a colour palette which was light and gave a fresh feeling to the user.

With this website, the target audience consists of all age groups who have an interest in cooking and food. 

[Here is a link to my UXD document] (UXD/UXD .pdf)
[Here is a link to my second UXD document] (UXD/UXD-dcd.pdf)


### User Stories

* As an individual interested in cooking, I want to view the recipes from any device and find particular recipes with ease. I want to see recipes from other users to get inspiration. I don't want to have to be logged in to view the recipes. I believe this is achieved through the layout of the recipe page along with the searching capabilities. 

* As a user who wants to share a recipe, I want to be able to login and add my recipes. I want to be able to edit and delete these recipes as I choose. The user is able to do this when using the Constant Cookbook. 

* As a user who may be of an older demographic, I want a website which is easily navigated so that I can move through the webpage with ease.

* As a user who may be of a young demographic, I want the information to be laid out in a way that is understandable in order to make the most of the information present. 

## Wireframes

[Here is a link to my wireframe](UXD/Wireframe-dcd.pdf)


## Features
### Existing Features
My website consists of the following features: 
* **Decorative header**: The landing page of the website includes a header to introduce the name of the website. 

* **Navbar**:  The navbar displays a link to the recipe page, login, registration, about and logout. If the user is logged in, it will also display a link to their profile and to the Create a Recipe page, and the login button will be removed. 

* **Flash Messages**: flash messages communicate to the user regarding their interactions. 

* **Registration**: While a user is free to use the site as a guest, some features are not available unless logged in.I have built-in authentication to check certain criteria is met before an account is validated. All passwords are hashed for security purposes.

* **Log-in/Logout**:The login page has an input form where the users can enter their username and password. If the password is incorrect an error message will appear. New users can click on the link "Register here" to get redirected to the register page. Clicking the logout button will log the user out of the account. 

* **Recipes Page**: On this page, the user can view all recipes on this page, and can go to a particular meal type if they click on the category buttons. They can also search through the recipes on this page. 

* **Search**: Using the search bar, a user can check for a particular recipe that they have in mind. 

* **Add a Recipe**: A logged-in user can add a recipe using a form which allows them to add fields to steps and ingredients. They can choose selective fields from the dropdowns. 

* **Individual Recipe Page - Editing, Deleting & Liking**: Any user can view a recipe, while a logged-in user can 'like' a recipe by clicking the heart icon. If the logged-in user is the one who created that recipe, they have the option to edit or delete the recipe. 

* **Category buttons**: This feature allows the user to filter the recipes according to their desired meal type e.g. Dinner, Breakfast. 

* **Footer**: A footer at the end contains social media links. 

* **Profile Page**: Each registered user will get their own profile page where they can see the recipes they have created and edit their information. 


### Features Left to Implement

In the future, I would like to add more features to this website, such as:

Offering users the chance to 'Favourite' a recipe and having that added to their profile page for their ease. 
I would like the recipe images to be uploaded from the users PC rather than through a URL. While it worked fine for this project, I would like to add that ability as I feel it is more professional. 


## Technologies Used

### Programming Languages 

[HTML](https://en.wikipedia.org/wiki/HTML) -
HTML was used to control the layout and the structure of the dashboard.

[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) -
Cascading Style Sheets are used to describe the appearance of a website and I used it to make my website look appealing to the user.

[Javascript]( https://www.javascript.com/) - 
Javascript was used to introduce the interactive elements to the project. 

[Python3]( https://www.python.org/) - 
Python is often used as a “scripting language” for web applications. This means that it can automate specific series of tasks, making it more efficient. It was used to run the backend application.

### Tools

[Gitpod](https://www.gitpod.io/) - 
Gitpod is the code editor I used to write the application.

[MongoDB]( https://www.mongodb.com/) - 
MongoDB Atlas was used to store my database

[Gitpod](https://www.gitpod.io/) - 
Gitpod is the code editor I used to write the application.

### Frameworks 

[Flask]( https://www.palletsprojects.com/p/flask/) - 
XXXX

[Materialize](https://materializecss.com/) - 
Bootstrap is a very useful CSS Framework. You can save time writing code by using the Bootstrap predefined design templates. It has a great grid system and is responsive to different screen resolutions.

### Libraries 

[JQuery](https://jquery.com/) - 
The project uses JQuery to simplify DOM manipulation.

[FontAwesome](https://fontawesome.com/) - 
Font Awesome is a great library of icons. I used this library for my link icons.

[Google Fonts](https://fonts.google.com/) - 
There is a great selection of fonts in the Google Fonts library, some of which I used in my project. 

[Materialize](https://materializecss.com/) - 
Materialize is a CSS Framework.

### Also

[Gifox](https://gifox.io/) - 
I used Gifox to record the website demo for my README file. I recorded it off the website 
[Am I Responsive](http://ami.responsivedesign.is/)

## Testing
* As an individual interested in finding recipes, I believe XXX.

* As a user of an older age, I want it to be as easily navigated as possible and attractive on a desktop or tablet. 

There was a bug with deploying to Heroku. Despite deploying successfully it would not create the application and gave an error stating it could not bind to the PORT. With the help of tutor support, we changed the Procfile to web: gunicorn app:app from python3 app.py. This allowed the application to display then on Heroku. 

### Code Validation

#### CSS
I validated my CSS code using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). This showed no errors.

#### HTML
I validated my CSS code using [W3C Markup Validation Service]( https://validator.w3.org/). This helped me to spot any small mistakes to the code and to clean it up. 

#### JavaScript
The JavaScript code in my project was validated using [JSHint]( https://jshint.com/). This was really useful in identifying any extra semicolons that I may have missed and for cleaning my code. 

### Jasmine
When researching whether to test my code with Jasmine, I could use Jasmine to test XXX

I created tests for these which can be seen in `<graphSpec.js>` and run by previewing `<tests.html>` or on [Github](https://melbiggs.github.io/ifd-milestoneproject/tests.html). You may need to refresh the page a few times to see an accurate result.

### Responsiveness
I tested the responsiveness of the webpage on browsers such as Chrome, Microsoft Edge and Safari and on multiple mobile devices. The page is fully responsive and I am satisfied that it works well on all devices.

### Peer Code Review
I published my project on the Code Institute's 'Peer Code Review' channel. This channel allows other students to have a look at your code and offer suggestions and comments to improve your project. 

## Deployment

### Deployment onto Heroku 

## Credits

### Content

### Media
The favicon I used was found on [favicon.io](https://favicon.io/emoji-favicons/)

### Acknowledgements
I received inspiration for the theme of this project from

I received tips on snippets of my code through [Stack Overflow](https://stackoverflow.com/), [CodePen]( https://codepen.io/) and [W3Schools](https://www.w3schools.com/).

I am very grateful to my mentor **Guido Cecilio** for his help and guidance throughout the project. I would also like to thank my mam and my friends for helping me test the responsiveness of the website. I would also like to thank the Code Institute Slack users for their helpful comments and suggestions on my project. 

[Link to Deployed Website