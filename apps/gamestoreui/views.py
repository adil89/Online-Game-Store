from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from apps.gamestore.models import Users
from apps.gamestore.models import Game
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Register_Users(request):
        return render(request, "gamestoreui/registerusers.html")

@csrf_exempt
def CreateUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        userName = request.POST.get('userName')
        password = request.POST.get('password')

        Users.objects.create(
            name = name,
            userName = userName,
            password = password,
            type = 1,
         )

        return HttpResponse("created")

def Login(request):
    return render(request, "gamestoreui/Login.html")

@csrf_exempt
def Register_Developer(request):
    return render(request, "gamestoreui/registerDeveloper.html")

@csrf_exempt
def CreateDeveloper(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        userName = request.POST.get('userName')
        password = request.POST.get('password')

        developer = Users(name= name,userName= userName,password= password,type=0);
        developer.save();

        return HttpResponse("created")

def GameStore(request):
      user = request.session['user']
      return render(request, "gamestoreui/gameStore.html",{"user" : user})

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        type = request.POST.get('type')

        count = Users.objects.values_list('userName').filter(userName = userName,type = type).count();
        if count > 0:
            pass1 = Users.objects.values_list('password').get(userName = userName);
            pass2 = pass1[0];
            if password == pass2:
                 if type == str(1):
                    request.session['user'] = 'true';
                    return HttpResponse(1)
                 else:
                    request.session['user'] = 'false';
                    return HttpResponse(1)
            else:
                return HttpResponse(0)
        else:
            return HttpResponse(0)

@csrf_exempt
def LoadGames(request):
    if request.method == 'GET':
        games = Game.objects.all();
        json = serializers.serialize('json', games);
        return HttpResponse(json,content_type='application/json')

@csrf_exempt
def SaveGame(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        gameURL = request.POST.get('gameURL')
        g = Game(name= name,price= price,gameURL= gameURL );
        g.save();
        return HttpResponse("saved");

@csrf_exempt
def SaveGameEdit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        game = Game.objects.get(pk=id)
        game.name = name;
        game.save();
        return HttpResponse("Edited");

@csrf_exempt
def DeleteGame(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        game = Game.objects.get(pk=id)
        game.delete();

        return HttpResponse("Deleated");


