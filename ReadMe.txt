Does the web application use Django to serve static HTML content?
Yes
Has the learner committed the project to a Git repository?
Yes
Does the application connect the backend to a MySQL database?
Yes.
Are the menu and table booking APIs implemented?
Yes
Is the application set up with user registration and authentication?
Yes
Does the application contain unit tests?
Yes
Can the API be tested with the Insomnia REST client?
Yes

Unittest:
python manage.py test tests/



/auth/users
-POST method:
    Allows everyone to register an account when supplied with the data:
        username
        Password  
        email  

/auth/users
-GET method: 
    Retrieves all Users information 
/auth/users/<username>
    Retrieves specified user information

User token generation:
In Insomnia
/restaurant/api-token-auth/
 -POST method 
    Creates token when input the data
	username
	password

User login from browser
/auth/token/login
-POST method
	Give Username and Password to login with token.
/auth/token/logout
-POST methos
	give the user token in JSON format to logout.
	Eg:
	{
    "auth_token": "4a6b8c2dc566d348ceaa7c8934e0ec42a12d0d3e"
	}

Menu API:
Insomnia test cases:
/restaurant/menu-items/
-GET method
   Bearer token : 4a6b8c2dc566d348ceaa7c8934e0ec42a12d0d3e
	Retrieves all the menu items.
-POST Method
	Bearer token : 4a6b8c2dc566d348ceaa7c8934e0ec42a12d0d3e
	Body as JSON :
{
    "id": 6,
    "title": "Strawberry Cake",
    "price": "7.00",
    "inventory": 50
}

-PUT method
	Bearer token : 4a6b8c2dc566d348ceaa7c8934e0ec42a12d0d3e
	Body as JSON with updated field:
{
    "id": 6,
    "title": "Strawberry Cake",
    "price": "7.00",
    "inventory": 40
}
/restaurant/menu-items/<item id>
-GET Method
	Retrieves the information about specified menu item 
- DELETE MEthod
	Deletes the specified menu item.

Booking API:
/restaurant/booking/tables
-GET method
	Retrieves all the booking list
-POST method
	Allows to book a table when give the inputs
	Name
	no_of_guests
	BookingDate with time





