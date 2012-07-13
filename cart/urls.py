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

Copyright (c) Steve "Uru" West 2012
'''

from django.conf.urls.defaults import *
from products.models import Catergory, Product

urlpatterns = patterns('cart.views',
	url(r'^$', 'index', name='index'),
	url(r'^add/(?P<item>\d+)$', 'add', name='add-item'),
	url(r'^remove/(?P<item>\d+)$', 'remove', name='remove-item'),
)
