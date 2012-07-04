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
``

Add the needed packages to the installed apps list:
```python
	'django.contrib.humanize', #This can be removed if you use your own templates
	'global',
	'products',
	'cart', #This one is optional if you don't want to have shopping cart functionality
```

`urls.py` will also have to be updated. Simply add `(r'^', include('products.urls', namespace='products', app_name='products')),`. By default this makes the index page the list of catergories but this can be easily changed. Just change the regex to something like `r'^shop'` or whatever you want to use.

You will also need to add your database connection info. I would recomend creating a local_settings.py that looks like this:

```python
TEMPLATE_DIRS = (
        '/location/of/manage.py/shopping/products/templates'
)

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
