****************************************************************************************
1. For advisor signup use curl:
****************************************************************************************

curl --location 'http://127.0.0.1:8000/zfund/advisor/signup' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Name of your advisor",
    "mobile": "Mobile no. of advisor"
}'


Response:
{
    "message": "Advisor account created successfully."
}


****************************************************************************************
2. To add product in table

****************************************************************************************

curl --location 'http://127.0.0.1:8000/zfund/add-product/' \
--header 'Content-Type: application/json' \
--data '{
    "product_name": "product name here",
    "description": "description of Product here",
    "category":"Write category here"
}'

Response:
{
    "message": "Product added successfully.",
    "product_id": id,
    "product_name": "product name here",
    "category": "category here"
}


****************************************************************************************
3. To add client

****************************************************************************************

curl --location 'http://127.0.0.1:8000/zfund/advisor/add-client' \
--header 'Content-Type: application/json' \
--data '{
    "advisor_id": "Advisor id here",
    "client_name": "Cient name here",
    "client_mobile": "Mobile number here"
}'

Response:

{
    "message": "Client {client_name} added to advisor {Advisor_name} successfully."
}


****************************************************************************************
4.To get the client list associated with any advisor
****************************************************************************************

curl --location 'http://127.0.0.1:8000/zfund/advisor/list-clients/<int:advisor_id>/' \
--header 'Content-Type: application/json' \
--data ''

Response:

Client list in response

****************************************************************************************
5. To create client/ client signup
****************************************************************************************

curl --location 'http://127.0.0.1:8000/zfund/user/signup' \
--header 'Content-Type: application/json' \
--data '{
    "user_name": "Client name here",
    "user_mobile": "mobile number here"
}'

Response:

{
    "message": "User account created successfully."
}

****************************************************************************************
6. If advisor want to purchange product for particular client
****************************************************************************************

curl --location 'http://127.0.0.1:8000/zfund/advisor/purchase-product/<int:advisor_id>/<int:user_id>/' \
--header 'Content-Type: application/json' \
--data '{
    "product_id": "product id here"
}'


Response:
{
    "message": "Product {Product_name} associated with user {Cient_name} by advisor {Advisor_name} successfully.",
    "ProductLink=": "https://producturl/10" #this is static url which we can change in future accordingly
}