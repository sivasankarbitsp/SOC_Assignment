To run this application, Execution Instruction
	The serviceendpoint.py is started and listens on port 5002.
	This API gateway application is configured with the correct url.
o	Here in this case local host
	Then apigateway.py is started and listens on port 5001, which routes the incoming API requests to the required service.


Use Postman tool to generate API request
curl - Client url is alternate option to send requests

Example commands

#To Add/ register new user
	http://localhost:5001/userservice/users/register	
	
#To Add/ register new product
	http://localhost:5001/productservice/products/register


JSON format

# product 
{
    "productid": "prodct488",
    "productname": "ProductC",
    "productprice": "Rs.200/-",
    "productdescription": "This is Product c"
}

# user account
{
    "username": "sivasankar",
    "password": "siva123"
}

