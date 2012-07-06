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

from django.db import models

class Catergory(models.Model):
	'''Contains the model for product catergories.
	Currently only contains a name'''
	name = models.CharField(max_length=100)

	def __unicode__(self):
		'''Returns the name of this catergory'''
		return self.name

class Product(models.Model):
	'''Contains the model for products.
	
	name = The name of the product
	description = The description, can contain html
	price = A decimal number to two paces to represent the price
	stock = An indication of how many units are available.'''
	catergory = models.ForeignKey(Catergory)
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.BigIntegerField(default=0)

	def __unicode__(self):
		''''Returns the name of this catergory'''
		return self.name
