from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Review
from .forms import ReviewForm
# Create your views here.


def review(request):
    if request.method == "POST":
        # existing_data here is used to call the object that already in database and passing it to instance help update data
        # existing_data = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_data)
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    
    return render(request,"reviews/review.html",{
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
