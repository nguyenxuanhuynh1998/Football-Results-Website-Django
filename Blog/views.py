from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
# Create your views here.

def index(request):
    today= datetime.today().strftime('%Y-%m-%d')
    url = "https://apiv3.apifootball.com/?action=get_events&match_live=1&league_id=149&from="+today+"&to="+today+"&APIkey=ddbb2c27630cc43e00807b8e444fe8b1bb36096407c7fdfe9fd96981a9148461"
    #url = "https://apiv3.apifootball.com/?action=get_events&league_id=149&from=2022-11-12&to=2022-11-12&APIkey=ddbb2c27630cc43e00807b8e444fe8b1bb36096407c7fdfe9fd96981a9148461 "
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request,'blog/index.html',{'jsonResponse':jsonResponse})

def specific(request):
    return HttpResponse("XIN CHAO") 

  