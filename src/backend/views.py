from django.shortcuts import render

# Create your views here.
def homePage (request):
	context = {}
	template = 'index.html'
	return render(request, template, context)
    
    
def workPage (request):
	context = {}
	template = 'work.html'
	return render(request, template, context)    
    
    
def servicesPage (request):
	context = {}
	template = 'services.html'
	return render(request, template, context)
    
def contactPage (request):
	context = {}
	template = 'contact.html'
	return render(request, template, context)   
    
    
def aboutPage (request):
	context = {}
	template = 'about.html'
	return render(request, template, context)   