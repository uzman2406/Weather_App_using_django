from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
from django.contrib import messages



def home(request):
    d={}
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='indore'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a9e30a4d7248f6f8d1096ca156f6dbac"
    PARAMS= {'units': 'metric'}

    API_KEY = "AIzaSyAklVpLbEBVTvvVH8XuYR_IX7J0oEWOVjg"
    SEARCH_ENGINE_ID = "52e71fe977aa8461f"
    
    
    
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    
    if search_items and len(search_items) > 0:
        image_url = search_items[0]['link']
    else:
        image_url = "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1920&q=80"

    


    try:
        data=requests.get(url,PARAMS).json()
        description=data['weather'][0]['description']
        temp=data['main']['temp']
        city=data['name']
        icon=data['weather'][0]['icon']
        day=datetime.datetime.now().strftime("%B %d, %Y")
        d={
            'description': description,
            'temp': temp,
            'city': city,
            'icon': icon,
            'day': day,
            "image_url": image_url,
            'exception_occurred': False
        }
        return render(request,"templates/index.html",d)
    except:
        exception_occurred=True
        messages.error(request,"Error fetching weather data")
        day=datetime.date.today()
        d={
            'description': "NOT AVAILABLE",
            'temp': "NOT AVAILABLE",
            'city': "NOT AVAILABLE",
            'icon': "NOT AVAILABLE",
            'day': day,
            "image_url": image_url,
            'exception_occurred': True
        }
        
        return render(request,"templates/index.html",d)
        

   