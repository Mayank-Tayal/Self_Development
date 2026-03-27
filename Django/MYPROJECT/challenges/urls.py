from django.urls import path
from . import views

urlpatterns = [
    # static way to add urls
    # path("january", views.index),
    # path("febuary",views.schedule),

    path("",views.challenge_page),
    # redirection
    path("<int:month>",views.redirect_months),

    # dynamic ways to add url
    path("<str:month>",views.monthly_challenges, name = "main_url"),
]