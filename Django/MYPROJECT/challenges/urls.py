from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.challenge_page, name = "index"),
    path("<int:month>",views.redirect_months),
    path("<str:month>",views.monthly_challenges, name = "main_url"),
]