from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

metadata = {
    "january": "1st Month",
    "february": "2nd Month",
    "march": "3rd Month",
    "april": "4th Month",
    "may": "5th Month",
    "june": "6th Month",
    "july": "7th Month",
    "august": "8th Month",
    "september": "9th Month",
    "october": "10th Month",
    "november": "11th Month",
    "december": "12th Month",
}


def challenge_page(request):
    
    month_list = list(metadata.keys())

    return render(request,"challenges/index.html",{
        "months": month_list
    })


def monthly_challenges(request, month):
    try:
        text = metadata[month]
        

        
        return render(request, "challenges/challenge.html",{
            "output" : text,
            "month" : month.capitalize()
        })
    except:
        return HttpResponseNotFound("Not supported")



def redirect_months(request, month):
    months = list(metadata.keys())
    if month > len(months):
        return HttpResponse("Invalid!!!")
    redir_month = months[month - 1]
    redir_path = reverse("main_url", args=[redir_month])
    return HttpResponseRedirect(redir_path)    #dynamic path

    