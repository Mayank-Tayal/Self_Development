from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Review
from .forms import ReviewForm

# Create your views here.

# DeleteView - Can help with deleting data
# UpdateView - Can help with updating data

class ReviewView(CreateView):
    model = Review 
    # no need for form_class when you only need to configure form fields,,, 
    # but cannot adjust labels and errors
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"



class ThankYouView(TemplateView):
   
   template_name = "reviews/thank_you.html"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["message"] = "This Works!!"
       return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    # if we want specified data to display
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        favourite_id = self.request.session.get("favourite_review")
        context["is_favourite"] = str(loaded_review.id) == favourite_id
        return context 


class FavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)