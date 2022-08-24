import hmac
from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    #data = requests.get("http://127.0.0.1:5000/employee").json()
    data = requests.get("http://34.170.55.94/employee").json()
    data = data.get("Employees")
    return render(request, 'home.html',{"data":data})

def add(request):
    return render(request,"add.html")

def postadd(request):

    eid = request.POST.get("eid")
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    technolgy = request.POST.get("technology")

    data = {
            "Emp_Id": int(eid),
            "Name": name,
            "Technology": technolgy,
            "Gender": gender
        }

    mes = requests.post("http://34.170.55.94/create", json = data)

    return home(request)


def delete(request):

    eid = request.GET.get("w")
    mes = requests.delete("http://34.170.55.94/delete/"+eid)
    return home(request)


def update(request):
    eid = request.GET.get("w")
    return render(request, "update.html",{"eid":eid})


def postupdate(request):

    eid = request.POST.get("eid")
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    technolgy = request.POST.get("technology")

    data = {
            "Name": name,
            "Technology": technolgy,
            "Gender": gender
        }

    mes = requests.put(("http://34.170.55.94/update/"+eid),json=data)
    return home(request)
