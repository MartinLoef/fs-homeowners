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
- Clean up the garage together
- Maintain the shared garden
- Organize a new year's drink
- Organize a BBQ for the complex
- When is garbage collected
- Next Annual VvE meeting

<b>Important thing to remind is that it is a closed community, where you can not sign up as an outsider.
The board of the VvE is the only authority to add and remove users to this site.</b>

For the project, **Django** was used as framework, with **Heroku** for hosting the site and database and **Amazon (AWS)** for file storage.

## UX

## Features
### Existing Features


### Features Left to Implement

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