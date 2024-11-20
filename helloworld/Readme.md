
# Django Hello World Project

## Steps to Create a Django "Hello World" Application

### Step 1: Install Django
To start, you need to install Django. Run the following command to install Django via `pip`:

```bash
pip install django
```

### Step 2: Create a Django Project
Create a new Django project using the `django-admin` command:

```bash
django-admin startproject helloworld
cd helloworld
```

This will create a new folder called `helloworld` with the necessary files for your project.

### Step 3: Create a Django App
Now, create a new app within the project to manage the "Hello World" functionality:

```bash
python manage.py startapp hello
```

This will create a folder called `hello`, which will contain the structure for your app.

### Step 4: Create a View for "Hello World"
In the `hello` app, open the `views.py` file and add a simple view that returns a "Hello, World!" message:

```python
# hello/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

### Step 5: Define the URL
Now, you need to tell Django to map a URL to the view. Open the `urls.py` file in your project folder (`helloworld/urls.py`) and add the following:

```python
# helloworld/urls.py
from django.contrib import admin
from django.urls import path
from hello import views  # Import the views from the hello app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),  # Map the URL to the view
]
```

### Step 6: Run the Development Server
To see the "Hello World" message, start the Django development server:

```bash
python manage.py runserver
```

The server runs by default on `http://127.0.0.1:8000/`. Open your browser and navigate to `http://127.0.0.1:8000/hello/`. You should see "Hello, World!" displayed on the page.

### Final File Structure
Your project structure should look like this:

```
helloworld/
├── helloworld/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── hello/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── views.py
└── manage.py
```

That's it! You've successfully created a simple Django "Hello World" application.