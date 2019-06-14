from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(req):
	return redirect('/')

def show(request, my_val):
    return HttpResponse("placeholder to display blog number: " + str(my_val))
    
def edit(req, my_val):
	return HttpResponse("placeholder to edit blog: " + str(my_val))

def delete(req, id):
	return HttpResponse("placeholder for delete: " + str(id))

def another_method(req):
	pass

def yet_another(request, name):
    pass
    
def one_more(request, id, color):
    pass