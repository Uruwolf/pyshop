from django.http import HttpResponse

def index(request):
	return HttpResponse('ZOMG! This is the index page!')
