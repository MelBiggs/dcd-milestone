!(static/img/screenshot.png)

[Link to Deployed Website]( https://dcd-milestone.herokuapp.com/)

# Code Institute Milestone Project 
## Recipe App - The Constant Cookbook 

The objective of this project was to build a MongoDB-backed Flask project for a recipe website. The purpose of this project is to "Create a web application that allows users to store and easily access cooking recipes", allowing users to **create**, **update**, and **delete** for their own recipes and to **read** those of others.

The Home page shows a logo header, with a navbar. Following that there are two cards. One generates a random recipe, while the other highlights the function of the website and gives some quick links. The navbar displays a link to the recipe page, login, registration, about and logout. If the user is logged in, it will also display a link to their profile and to the Create a Recipe page, and the login button will be removed. 

Clicking onto the Recipes page will bring them to a list of the recipes on cards. They can also filter by category e.g. dinner or dessert and search the database for a particular dish. Here they can click into individual recipes and view them by one. 

If they wish to create a recipe, following the link will bring them to a form they can enter to complete this. They can add fields to the ingredients and steps to facilitate a dish of any length. A user profile is available for them to see the dishes they have created.

The user can log in or register also and can view an About page to know more about the project. 

Social media links are included. 

I've included an Admin user, who has access to the categories and all user names. In Categories they can add, edit or delete a category. 


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
Allowing the users to leave comments on particular recipe pages. 
I would like the recipe images to be uploaded from the users PC rather than through a URL. While it worked fine for this project, I would like to add that ability as I feel it is more professional. 
I'd like to include the option to upload a profile picture also


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

### Libraries & Frameworks 

[JQuery](https://jquery.com/) - 
The project uses JQuery to simplify DOM manipulation.

[FontAwesome](https://fontawesome.com/) - 
Font Awesome is a great library of icons. I used this library for my link icons.

[Google Fonts](https://fonts.google.com/) - 
There is a great selection of fonts in the Google Fonts library, some of which I used in my project. 

[Materialize](https://materializecss.com/) - 
Materialize is a CSS Framework.

[Flask](https://www.palletsprojects.com/p/flask/) - 
Flask is a lightweight web application framework that runs my application.

[Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - 
Jinja is a modern and designer-friendly templating language for Python. 

[Pymongo](https://api.mongodb.com/python/current/) - 
PyMongo allowed me to work with MongoDB.

### Host

[Heroku](http://heroku.com/) - 
The app is hosted on Heroku

### Also

[Gifox](https://gifox.io/) - 
I used Gifox to record the website demo for my README file. I recorded it off the website [Am I Responsive](http://ami.responsivedesign.is/)

## Testing
* As an individual interested in cooking, I believe they will enjoy my website. I believe it is easy to navigate and they will find recipes easily.

* As a user interested in sharing their recipes, they can achieve this by registering or logging in and adding a recipe. I have placeholders in the forms to help them with this. 

* As a user of an older age, I want it to be as easily navigated as possible and attractive on a desktop or tablet. I believe it is laid out in a clear way and they will find what they need easily. 

* A younger person who wants to have the information presented in the most understandable way will find the website pleasant to use. A card on the landing page also explains the function of the site. 

I have tested the site throughout development and after to ensure all worked fine and linked to the database correctly. My friends and family were kind enough to also test the site for me on their own devices and were able to move through it with ease. 

However, during development, there was a bug with deploying to Heroku. Despite deploying successfully it would not create the application and gave an error stating it could not bind to the PORT. With the help of tutor support, we changed the Procfile to `web: gunicorn app:app` from `python3 app.py`. This allowed the application to display then on Heroku. 

### Code Validation

#### CSS
I validated my CSS code using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). This showed no errors.

#### HTML
I validated my CSS code using [W3C Markup Validation Service]( https://validator.w3.org/). This helped me to spot any small mistakes to the code and to clean it up. 

#### JavaScript
The JavaScript code in my project was validated using [JSHint]( https://jshint.com/). This was really useful in identifying any extra semicolons that I may have missed and for cleaning my code. 

### Responsiveness
I tested the responsiveness of the webpage on browsers such as Chrome, Microsoft Edge and Safari and on multiple mobile devices. The page is fully responsive and I am satisfied that it works well on all devices.

### Deployment onto Heroku 
To deploy my app onto Heroku, I completed the following steps from Gitpod, after setting up a repository on Github: 

1. Created a Procfile with the command echo web: python run.py > Procfile.
2. Created a requirement.txt file with the command sudo pip freeze --local > requirements.txt
3. I then used `<git add>` to add the files to the staging area before using the `<git commit -m "Description of work done">` command to commit the files.
4. I could then push my files into GitHub by using `<git push>`
5. I created my config vars - SECRET_KEY, IP PORT and MONGO_URI - within env.py.
6. In Heroku after setting up my new application, I entered my config vars to match what I had made them in my env.py file.
7. On Heroku's dashboard I chose Deploy and chose Github as my deployment method. 
8. I linked Heroku to the correct Github repository and clicked "Deploy" from the master branch. 

## Credits

### Content

I took inspiration from BBC Good Food and sourced the recipes from their site. I also took inspiration from recipe websites mentioned on the About page of my app! 

### Media

The favicon I used was found on [favicon.io](https://favicon.io/emoji-favicons/)

I used BBC Good Food for most of the images on the website. 

### Acknowledgements

I received tips on snippets of my code through [Stack Overflow](https://stackoverflow.com/), [CodePen]( https://codepen.io/) and [W3Schools](https://www.w3schools.com/).

I was able to get help from these links and users:

* <https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search> 
* <https://stackoverflow.com/questions/7118276/how-to-remove-specific-element-from-an-array-using-python> 
* <https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/>
* <https://stackoverflow.com/questions/2570972/css-font-border>

I am grateful to my mentor **Guido Cecilio** for his help with this project. I would also like to thank my mam and my friends for helping me test the responsiveness of the website.  

[Link to Deployed Website]( https://dcd-milestone.herokuapp.com/)
