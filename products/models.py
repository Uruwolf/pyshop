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
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Product(models.Model):
	catergory = models.ForeignKey(Catergory)
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.BigIntegerField(default=0)

	def __unicode__(self):
		return self.name
