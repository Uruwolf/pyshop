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
