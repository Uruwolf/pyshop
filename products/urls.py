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
