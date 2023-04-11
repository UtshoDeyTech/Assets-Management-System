## Asset Tracking App

This is a Django-based web application that allows users to track company assets and their assigned employees. It also includes a RESTful API that allows users to access and manipulate data for the `Company`, `Employee`, and `Device` models.

### Features

- User authentication and authorization
- CRUD (Create, Read, Update, Delete) operations for `Company`, `Employee`, and `Device` models
- Asset check-out and check-in functionality for devices
- RESTful API for accessing and manipulating data

### Installation

1. Clone the repository: `git clone https://github.com/UtshoDeyTech/Assets-Management-System`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the server: `python manage.py runserver`

### Usage

To access the web application, navigate to `http://localhost:8000/` in your web browser. You can log in using your superuser account or create a new account by clicking on the "Sign Up" link. Once logged in, you can view, add, edit, or delete companies, employees, and devices. You can also check out a device to an employee and check it back in when it is returned.

To access the RESTful API, navigate to `http://localhost:8000/api/` in your web browser. You can access the following endpoints:

- `/companies/`: List all companies or create a new company
- `/companies/{id}/`: Retrieve, update, or delete a specific company
- `/employees/`: List all employees or create a new employee
- `/employees/{id}/`: Retrieve, update, or delete a specific employee
- `/devices/`: List all devices or create a new device
- `/devices/{id}/`: Retrieve, update, or delete a specific device

You can use a tool such as `curl` or `httpie` to send HTTP requests to these endpoints.

### Development

This application was built using Django and Django REST framework. The `asset_tracking` app contains the web application logic, while the `api` app contains the API logic.

The `models.py` file in the `asset_tracking` app defines the models for the `Company`, `Employee`, and `Device` objects. The `views.py` file defines the views for displaying and manipulating these objects in the web application. The `urls.py` file defines the URLs for these views.

The `serializers.py`, `views.py`, and `urls.py` files in the `api` app define the serializers, views, and URLs for the RESTful API.

### Testing

This application includes automated tests for the `HomeView` view. To run the tests, navigate to the project directory and run `python manage.py test`.

### Deployment

This application can be deployed to a production environment using a variety of methods, including:

- Hosting on a cloud service such as Heroku or AWS
- Setting up a virtual private server (VPS) and using a service like Gunicorn or uWSGI to run the application
- Using a containerization platform such as Docker and deploying to a cloud service or VPS

### License

This project is licensed under the MIT License.

### Credits

This project was created by Utsho Dey.
