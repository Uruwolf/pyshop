
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

class Order(models.Model):
	'''Contains the model for orders

	order_status = The status of the order. Feel free to customise this below
	order_date = The date the order was placed
	name = Name of the person to ship to
	address = Address to ship to
	phone = Phone number
	email = Email
	'''
	ORDER_STATUS_CODES = (
		('0', 'recieved'),
		('1', 'payment processed'),
		('2', 'shipped'),
	)
	order_status = models.SmallIntegerField(choices=ORDER_STATUS_CODES)
	order_date = models.DateField(auto_now_add=True)
	name = models.CharField(max_length=100)
	address = models.TextField()
	phone = models.CharField(max_length=16)
	email = models.EmailField()

	def __unicode__(self):
		'''Returns the order ID'''
		return self.id

class OrderProduct(models.Model):
	'''Contains information about a product in an order
	
	order = The order that this is part of
	name = The name of the product
	unit_price = Cost per unit
	product = Orrignal product
	quantity = Number of units sold'''
	order = models.ForeignKey(Order)
	name = models.CharField(max_length=200)
	unit_price = models.DecimalField(max_digits=10, decimal_places=2)
	product = models.BigIntegerField()
	quantity = models.BigIntegerField()

	def __unicode__(self):
		'''Returns a more human readable represntation'''
		return self.name
