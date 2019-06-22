from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
def book(req):
	books = {
		'all_books': Book.objects.all()
	}
	print(books)
	return render(req, 'first_app/index.html', books)

def add_book(req):
	if req.method == 'POST':
		new_title = req.POST['title']
		new_desc = req.POST['desc']
		new_book = Book.objects.create(title=new_title, desc=new_desc)
		print(new_book)
	return redirect('/')

def view_book(req, id):
	context = {
		'this_book' : Book.objects.get(id=id),
		'this_books_authors' : Book.objects.get(id=id).authors.all(),
		'non_authors' : Author.objects.all()

	}
	return render(req, 'first_app/book_view.html', context)


def author(req):
	authors = {
		'all_authors': Author.objects.all()
	}
	print(authors)
	return render(req, 'first_app/authors.html', authors)

def add_author(req):
	if req.method == 'POST':
		new_fn = req.POST['first_name']
		new_ln = req.POST['last_name']
		new_author = Author.objects.create(first_name=new_fn, last_name=new_ln)
		print(new_author)
	return redirect('/authors')

