from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

# Static Approach
# def index(request):
#     return HttpResponse("This WOrks!")


# def schedule(request):
#     return HttpResponse("You need to go for running!!!!")






# Dynamic Aproach
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
    # data = ""
    month_list = list(metadata.keys())

    # for month in month_list:
    #     mod = month.capitalize()
    #     month_path = reverse("main_url",args= [month])
    #     data += f"<li><a href = \" {month_path}\">{mod}</a></li>"
    # respo = f"<ul>{data}</ul>"
    # return HttpResponse(respo)
    return render(request,"challenges/index.html",{
        "months": month_list
    })


def monthly_challenges(request, month):
    try:
        text = metadata[month]
        # responseData = render_to_string("challenges/challenge.html")
        # return HttpResponse(responseData)

        # kinda like shortcut above 2 lines can be reduced to this single line
        return render(request, "challenges/challenge.html",{
            "output" : text,
            "month" : month.capitalize()
        })
    except:
        return HttpResponseNotFound("Not supported")



# redirection
def redirect_months(request, month):
    months = list(metadata.keys())
    if month > len(months):
        return HttpResponse("Invalid!!!")
    redir_month = months[month - 1]
    redir_path = reverse("main_url", args=[redir_month])
    # return HttpResponseRedirect("/challenges/" + redir_month)  #hardcoded path
    return HttpResponseRedirect(redir_path)    #dynamic path

    