# [Commonhold website](https://commonhold.herokuapp.com/)

Travis says:<br>
[![Build Status](https://travis-ci.com/MartinLoef/fs-homeowners.svg?branch=master)](https://travis-ci.com/MartinLoef/fs-homeowners)

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

## UX
With a site that is aimed at fpr closed communities, the sign up should be limited. The only way a user should be able to join
a site like this, is when the board of owners can acknowledge that the user is indeed a new resident. A contact option would be 
a nice way to get in touch.

The other goals are that members should be able to post blogs and events. This will most likely be done on a small device
when people are sitting on the couch, bed or any other travelling spot.

In case of organized events, on behalf of the board, a cart and payment options should be in place in order to handle these kind 
of functionality.

The site has a main focus on the smaller devices instead of the larger devices.

#### Wireframe and User Stories
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
In my opiion every aspect of the site was extensively manually tested.

In the [**Word document**]()
in the root of the repository, a chapter is dedicated to the tests, including screenshots of manual testing, 
overview of automated tests and the result as Travis relays.  
Some app's contain a `tests.py` file. In order to run all tests manually instead of using Travis, 
go to a terminal prompt, and enter `python3 manage.py test` to run all tests.  
In order to run tests for a specific app, enter (e.g.) `python3 manage.py products` where products is the app to run the tests for.

Testing (manually) was done every step of development, as well as automated (in a later stadium) using **[Travis](https://travis-ci.org)**

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

The question actually isare these things really bugs or just extra knowledge?

## Deployment

I assume that you know your way with Linux and Github. How to clone/dowload an repository and to make it work on your dev environment

Deployment
This project is deployed and hosted on Heroku using Postgres Database and AWS S3 Bucket to host static and media files. 

Needed to get it all to work
1.	Cloud 9 account(https://c9.io/)
2.	Heroku Account  (https://www.heroku.com/)
4.	Travis Account (https://travis-ci.com/)
3.	Github Repository (https://github.com/)
5.	Create a email address (https://accounts.google.com)
6.	AWS S3 (https://aws.amazon.com)
7.	Stripe dev account (https://stripe.com/)<br>


1.	Cloud9<br>
	**a.** 	Select a Blank workspace<br>
		Open terminal window and install the packages mentioned in the requirements.txt (make sure the versions are the same)<br>
		The Install command is like: sudo pip3 install <package-name>==<version><br>
	**b.**	Open .bashrc file and add the local enviroment variables to it:
			export EMAIL_ADDRESS="<_your email>"<br>
			export EMAIL_PASSWORD="<_your email pwd>"<br>
			export SECRET_KEY="<_your secretkey, remove it from the settings file!!>"<br>
			export STRIPE_PUBLISHABLE="<_your stripe publishable key>"<br>
			export STRIPE_SECRET="<_your stripe secret key>"<br>
			export AWS_ACCESS_KEY_ID="<_your AWS Access Key>"<br>
			export AWS_SECRET_ACCESS_KEY="<_your AWS Secret Access key>"<br>
			export DTAP="Dev"<br><br>
		MAKE SURE TO REFRESH THE .BASHRC file  (terminal: <type command: . ~/.bashrc>)
<br><br>
	**c.**	Create a database and superuser on the workspace<br>
	**d.**	Dont forget to makemigrations and migrate in order to get your modals into the database<br>
	**e.**   Update settings.py file to contain the right settings
		Settings file contains logic to determine on what environment the site is working<br>
		Have a look at the settings file for the full logic, hereunder i will mention some specific ones you have to pay attention to.
		
		<generic OS variables>
		ALLOWED_HOSTS = [os.getenv('C9_HOSTNAME'),'<your heroku app>']
		
		<setting up your email>
		EMAIL_USE_TLS = True
		EMAIL_HOST = 'smtp.gmail.com'
		EMAIL_PORT = 587
		
		<specific mentioned parameters for your prod>
		AWS_STORAGE_BUCKET_NAME = '<your bucket name'>
		AWS_S3_REGION_NAME = '<your region name>'
    
		<see also custom_storages.py>
		STATICFILES_LOCATION = 'static'
		STATICFILES_STORAGE = 'custom_storages.StaticStorage'
		
		<get your media files to work with amazon>
		MEDIAFILES_LOCATION = 'media'
		DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    
		MEDIA_URL = 'https://%s/%s/' % (
			AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
		MEDIA_ROOT = (
			os.path.join(BASE_DIR, 'media'),
        )
	d.	Create requirements.txt Run command $ pip3 freeze --local > requirements.txt<br>
	e.	Create Procfile and custom_storages.py in root directory<br>
	f.	IF AWS IS ALREADY IN PLACE: Collect static files and upload to S3 by running $ python3 manage.py collectstatic
	
	
2.	Github
	a.	Create a repository<br>
	b.	Init git on cloud9 <br>
	c.	add github repository master to your work environment<br>
	d.	git add ., git commit -m "your message", git push origin master<br>
	
3.	Heroku<br>
	a.	Add an App to your account<br>
	b.	Link it to your github repository<br>
	c.	Go to settings and add the Variables to it<br>
		-	AWS_ACCESS_KEY_ID = <_your own><br>
		-	AWS_SECRET_ACCESS_KEY = <_your own><br>
		-	DATABASE_URL = <_your own><br>
		-	DISABLE_COLLECTSTATIC = 1	<br>
		-	SECRET_KEY = <_your own><br>
		-	STRIPE_PUBLISHABLE = <_your own><br>
		-	STRIPE_SECRET = <_your own><br>
		-	DTAP = "Prod"<_br>
		-	EMAIL_ADDRESS = <_your own><br>
		-	EMAIL_PASSWORD = <_your own><br>
		-	IP = 0.0.0.0<br>
		-	PORT = 5000<br>
	d. Connect your heroku to your github repository for automatic deployment.

4.	setup travis account with your github repo, add travis tag to your readme.md

5.	Amazon Web Services:
	Follow the amazon webtutorials to create Bucket, IAM user, Groups and policies.	

6. All setup is done, go to heroku and open the app.

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

