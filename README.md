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