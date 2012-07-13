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


from django.http import HttpResponse
from django.core.urlresolvers import reverse
from settings import CART_SESSION_NAME
from products.models import Product
from django.template import Context, loader
from django.shortcuts import redirect

def index(request):
	ensureSessionCart(request.session)

	product_list = []
	#Loop through and build a list of products
	for product in request.session[CART_SESSION_NAME].keys():
		p = Product.objects.get(pk=product)
		#Hijack the model for the quantity in the basket
		p.quantity = request.session[CART_SESSION_NAME][product]
		product_list.append(p)

	c = Context({
			'product_list': product_list
	})

	return HttpResponse(loader.get_template('cart/cart.html').render(c))

def add(request, item):
	ensureSessionCart(request.session)
	request.session[CART_SESSION_NAME][item] = 1
	request.session.modified = True
	return redirect('cart:index')

def remove(request, item):
	ensureSessionCart(request.session)
	del request.session[CART_SESSION_NAME][item]
	request.session.modified = True
	return redirect('cart:index')

def ensureSessionCart(session):
	if CART_SESSION_NAME not in session:
		session[CART_SESSION_NAME] = dict()
