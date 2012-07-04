pyShop
======

This is my attempt at teaching myself python and django.

The aim is to produce a simple shopping system. If you want to use it then feel free but please keep my copyright notices. And it's always nice if you could drop me a message and let me know where my code is being used.

Other than that feel free to use and modify.

Using
-----

Add the template dirs:
```python
	'products/templates',
	'cart/templates',
```
The best place for this would be in local_settings.py

Add the needed packages to the installed apps list:
```python
	'django.contrib.humanize', #This can be removed if you use your own templates
	'global',
	'products',
	'cart', #This one is optional if you don't want to have shopping cart functionality
```

Add the following entries to `urls.py`
```python
	(r'^', include('products.urls', namespace='products', app_name='products')), #The regex can be whatever you like.
	(r'^cart/', include('cart.urls', namepsace='cart', app_name='cart')), #This can be removed if you are not using the cart system.
```

If you are using the code as-is then you do not need to add the apps or update the urls.

You will also need to add your database connection info. I would recomend creating a local_settings.py that looks like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database',
        'USER': 'my_user',
        'PASSWORD': 'my_password',
        'HOST': 'my_server',
        'PORT': '',
    }
}
```

settings.py is already set up to handle local settings.

Then all you need to do is run `python manage.py syncdb` to make django add the needed database tables.

Sample data
-----------

There is also a set of sample data that can be loaded using `python manage.py loaddata sample_data.json` after you have synced the databse.
