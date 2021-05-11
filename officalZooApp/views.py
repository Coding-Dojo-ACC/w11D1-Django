from django.shortcuts import render, redirect
from .models import *

def officialZoo(request):
    return render(request, 'officialZoo.html')

def allZoos(request):
    context = {
        'allZoos': Zoo.objects.all().values()
    }
    return render(request, 'allZoos.html', context)

def createZoo(request):
    if request.method == "GET":
        return redirect('/zoo/createZoo/')
    Zoo.objects.create(
        zooName=request.POST['zooName'],
        zooLocation=request.POST['zooLocation']
    )
    return redirect('/zoo/theZoos/')

def editZoo(request, zoo_id):
    oneZoo = Zoo.objects.get(id='zoo_id')
    context = {
        'editZoo': oneZoo
    }
    return render(request, 'editZoo.html', context)

def updateZoo(request, zoo_id):
    toUpdate = Zoo.objects.get(id=zoo_id)
    toUpdate.zooName = request.POST['zooName']
    toUpdate.zooLocation = request.POST['zooLocation']
    toUpdate.save()

    return redirect('/zoo/theZoos/')

def deleteZoo(request, zoo_id):
    toDelete = Zoo.objects.get(id=zoo_id)
    toDelete.delete()

    return redirect('/zoo/theZoos/')