# Não envidas

Site where you can add "anonymous" messages for special people.
Messages we wish had sent to someone, but they weren't sent 

https://user-images.githubusercontent.com/21327808/128564993-a9979ab2-0789-4355-9426-6f27509c08e5.mp4

### Prerequisites

What do you need to install the application
  - Python 3.9+

## Running the project

Create a virtual environment
```python
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies
```python
pip install -r requirements.txt
```

Apply the migrations
```
python manage.py migrate
```

Create admin user
```
python manage.py createsuperuser
```

Run the project
```
python manage.py runserver
```
