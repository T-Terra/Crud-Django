# Crud-Django

Run specific test
```cmd
python manage.py test crud.tests.SeleniumTestes.testAddUser
```
Run all tests
```cmd
python manage.py test
```
Generate secret key
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```