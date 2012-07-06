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

from products.models import Catergory, Product
from django.contrib import admin

#Catergories get the generic admin treatment
admin.site.register(Catergory)

class ProductAdmin(admin.ModelAdmin):
	'''Contains the admin panel settings for product objects
	Currently set to display the name and catergory,
	be filterable by catergory
	and searchable via name and description.'''
	list_display = ('name', 'catergory')
	list_filter = ['catergory']
	search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)
