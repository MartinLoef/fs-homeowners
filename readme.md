# [Commonhold website](https://commonhold.herokuapp.com/)

Travis says:<br>
[![Build Status](https://travis-ci.com/MartinLoef/fs-homeowners.svg?branch=master)](https://travis-ci.com/MartinLoef/fs-homeowners)


## What you have to know about the project and VvE(commonholds)
This is the fourth project created for the Full Stack Web Developer course by [**Code Institute**](https://codeinstitute.net).<br>

The goal here was to create a full stack application, using Django with multiple apps and (in my case) a PostGres database.  

<b>In order to understand the purpose of this project, there are a few things that you have to know about the way things are done in the Netherlands:</b>

Owner’s association (VvE) (Commonhold would be the closest English word to match it)<br>

Dutch law prescribes that those who own an apartment in the same building, are automatically unified in an owner’s association. 
It is impossible to exclude yourself from membership if you own an apartment, and it is impossible to be a member of the association without owning an apartment. 
The Dutch term for such association is ‘Vereniging van Eigenaren’, loosely translated as ‘Association of Owners’. 
The Dutch abbreviation is VvE, which we use in this article.


The VvE looks after the joint interests of the owners of the apartments, like making sure the building is maintained, 
cleaned, and insured. Decisions in the VvE are taken in a democratic fashion: the ‘meeting of owners’ is organized periodically, 
and every owner holds one vote for each apartment he or she owns. Most regular decisions require majority consent, 
more radical decisions often super majority (more than 75% or a higher percentage) of the votes.

More information about the shared ownership can be found [here](https://www.vvewiki.nl/owning-apartment-netherlands).

### Goal
This site would help VvE's to organize and make contact which each other more easy.
HomeOwners can post blogs about things that are happing in and around the appartment complex, where other can comment on it.
Also events can be created/posted which are free to join, or where (extra) payment is needed for.

Events can be like:
- Clean up the garage together (Join option instead of Subscribe with payment option)
- Maintain the shared garden (Join option instead of Subscribe with payment option)
- Organize a new year's drink (Subscribe with payment)
- Organize a BBQ for the complex (Subscribe with payment)
- When is garbage collected 
- Next Annual VvE meeting (Join option instead of Subscribe with payment option)

<b>Important thing to remind is that it is a closed community, where you can not sign up as an outsider.
The board of the VvE is the only authority to add and remove users to this site.</b>

For the project, **Django** was used as framework, with **Heroku** for hosting the site and database and **Amazon (AWS)** for file storage.

## Biggest Lessons Learned
The biggest lessons i have learned during this project are:
1. Never push your ENV variables with secret keys to Github. I made this mistake with secret values from the AWS site. This resulted within 15 minutes with a mail and phonecall from Amazon that my credentials
were compromised. I needed to make a new key with new values, and most complicated thing was to remove the env file from all previous commits in github.
2. Never try to push files larger than 50MB to github, it doesn't like that (i made a MP4 video as a demo with a size of 130 MB). It took a while to remove that from the local Git repo.

## UX
With a site that is aimed at fpr closed communities, the sign up should be limited. The only way a user should be able to join
a site like this, is when the board of owners can acknowledge that the user is indeed a new resident. A contact option would be 
a nice way to get in touch.

The other goals are that members should be able to post blogs and events. This will most likely be done on a small device
when people are sitting on the couch, bed or any other travelling spot.

In case of organized events, on behalf of the board, a cart and payment options should be in place in order to handle these kind 
of functionality.

The site has a main focus on the smaller devices instead of the larger devices.

## User Stories 
User Stories VvE Site:

1. <done> As a VvE i want the site to be closed subscription because it contains data that belongs to only those who live in the shared appartment complex
2. <done> As a VvE i want to be able to add and suspend users to the site
3. <done> As a VvE i want that users can reset their passwords themselves
4. <done> As a VvE i want to be able to delete and add content to the page
5. <done> As a VvE i want to be able to offer payment options to the site in order to receive automatically money on event subscriptions

1. <done> As a user i want to be able to create and delete(my) blogs
2. <done> As a user i want to be abe to create and delete (my) events 
3. <done> As a user i want to be able to reset my passwords
4. <done> As a user i want to be able to join, like or subscribe to blogs or events  
5. <done> As a user i want that my orders are only visible for myself
6. <done> As a user i want to see who joined free events
7. <done> As a user i want to be able to pay with a credit card for payed events 

Manual check section will show what and who is able to do what on the site.


## Database Design
Herunder an impression how the database should look like.
It is purely an impression how it should be connected to each other.
Please dont hang me up on the relations(Foreign keys etc) visible in this picture because it wasn;t the goal to make a perfect DB schema map, but just as a mockup.

<img src="https://github.com/MartinLoef/fs-homeowners/blob/master/readme_screenshots/db_schema/db_schema.png" width=100%  alt="Architecture">


## Wireframess
For user stories and wireframe mockups created as part of this project, see the [**Word document**]

## Features
### Existing Features
- Opening page with a with a picture of a appartment complex (currently the on I live in)  
   **a.** Sign In Button to the login page <br>
   **b.** Button to open the contact form in case of no account
- Navbar containing links to (when not authenticated):  
   **a.** homepage / index page<br> 
   **b.** sign-in page  
- Navbar containing links to (when authenticated as normal user):  
   **a.** homepage / index page <br>
   **b.** OrderHistory <br>
   **c.** Blogs <br>
   **d.** Events<br>
   **e.** Cart<br>
- Navbar containing links to (when authenticated as Admin user):  
   **a.** homepage / index page <br>
   **b.** OrderHistory <br>
   **c.** Blogs <br>
   **d.** Events<br>
   **e.** Add User <br>
   **f.** Registered Users Overview<br>

- Overview page shows<br>
  **a.** the next 5 upcoming events<br>
  **b.** the latest posted blog<br>
  **b.** the newest added event<br>

- Contact form transcript is only mailed to the registered mail account from the appartment board
- Cart page linking to checkout page
- Blog page showing all blogs
- Event page showing all events
- OrderHistory page showing all orders that were done by that user
- Checkout with (test) payment system for credit card using Stripe
- Mail sent to user after checkout with list of items, submitted address and order ID
- Staff / Admin page added into the site  
   **a.** Register / Add User --> new mamber will receive an email that accout is created (has to go password reset functionality) 
   **b.** Activate or suspend User  
- Standard Django admin pages allow addition, change or deletion of events, blogs, users, comments, orders  
- Account owners can reset their passwords themselves via the 'I forgot my login option' on the signin page. 
- Example of mail that are send by the site can be viewed at: [here](https://github.com/MartinLoef/fs-homeowners/blob/master/readme_screenshots/mail/)


### Features Left to Implement
- Overview of payed subscribers for events (so other people know who is going)
- Add emoticons to comments
- Edit possibility of a comment when you are the writer of the comment
- Further Mail styling
- Upgrade to Stripe v3
- Add more payment options (and receivers --> organizer vs VvE bankaccount)

## Technologies Used
- **HTML**, **CSS**, **Javascript/jQuery**, **Python** were all at the heart of things
- [**Django**](https://www.djangoproject.com/) - The entire site uses **Django 1.11.20** as its framework  
   Django pip-installed add-ons used:  
   *django-materializecss-form* - used for the styling of the forms in Materialize  
   *stripe* - used in processing of payments<br>
   *django-storage* - used for the AWS storage<br>
   *boto3* - used for the AWS storage  
   *dj-database-url* - used for Heroku PostGres integration  
- [**BootstrapCSS**](https://getbootstrap.com/) - The site is styled based on **BootstrapCSS 4.0**  
   99% of the site is build with out of the box bootstrap 4 css, only a few custom css styles were used which can be found in the custom.css file
- [**Stripe**'s stripe.js](https://stripe.com/) - test version used for (m/f)aking payments.  
   *No actual payments can be made*
- [**JQuery**](https://jquery.com) - The project uses **JQuery** to simplify DOM manipulation.  
   *Additional javascript was used to perform some enhancements as well, for accordion and modal behavior.*

## Testing
Testing the site has been ongoing from the very start, with each and every addition tested manually and/or automated with the help of
[**Travis CI**](https://travis-ci.org/).  
In my opinion every aspect of the site was extensively manually tested.

[**See Manual_test.md file**](https://github.com/MartinLoef/fs-homeowners/blob/master/manual_test.md).<br>

### Scaling on the different browsers / devices
The site has been tested on multiple environments:  
   **a.** Google Chrome (Desktop) - *both direct and using developer tools to emulate devices*  
   **b.** Safari (Desktop)  
   **c.** Google Chrome (Mobile) - *installed on iPhone 8 and iPad (2018)*  
   **d.** Safari (Mobile) - *installed on iPhone 8 and iPad (2018)*  
   **e.** Opera (Mobile)
   **f.** Developer tools - *emulated versions of Pixel 2 (XL), iPhone 6/7/8(Plus) and X and iPad(Pro)*

Scaling on all devices works as intended. The site does not scale well to the old phone models(iPhone 5, Galxy S5). 
Because these are not very common phones anymore i didnt go to the limit to make the site also on those devices perfect.
I choose to focus on most common devices instead of (semi-)obsolete mobile phones.

### Bugs encountered
Actually all bugs i have ran into, were thanks to my own stupidity and stuborness.
These bugs were correct along the way the site progressed and after posting, viewing, liking events and blogs during manual tests (feels like a 1000 times)

After deploying to Heroku i found out that i had 2 different MEDIA_URL's defined. Which gave me some headache before i found that.

The question actually is: are these things really bugs or just extra knowledge?

## Deployment
[**See Deployment.md file**](https://github.com/MartinLoef/fs-homeowners/blob/master/deployment.md).<br>


## Credits

### Content
Content of the site is all self written based on the things i have encountered during the time I live in appartment complexes

### Media 
To mention something about this subject, i have used the bootstrap sites, facebook.com to get ideas about how to style and lay-out
this page. This is show by the amount of custom made css which is very low (in my opinion)

### Acknowledgements
My girlfriend which had to put up with me during my 'WTF why isnt this working' moments.<br>
Support from the tutors and teachers from [**Code Institute**](https://codeinstitute.net).<br>
Amazing CSS styles invented and made public useable by [**BootstrapCSS**](https://getbootstrap.com/)<br>
StackOverflow community for all my (stupid) questions [**Stackoverflow**](https://stackoverflow.com/)<br>
Database mockup made with [**SqlDBM - Online Database Modeler**](https://app.sqldbm.com/)
