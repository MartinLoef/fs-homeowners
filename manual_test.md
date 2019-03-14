### Automated Testing

Testing the site has been ongoing from the very start, with each and every addition tested manually and/or automated with the help of
[**Travis CI**](https://travis-ci.org/).  

Some app's contain a `tests.py` file. In order to run all tests manually instead of using Travis, 
go to a terminal prompt, and enter `python3 manage.py test` to run all tests.  
In order to run tests for a specific app, enter (e.g.) `python3 manage.py accounts` where accounts is the app to run the tests for.
Testing (manually) was done every step of development, as well as automated (in a later stadium) using **[Travis](https://travis-ci.org)**

### Manual testing
Extensive manual testing has also been conduted to make sure that conditional content is viewed correctly for each type of user.  
In order to test appropriately ficticious user accounts have been created. 
Information on the users created and expected content visible can be found below:

**Sample Users**


|Function/Username          |Anonymous | Admin   | Mare no 62| Mare no 64| 
|---------------------------|:----------|:-----: |:---------:|:---------:|
| Authenticated             |    No     | Yes    |  Yes      |   Yes     |
| **BLOG**                  |           |        |           |           |
| Add Blog                  |    No     | Yes    |  Yes      |   Yes     |
| Add Blog Comment          |    No     | Yes    |  Yes      |   Yes     |
| Edit Own Blog             |    No     | Yes    |  Yes      |   Yes     |
| Edit other Blog           |    No     | Yes    |  No       |   No      |
| Delete Own Blog           |    No     | Yes    |  Yes      |   Yes     |
| Delete Other Blog         |    No     | Yes    |  No       |   No      | 
| Delete Own Blog Comment   |    No     | Yes    |  Yes      |   Yes     |
| Delete Other Blog Comment |    No     | Yes    |  No       |   No      |
| Like Blog                 |    No     | Yes    |  Yes      |   Yes     |
| Remove Like Blog          |    No     | Yes    |  Yes      |   Yes     |
| ** EVENT**                |           |        |           |           |
| Add Event                 |    No     | Yes    |  Yes      |   Yes     |
| Edit Own Event            |    No     | Yes    |  Yes      |   Yes     |
| Edit other Event          |    No     | Yes    |  No       |   No      |
| Add Event Comment         |    No     | Yes    |  Yes      |   Yes     |
| Delete Own Event          |    No     | Yes    |  Yes      |   Yes     |
| Delete Other Event        |    No     | Yes    |  No       |   No      | 
| Delete Own Event Comment  |    No     | Yes    |  Yes      |   Yes     |
| Delete Other Event Comment|    No     | Yes    |  No       |   No      |
| Like Event                |    No     | Yes    |  Yes      |   Yes     |
| Remove Like Event         |    No     | Yes    |  Yes      |   Yes     |
| Join Event(free)          |    No     | Yes    |  Yes      |   Yes     |
| Unjoin Event(free)        |    No     | Yes    |  Yes      |   Yes     |
| Subscribe Event           |    No     | Yes    |  Yes      |   Yes     |
| **ORDERS**                |           |        |           |           |
| See Own Orders            |    No     | Yes    |  Yes      |   Yes     |
| See Other Orders          |    No     | yes(db)|  No       |   No      |
|**USER Admin**             |           |        |           |           |
| Add user                  |    No     | Yes    |  No       |   No      |
| Suspend User              |    No     | Yes    |  No       |   No      |
| Activate User             |    No     | Yes    |  No       |   No      |
|**Password**               |           |        |           |           |
| Request PWD Reset         |    No     | Yes    |  Yes      |   Yes     |
| Receive reset url at mail |    No     | Yes    |  Yes      |   Yes     |
| **Contact**     			|           |		 |           |			 |
| Send Contact Forms		|	Yes		| Yes	 | 	Yes		 |	 Yes  	 |

 
*the password for each of the users above is Password123

**Logged out:**
    i. Able to see main page
    ii. Able to see signin page
    iii. Use of the contact form

**Logged in member:**
    i. Able to Add/Edit/Delete Blogs
    ii. Able to Add/Remove Blog Comments 
    iii. Able to Add / Remove and see Joins
    iv. Able to Add/Edit/Delete Events
	v. Able to Add / Remove Event Comments
	vi. Able to Subscribe to event
	vii. Able to dom payments
	
**Logged in Admin:**
	i. All from logged in member
	ii. Add User
	iii. Activate/Suspend user
    
**Forms & Inputs :**
    i. log in, log out, registration, forgotten password - all forms work correctly and display appropriate error messages where applicable
    ii. Forms have been tested for validation of fields
    iii. In case of incorrect input a message pops up with hint for correction

**Test Responsiveneness:**
This web app has been designed to display on various screen sizes. The variable view have been handled with a combination of bootstrap column settings in HTML and @media queries in CSS if necessary.
1.  Tests were done on actual iPhone 8 device, iPad using safari
2.  Windows 10, Chrome and Opera
3.  Dev tools from Google Chrome