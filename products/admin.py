from products.models import Catergory, Product
from django.contrib import admin

admin.site.register(Catergory)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'catergory')
	list_filter = ['catergory']
	search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)
