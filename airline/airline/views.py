
from django.http import HttpRequest
from django.shortcuts import render,redirect
from .models import Airports

def index(request:HttpRequest):

    session = request.session.get('admin')
    print(session)
    if session != None:
        return render(request, 'admin_manage/admin_result.html')
    else:
        user_id = request.session.get('login')
        if user_id ==None:
            user_id = ""

        airport = Airports.objects.all()
        
        context = {
            'airport' : airport,
            'user_id' : user_id
        }
    



    # session = request.session.get('admin')  # 관리자가 로그인 했는지 체크
    # user_id = request.session.get('login')  # 회원이 로그인 했는지 체크

    # airport = Airports.objects.all()

    # print(session)
    # if session != None:
    #     return render(request, 'admin_manage/admin_result.html')
    # else:
    #     context = {
    #         'airport' : airport
    #     }

    # if user_id == None:
    #     user_id = ""
    # else:
    #     context = {
    #         'airport' : airport,
    #         'user_id' : user_id
    #     }


        return render(request, 'airline/index.html', context)

def airplane(request:HttpRequest):

    return render(request, 'airline/airplane.html')

def baggage(request:HttpRequest):

    return render(request, 'airline/baggage.html')

def restricteditems(request:HttpRequest):

    return render(request, 'airline/restricteditems.html')

def carryon(request:HttpRequest):

    return render(request, 'airline/carryon.html')


def damagedorlost(request:HttpRequest):

    return render(request, 'airline/damagedorlost.html')

def checkno(request:HttpRequest):

    return render(request, 'airline/checkno.html')

def no(request:HttpRequest):

    return render(request, 'airline/no.html')

def lost(request:HttpRequest):

    return render(request, 'airline/lost.html')

def broke(request:HttpRequest):

    return render(request, 'airline/broke.html')

def aircraft737(request:HttpRequest):

    return render(request, 'airline/aircraft737.html')

def aircraft747(request:HttpRequest):

    return render(request, 'airline/aircraft747.html')

def aircraft777(request:HttpRequest):

    return render(request, 'airline/aircraft777.html')



