from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^shopping/', include('shopping.foo.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	(r'^', include('products.urls', namespace='products', app_name='products')),
	(r'^cart/', include('cart.urls', namespace='cart', app_name='cart')),
)
