## Deployment

I assume that you know your way with Linux and Github. How to clone/dowload an repository and to make it work on your dev environment

What do you need to get it to work:
1.	Cloud 9 account(https://c9.io/)
2.	Heroku Account  (https://www.heroku.com/)
4.	Travis Account (https://travis-ci.com/)
3.	Github Repository (https://github.com/)
5.	Create a email address (https://accounts.google.com)
6.	AWS S3 (https://aws.amazon.com)
7.	Stripe dev account (https://stripe.com/)<br>

This project is deployed and hosted on Heroku using Postgres Database and AWS S3 Bucket to host static and media files. 

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