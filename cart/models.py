
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
	name = models.CharField()
	address = models.TextField()
	phone = models.CharField(max_length=16)
	email = models.EmailField()

	def __unicode__(self):
		'''Returns the order ID'''
		return self.id
