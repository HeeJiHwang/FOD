from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

from login.models import Member,Admin

# Create your views here.
def loginForm(request:HttpRequest):
    id = request.GET.get("id") # ''
    check = False
    if id == '' or id == None:
        id = request.COOKIES.get("ckid")
        if id != None:
            check = True

    context = {
        'id' : id,
        "check" : check,
    }

    return render(request,'login/form.html',context);


def checkLogin(request:HttpRequest):
    id = request.POST.get("id")
    password = request.POST.get("password")
    print(id)
    print(password)

    msg = None
    check = False
    

    try:
        member = Member.objects.get(id=id,pw=password) # and
        print(member)
        #print(member.query) # 지금 작성한 쿼리문 반환...
    except Exception as e:
        msg = "아이디 혹은 비밀번호가 잘못되었습니다."
        url = '/login/loginForm/'
    else:
        check = True
        msg = member.first_name + "님이 로그인하셨습니다."

        #로그인 처리
        request.session['login'] = member.id
        url = '/'

    context = { 'msg' : msg , 'check' : check, 'url' : url}
    
    # response = render(request,'login/result.html',context)
    response = render(request,'login/result.html',context)

    if check:
        ckid = request.POST.get("ckid") #파라미터의 ckid

        ck = request.COOKIES.get('ckid') # 쿠키파일중에 파일명이 ckid 찾기

        
        if ckid != None: #아이디 기억하기 체크된 상태
            if ck == None:
                #쿠키파일 생성...
                response.set_cookie("ckid",id,max_age=60*60*10) #생성
                # ckid라는 파일명으로 로그인한 아이디를 컨텐츠에 넣고 유지시간 10시간으로 쿠키파일 설정.
            elif ck != id: #쿠키파일의 아이디와 로그인된 아이디가 다른경우
                response.set_cookie("ckid",id,max_age=60*60*10) # 만들어진 상황이면 쿠키파일 변경
        else: # 아이디 기억하기 체크 해제된 상태
            if ck == id: # 쿠키파일의 아이디와 로그인된 아이디가 같은경우
                response.delete_cookie("ckid") # 쿠키파일 삭제

    

    return response



        #response = HttpResponse()-굳이 할 필요가 없다 render 안에 자동으로 들어가 있기 때문이다
        # if ckid != '': #아이디 기억하기 체크된 상태
        #     if ck == None:
        #         #쿠키파일 생성...
        #         response = render(request,'login/result.html')
        #         response.set_cookie("ckid",id,max_age=60*60*10)
        #         # ckid라는 파일명으로 로그인한 아이디를 컨텐츠에 넣고 2년이라는 시간으로 쿠키파일 설정.
        #         return response
        #     elif ck != id:
        #         response = render(request,'login/result.html')
        #         response.set_cookie("ckid",id,max_age=60*60*10)#쿠키파일 변경이 되어버리는 것
        #         # ckid라는 파일명으로 로그인한 아이디를 컨텐츠에 넣고 2년이라는 시간으로 쿠키파일 설정.
        #         return response
        # else:
        #     if ck == id:
        #         response = render(request,'login/result.html')
        #         response.delete_cookie("ckid") 
        #         # ckid라는 파일명으로 로그인한 아이디를 컨텐츠에 넣고 2년이라는 시간으로 쿠키파일 설정.
        #         return response

   
    


def logout(request:HttpRequest):
    try:        
        request.session.pop('admin') # 세션에 저장된 하나의 키와 밸류 삭제.
        return render(request, 'admin_manage/admin_result.html')
    except Exception as e:
        request.session.pop('login') # 세션에 저장된 하나의 키와 밸류 삭제.
        return redirect('/')
    # request.session.flush() # 세션의 저장된 정보 초기화
    


def admin_loginForm(request):
    id = request.GET.get("id") # ''
    check = False
    if id == '' or id == None:
        id = request.COOKIES.get("ckid")
        if id != None:
            check = True

    context = {
        'id' : id,
        "check" : check,
    }

    return render(request,'login/admin_loginForm.html',context)

def admin_checkLogin(request):
    id = request.POST.get("id")
    password = request.POST.get("password")
    print(id)
    print(password)
    

    msg = None
    check = False
    

    try:
        admin = Admin.objects.get(id=id,pw=password) # and
        print(admin)
    except Exception as e:
        msg = "아이디 혹은 비밀번호가 잘못되었습니다."
        return redirect('/login/loginForm/')
    else:
        check = True
        msg = admin.name + "님이 로그인하셨습니다."

        #로그인 처리
        request.session['admin'] = admin.d_no.no
        print(admin.d_no.no)

    context = { 'msg' : msg , 'check' : check}
    
    response = render(request,'admin_manage/admin_result.html',context)

    if check:
        amdin = request.POST.get("amdin") #파라미터의 ckid

        ck = request.COOKIES.get('amdin') # 쿠키파일중에 파일명이 ckid 찾기

        
        if amdin != None: #아이디 기억하기 체크된 상태
            if ck == None:
                #쿠키파일 생성...
                response.set_cookie("amdin",id,max_age=60*60*10) #생성
                # ckid라는 파일명으로 로그인한 아이디를 컨텐츠에 넣고 유지시간 10시간으로 쿠키파일 설정.
            elif ck != id: #쿠키파일의 아이디와 로그인된 아이디가 다른경우
                response.set_cookie("amdin",id,max_age=60*60*10) # 만들어진 상황이면 쿠키파일 변경
        else: # 아이디 기억하기 체크 해제된 상태
            if ck == id: # 쿠키파일의 아이디와 로그인된 아이디가 같은경우
                response.delete_cookie("amdin") # 쿠키파일 삭제

    

    return response


def my(request:HttpRequest):

    id = request.session['login']
    member = Member.objects.get(id=id)

    context = {
        'member' : member
    }

    return render(request, 'login/my.html',context)

def mymileges(request:HttpRequest):

    id = request.session['login']
    member = Member.objects.get(id=id)
    p=member.p_points
    s = 5000-p

    context = {
        'member' : member,
        's' : s,
        'p':p
    }

    return render(request, 'login/mymileges.html',context)


# 회원탈퇴 함수(은수가 추가)
def memberOut(request:HttpRequest):

    user_id = request.session['login']
    print(user_id)

    try:
        if user_id != None:
            Member.objects.filter(id = user_id).delete()
            msg = "안녕히가세요"
            print("회원탈퇴 성공")

            request.session.pop('login') # 세션에 저장된 하나의 키와 밸류 삭제.
            return redirect('/')

    except Exception as e:
        msg = "회원을 지우는데 실패했습니다."
        print("회원탈퇴 실패")
        request.session.pop('login') # 세션에 저장된 하나의 키와 밸류 삭제.
        return render(request, '/login/form.html')