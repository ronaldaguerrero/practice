from django.shortcuts import render, HttpResponse, redirect
from .models import Show

def index(request):
	context = {
		'all_shows' : Show.objects.all()
	}
	return render(request, 'first_app/index.html', context)

def add_show(req):
	req.POST['title']
	req.POST['network']
	req.POST['date']
	req.POST['desc']
	new_show = Show(title=req.POST['title'], network=req.POST['network'], date=req.POST['date'], description=req.POST['desc'])
	new_show.save()
	return redirect('/')
