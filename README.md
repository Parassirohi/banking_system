# banking_system

Banking System API

This is a RESTful API for managing banks and their branches. The API has the following endpoints:

banks/: Returns a list of all banks.
banks/<int:bank_id>/: Returns the details of a specific bank.
branches/: Returns the branches of all banks.
banks/<int:bank_id>/ifsc/: Returns a list of all branches of a specific bank.


Technology Stack
This API is built using Django Rest Framework, which is a powerful and flexible toolkit for building Web APIs.


Getting Started
To get started with the API, follow these steps:


Clone the repository.
Install the requirements by running pip install -r requirements.txt.
Run the migrations by running python manage.py migrate.
Load the data by running python manage.py loaddata banks.json.


Models
This API has two models: Bank and Branch.


Bank Model
The Bank model has the following fields:
name: The name of the bank.

Branch Model
The Branch model has the following fields:

name: The name of the branch.
ifsc: The unique IFSC code assigned to the branch.
address: Address of bank.
district: 
city:
state:
bank: A foreign key to the bank model.


Serializers
This API uses ModelSerializers to serialize the Bank and Branch models.

Viewsets
This API uses ModelViewSet to handle CRUD operations for the Bank and Branch models.

Running Tests
To run the tests for the API, run the following command:
python manage.py test


Conclusion
This API provides a simple and easy-to-use interface for managing banks and their branches.
With the power of Django Rest Framework, it can be easily extended to handle more complex use cases.
