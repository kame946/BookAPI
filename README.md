# Project Title
### REST API for a CRUD Resource using Django and PostgreSQL

## Description
The project is about building a REST API for a CRUD resource using Django and PostgreSQL. The API should provide CRUD functionality for a resource of your choice. In this project, the resource is books. The project has a simple front-end using Bootstrap and CSS. JavaScript and AJAX have been used for implementing client-side functionality for the front-end. The API has been tested using Postman to ensure that it is functioning correctly and returning expected responses.

##Installation
Clone the repository
1. Create a virtual environment
2. Install dependencies using pip install -r requirements.txt
3. Set up PostgreSQL and create a database
4. Copy the .env.example file to .env and update the environment variables with your values
5. Run migrations using python manage.py migrate
5. Run the development server using python manage.py runserver
## Usage
The API has been deployed to Heroku and can be accessed here. The API provides the following endpoints:

* GET /api/books/ - Get a list of all books
* POST /api/books/ - Create a new book
* GET /api/books/:id/ - Get details of a specific book
* PUT /api/books/:id/ - Update a specific book
* DELETE /api/books/:id/ - Delete a specific book
## Technologies Used
- Django
- PostgreSQL
- Django REST Framework
- Bootstrap
- JavaScript
- AJAX
- Postman
## Challenges Faced
* One of the challenges faced was setting up the PostgreSQL database and configuring the project to use it. This was overcome by following the official documentation and tutorials online.

* Another challenge was implementing client-side functionality using JavaScript and AJAX. This was overcome by referring to online resources and experimenting with different approaches.

## Future Improvements
In the future, we plan to add authentication and authorization to the API, allowing only authorized users to perform CRUD operations. We also plan to add more features to the front-end, such as search and filtering options.
