# MySport Blog

Stay ahead of the game with My Sport Blog News, your go-to source for the latest updates, insights, and analyses in the world of sports. Whether you're a die-hard fan, a casual follower, or an aspiring athlete, our blog covers everything from breaking news and match highlights to in-depth features and exclusive interviews.

- Link to deployed site - [https://my-sportblog-d25b82c351ce.herokuapp.com/](https://my-sportblog-d25b82c351ce.herokuapp.com/)
- Link to GitHub repository - [https://github.com/baselhn-cmd/mysportblog-pp4](https://github.com/baselhn-cmd/mysportblog-pp4)

## Table of Contents

- [My sport blog](#my-sport-blog)
  - [Table of Contents](#table-of-contents)
  - [Wireframes](#wireframes)
  - [Post and Comment Relationship Diagram](#post-and-comment-relationship-diagram)
  - [User Stories](#user-stories)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Future Features](#future-features)
  - [Setting up Django](#setting-up-django)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
    - [Django Testing](#django-testing)
    - [Automated Testing](#automated-testing)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Libraries \& Frameworks](#libraries--frameworks)
    - [Acknowledgements](#acknowledgements)
  
## Wireframes

- At the start of the project, I created some basic wireframes to visualize the design I had in mind for the site. I used moqups.com to develop these wireframes, covering the home page, sign-in, signup, and about pages.

<details><summary>Wireframe Home</summary> 

![Wireframe Home](static/images/home1.png)
</details>

<details><summary>Wireframe Sign Up</summary>

![Wireframe Signup](static/images/signup1.png)
</details>

<details><summary>Wireframe Login</summary>

![Wireframe Profile](static/images/login1.png)
</details>

<details><summary>Wireframe About</summary>  

![Product About](static/images/about.png)
</details> 

## Post and Comment Relationship Diagram

- Initial plan

<details><summary>Post and comment relationship model</summary>

![post and comment relationship model](static/images/post_comment_relationship.png)
</details>

<details><summary>Post Model</summary>

![post model](static/images/post-model.png)
</details>

<details><summary>Comment Model</summary>

![comment model](static/images/comment-model.png)
</details>

## User Stories

- As a site user, I can view a paginated list of posts so that I can select which post I want to view.
- As a Site User / Admin, I can view comments on an individual post so that I can read the conversation.
- As a Site User I can register an account so that I can comment on a post.
- As a Site User I can leave comments on a post so that I can interact with the listings
- As a Site User I can modify or delete my comment on a post.
- As a Site Admin I can create, read, update and delete posts so that I can manage the listings.
- As a Site Admin I can create draft posts so that I can finish writing the content later.
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

## Features

- Pagination  The posts are paginated so that the user can view 6 posts per page. There is a link to the next page at the bottom of the page. When the user is not on the first page of listings, there is a link to the previous page.

<details><summary>Pagination</summary>

![Pagination](static/images/next.png)
![Pagination](static/images/prev.png)
</details>

- Navbar
The navbar is anchored to the top of the page, providing effortless navigation throughout the site. It features a concise set of essential links, including:

Home page
About page
Login/Logout page
Register page
This design ensures that users can quickly access key sections of the website, enhancing overall usability and user experience

<details><summary>Navbar</summary>

![navbar](static/images/navbar.png)
</details>

- Login Status 

A prominent banner, situated below the navigation buttons, dynamically displays the user's login status, clearly indicating whether they are:

Logged in
Not logged in
This intuitive feature keeps users informed about their current login state, ensuring a seamless and personalized experience on the site.

<details><summary>Login Status</summary>

![Status](static/images/status2.png)
![Status](static/images/status3.png)
</details>

- About Page This site talking about the developer 

- Register Page

<details><summary>Register</summary>

![regestration](static/images/regestration.png)
</details>

- Login Page

<details><summary>Login</summary>

![login](static/images/login.png)
</details>

- Logout Page

![logout](static/images/logout.png)

## Technologies Used

- HTML - The project uses HTML to create the structure of the site.
- CSS - The project uses CSS to style the site.
- JavaScript - JavaScript was used to link the buttons to functionality
- Python - The project uses Python to create the backend of the site.
- Django - The project uses Django as the web framework.
- Heroku - The project is deployed on Heroku.
- Git - The project uses Git for version control.
- GitHub - The project uses GitHub to store the code and to plan the project.
- Postgres - The project uses Postgres as the database.
- Bootstrap - The project uses Bootstrap to style the site.
- Google Fonts - The project uses Google Fonts to import the font used in the site.
- ElephantSQL - The project uses ElephantSQL to host the database.
- Draw.io - The project uses Draw.io to create the wireframe.
- Cloudinary - The project uses Cloudinary to host the images.

## Future Features

- The next feature of the site will be like the post i´m working on but it´s not done yet

Setting Up Django: A Step-by-Step Guide

To set up Django for my site, I followed these steps:

Installation of Required Packages
I installed the necessary packages, including Django, Gunicorn, Psycopg2, Django Heroku, Django Crispy Forms, Pillow, Cloudinary, DJ Database URL, and Whitenoise.

Creating a New Django Project and App
Next, I created a new Django project and app, laying the foundation for my site.

Database Setup and Superuser Creation
I migrated the database and created a superuser to manage the site's admin tasks.

Configuration Files
I created a Procfile and a requirements.txt file, which are essential for deploying the app on Heroku.

Admin Account and Models
I created an admin account and defined the models for the site, then migrated the database again to apply the changes.

Database Hosting and Connection
I used Elephantsql to host the database and connected it to the site using a newly created instance. The DJ Database URL package helped link the database to the site.

Views, URLs, Templates, and Static Files
I created the views and URLs for the site, followed by the templates and static files.

Forms and Heroku Deployment
I created the forms for the site and then logged into Heroku to create a new app. I linked the app to my code base via GitHub and deployed it early to monitor for any bugs during the build process. By redeploying the app, I ensured everything was working as expected.

Config Vars and Final Touches
Finally, I added the necessary config vars to Heroku to connect the database and Cloudinary image hosting, completing the setup process.