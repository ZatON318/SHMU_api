from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse

from bs4 import BeautifulSoup
from lxml import html
import requests

stationsList = []
class Station:
    def __init__(self, name, temp, wdir, wspeed, wgusts, preasure):
        self.name = name
        self.temp = temp
        self.wdir = wdir
        self.wspeed = wspeed
        self.wgusts = wgusts
        self.preasure = preasure

def getData():
    webpage = requests.get("https://www.shmu.sk/sk/?page=59")
    t = html.fromstring(webpage.content)

    u = 12
    #for i in t.xpath('//tbody/tr//text()'):
    print(t.xpath("//tbody/tr/td//text()"))
    
    weatherData = t.xpath("//tbody/tr/td//text()")
    for s in weatherData:
        if s.isalpha():
            print(s)
    
        #print(u)

    """for y in range(0, 86):
        print("\n\n")
        print("name: " + t.xpath('//td//text()')[u])
        u += 1
        print("temp: " + t.xpath('//td//text()')[u])
        u += 1
        print("wdir: " + t.xpath('//td//text()')[u])
        u += 1
        print("wspeed: " + t.xpath('//td//text()')[u])
        u += 1
        print("wgusts: " + t.xpath('//td//text()')[u])
        u += 1
        print("preasure: " + t.xpath('//td//text()')[u])
        u += 1
        
        #for x in range(0, 7):
            #print(t.xpath('//td//text()')[u])
            #u += 1"""
    

def index(response):
    getData()
    return JsonResponse({'foo':"123"})

