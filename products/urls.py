'''
This file is part of pyShop

pyShop is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyShop is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyShop.  If not, see <http://www.gnu.org/licenses/>.

Copyright (c) Steve "Uru" West 2012 <uruwolf@gmail.com>
'''

from django.conf.urls.defaults import *
from products.models import Catergory, Product

#Contains the list of catergories for the list and detail view
catergory_set = {
		'queryset': Catergory.objects.all(),
}

#Contains the list of products for the detail view
product_set = {
		'queryset': Product.objects.all(),
}

urlpatterns = patterns('',
	#Routing information to get to the list of catergories.
	url((r'^$', 'django.views.generic.list_detail.object_list', catergory_set), name='catergory_list'),

	#Contains routing information for the catergory detail view (Basically a list of products)
	url(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', catergory_set, name='catergory_detail'),

	#Routing information for the product detail page
	url(r'^product/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', product_set, name='product_detail'),
)
