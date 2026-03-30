from django.shortcuts import get_object_or_404,render
from .models import Book
from django.http import Http404
from django.db.models import Avg
# Create your views here.

def index(request):
    all_books = Book.objects.all().order_by('-title')
    count_of_books = all_books.count()
    average_rating = all_books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html",{
        "books": all_books,
        "total_number_of_books":count_of_books,
        "average_rating":average_rating
    })

def book_detail(request,slug):
    # try:
    #     book = Book.objects.get(pk=id) #instead of pk can use id as a parameter automaticallu added by django and it is this parameter that is primary key
    # except:
    #     raise Http404()
    # book = get_object_or_404(Book,pk=id)#shortcut for code commented code block
    book = get_object_or_404(Book, slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "isBestSeller":book.isBestSelling
    })
