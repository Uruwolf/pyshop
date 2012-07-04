pyShop
======

This is my attempt at teaching myself python and django.

The aim is to produce a simple shopping system. If you want to use it then feel free but please keep my copyright notices. And it's always nice if you could drop me a message and let me know where my code is being used.

Other than that feel free to use and modify.

Using
-----

Make sure that '/products/templates' has been added to the list of template dirs and add 'django.contrib.humanize' and 'products' to the list of installed apps.

Then all you need to do is run 'python manage.py syncdb' to make django add the needed database tables.

You will also need to add your database connection info. I would recomend creating a local_settings.py that looks like this:

```
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
