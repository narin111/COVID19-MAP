from django.shortcuts import render
from DB_Crawling import route_table

# Create your views here.

def route_table(request):
    routTable = route_table()
    return render(request, 'cTable/cTable.html', rout_table)