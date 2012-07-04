from django.conf.urls.defaults import *
from products.models import Catergory, Product

catergory_set = {
		'queryset': Catergory.objects.all(),
}

product_set = {
		'queryset': Product.objects.all(),
}

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', catergory_set),
	url(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', catergory_set, name='catergory_detail'),
	url(r'^product/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', product_set, name='product_detail'),
)
