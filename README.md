
# Hikini 

![HIKINIE](static/assets/mockups/hikinie.png)

HIKINIE , Hiking In ireland 
A website for hikers to find best trails in Ireland , create their profiles , upload images & reviews 
and get in touch with other hikers 

This the 3rd milestone project for a Software Development Diploma in Code Institute .

The websit built by Python , Flask in Backend , MongoDb as Database , HTML, CSS , JS and Materialize in the Front end.
## UX

HIKINIE is a place where Hikers can find the best trails In Ireland and Join the other HIkers in discussions.
In this website users can go through the following :

#### New website Visitor
Visitor is the new user who is not have an account yet:
- Visitor can explore Best Trails in HIKINIE & Hikers .
- Visitor can visit each trail page and see more details about the trail like:
    - Trails Info like Name , County , Category , Length , Estimated time , rating & Map location
- Visitor can see the trail reviews by other hikers with rating , also can read comments 
- Visitor can visit hiker profile to see details like
    - Hiker name , bio , social media links , hiker gallery , and reviews made by this hiker
- If visitor want to engage with hikers or add a trail to his plan visitor need to sign in or login 

#### Hikers 
Hiker is website user with valid account , along with above can :
- hiker can create personal profile with bio , Social media & profile image .
- Hiker can add a trail to plan or mark it as a completed.
- Hiker can add review for a trail if completed with rating 
- Hiker can write about a trail as a plan 
- Hiker can add a comment for trail reviews
- hiker can comment on trail review in other hikers profile
- hiker can upload images to his galler , the images will showe in his profile and the trail page
- hiker can delete own reviews , also can delete his account 

#### Admin
 Admin is the website owner
 along with above features
- admin can add new trails to thw website 
- admin can edit trail info
- admin can remove a trail from website

### Design 
The website bullit to be simple and acheive users goal 
Mockups refrence :

- [Mockup-Desktop-home-page](static/assests/mockups/desktop-home-page.png)
- [Mockup-Desktop-All-Trails](static/assests/mockups/desktop-allplaces.png)
- [Mockup-Desktop-Hiker-PAge](static/assests/mockups/desktop-userprofile.png)
- [Mockup-Desktop-Trail-Page](static/assests/mockups/desktop-hiking-place-page.png)


## Features

###### Home Page
    * Top Menu & Navbar 
        the menue links to the main pages in the website & login/sign up forms , if user logedin 
        the menue will show link to his account & logout form.

    * sign up form
        by filling the form an account will be created and user will redirct to a thank you page 
        with option to back to his account & update profile or continue explore HIKINIE
    * Login form
        if user with an account , user can login with email & password and will be redircted to 
        welcome page 
    * Main Slider 
        In home page the slider shows website purpose with links to all trails & all hikers
    * Top trails 
        in the home page the user will see trails cards with basic info and link to trail page to more details
    * Hikers Slider
        Carousel cards show hikers in HIKINIE with link to visit hiker profile
    * Sign up Call To Action 
        if user not sign up a CTA link with sign up form 
    

###### Trail Page
    * Main Image for the trail
    * Trail Basic info
    * Trail review 
        the review in trail page is the average rating by hikers in HIKINIE reprecented in stars
    * Trail location
        a map card to show the trail location 
            * future : I am plan to link this card with Google map API for trail location
    * Add the trail
        A Modal form where Hiker can add the trail as a completed with rating & reviews or as plan with post 
        to show other hikers his plan for this trail
    * Trail gallery
        the gallery is an images uploaded by hikers with refrence to this trail 
    * Trails reviews
        A Collapsibles cards to show trail reviews , by click on trail comments will show.
        Each review with details of made by whome and rating if the trail completed 
            * future : The comments icon will show number of comments for each review

 ###### Hiker Page
    * Hiker Profile Header
        Profile image with Hiker name , Image , bio & social media links
    * Edit profile 
        If hiker in his account he can click to edit profile to update profile info
    * Upload Image
        Modal form where hiker can paste a url for an image and link with trail per name from trail list
            * future : Option to upload image from mobile or instagram
    * Hiker Gallery 
        A slider of Hiker Images.
    * Hikers reviews
        Hikers reviews with option of comment to each review ,
        if hiker in his page he can delete the post


## Technologies Used

 * HTML5 
 * CSS 
 * Javascript 
 * [Materialize ](https://materializecss.com/) 
 * [Owl Carousel](https://owlcarousel2.github.io/OwlCarousel2/) Carousel slider
 * [Gitpod](gitpod.io) as an IDE 
 * Python
 * Flask
 * [werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
 * [MongoDB](https://www.mongodb.com/) Database

## Testing
* Functions Testing 
    * New User can Explore The main Features without access to Add trails , Add comments 
    * New user can fill the sign up form & create account successfuly and redircted to thank you page
    * If new user have an account , loge in form work successfuly and redirct to welcome page

            Hiker is the user with an account in HIKINIE
    * Hiker can add a trail as plan , write the post & redircted to the trail page 
    * Hiker can mark the trail completed with rating & redircted to the trail page 
    * Hiker can add comment for any trail review post
    * new reviews with rating will be count in trail average rating
    * Hiker can edit profile , upload image and redircted to his profile with update info
    * If some info in edit form not changed , the old info will remain without change
    * Hiker can upload images to gallery & Images will show in hiker gallery
    * Hiker can delete posts

    * Admin can edit trails info successfuly
    * Admin can delete trails successfuly
    * Admin Can add trails successfuly

For HTML & CSS Testing I used 
* [W3C Mark-up Validation Service](https://validator.w3.org/) HTML Validator
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) CSS Validator


## Deployment
The Deployment was through Heroku
- after push the code to github in Heroku app page for hiking project
- in deploy section
- link Heroku with github account
- choose the hiking project repo. 
- in Manual deploy 
- Choose a master branch to deploy
- click to deploy



## Credits
Edit profile form function to change only new data was in code insbired from stack overflow [answer](https://stackoverflow.com/a/24824812/14122351)
and refrence in mongodb [doc](https://docs.mongodb.com/manual/reference/operator/aggregation/cond/)
### Content
- Trails info from [spunout](https://spunout.ie/) 
[Best places to hike in Ireland](https://spunout.ie/health/exercise/hike-in-ireland)

### Media
- Images uploaded from [Pexels](https://www.pexels.com/) 

### Acknowledgements

- I received inspiration from [Hiking Ireland](https://www.facebook.com/groups/hikingirelandgroup) Group In Facebook

#### Disclaimer

**The content of this website is for educational purposes only.**