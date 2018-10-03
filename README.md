# cs4501team15
CS4501 Market Place Project - Building a market for limited/designer shoes that you can either sell or trade.

# Getting Started
To run this marketplace app for shoes, you must run 
```
docker-compose up
```

This will setup the local environment for the app at "http://localhost:8001/api/v1/inventory" and the databases that catalog all the shoes, users, inventory, and transactions will be loaded into a json file.

# Using the App
There are 4 types of models that the user can create, edit, or delete. To access each type, they can change the url end. Ex: "http://localhost:8001/api/v1/shoe" When a model is created, edited, or deleted, it will update the database containing the data.
