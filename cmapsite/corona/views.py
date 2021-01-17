from django.shortcuts import render
from django.http import HttpResponse
from corona.DB_Crawling import route_table

# Create your views here.
def index(request):
    context={

    }
    return render(request, 'corona/index.html', context=context)

def chart(request):
    context={

    }
    return render(request, 'corona/chart.html', context=context)


def route_table(request):
    route_Table = route_table()
    return render(request, 'corona/chart.html', route_Table)
