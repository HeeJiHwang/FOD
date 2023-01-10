from django.shortcuts import render,redirect
from join.models import Member

# Create your views here.
from datetime import datetime


def joinForm(request):

    now = datetime.now().date()
    # print(now)
    listt = list(Member.objects.all().values_list('id', flat=True))
    context={
        'now' : now,
        'list':listt
    }
    return render(request,'join/joinForm.html',context)

def checkJoin(request):
    # 회원번호 만들기
    li = Member.objects.all()
    num =len(li)+1
    member_no = '{:0>4}'.format(num)
    
    last_name = request.POST.get("last_name")
    first_name = request.POST.get("first_name")
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    gender = request.POST.get("gender")
    birth_date = request.POST.get("birth_date")
    phone = request.POST.get("phone")
    security1 = request.POST.get("security1")
    security2 = request.POST.get("security2")
    sms = request.POST.get("sms")
    country_code = request.POST.get("country_code")
    check_foreign = request.POST.get("check_foreign")
    passport = request.POST.get("passport")

    print(birth_date)
    try:
        Member.objects.create(no=member_no,last_name=last_name,first_name=first_name,id=id, pw=pw, gender=gender, birth_date=birth_date,
          phone=phone,security1=security1, security2=security2, sms=sms, country_code=country_code, check_foreign=check_foreign, passport=passport, p_points=0 )
    except Exception as e:
        print(e)
        return redirect('/join/joinForm/')
    
    return redirect('/login/loginForm/')



