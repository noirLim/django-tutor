from django.shortcuts import render
from django.http import *
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january":"Meat",
    "february":"Donut",
    "march":"Candy",
    "may":"Fruits",
    "june":"Donut",
    "july":"Name",
    "august":"Agustus",
    "september":"None"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request,"challanges/index.html",{
        "months":months
    })

def monthly_challange_by_number(request,month):
    months = list(monthly_challenges.keys())
 

    if month  > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challange", args=[redirect_month]) # /challange/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challanges/challange.html",{
            "text":challenge_text,
            "month_name":month.capitalize()
        });
        # response_data = render_to_string("challanges/challange.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
   
    
 