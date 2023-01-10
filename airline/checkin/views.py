from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from checkin.models import Reservation, FlightSchedule, Member, PassengerForm




def checkin_before(request:HttpRequest):

    id = request.session.get('login')

    msg = None 
    url = None
    login = None
    no = None
    su = None
    check = True
    

    # 로그인한 사람만 페이지 볼수 있게하는 함수
    if id == None:
        msg = '로그인이 필요한 기능입니다.'
        url = '/login/loginForm/'
    else:
        login = Member.objects.get(id = id)
        no = Reservation.objects.filter(m_no=login)
        su = len(no)
        check = False


    context = {
        'id' : id,
        'no' : no,
        'login' : login,
        'su' : su,
        'msg' : msg,
        'url' : url,
        'check' : check,
    }
    return render(request, 'checkin/checkin_before.html', context)








def checkin(request:HttpRequest):
    
    try:
        idx = request.GET.get('re_idx')   # reservation - idx
        reservation = Reservation.objects.get(idx=idx)
        f_no = Reservation.objects.filter(idx=idx).values('f_no')
    except Exception as e:
        idx = ""
        reservation = ""
        print("idx 불러오지 못함") 


    print('idx: ', idx)

    try:
        passenger = PassengerForm.objects.get(re_idx=idx)
    except Exception as e:
        passenger = ""   
        print("PassengerForm 데이터를 불러오지 못함")
    
    print('passenger: ', passenger)
    print('passenger seat: ', passenger.seat)

    passenger_seat = passenger.seat

    dep_time = FlightSchedule.objects.filter(no__in=f_no).values('departure_time') # 출발 시간
    dep_date = FlightSchedule.objects.filter(no__in=f_no).values('departure_date') # 출발 날짜   
    checkin_yn = True
    msg = ''
    url = ''
    check = False


# 출발날짜 + 출발시간 더하는 함수
    departure = datetime.combine(dep_date[0].get('departure_date'),dep_time[0].get('departure_time'))
    now = datetime.now()
    diff = departure - now
    diff_day = diff.days * 24


# 출발일로부터 1일전까지만 체크인이 가능하게 하는 함수
# 원래는 24이나 다 보이게 하기위해 1024로 설정! 나중에 수정
    if (diff_day + diff.seconds/3600) <= 24:  
        checkin_yn = True
    else:
        checkin_yn = False
   
    

    #체크인 전에 좌석값이 지정되지않았을경우(None) 좌석지정페이지로 강제이동
    if PassengerForm.objects.get(re_idx=idx).seat == None:
        msg = "체크인전에 좌석지정은 필수^^"
        url = '/seats/seat/'


    print(PassengerForm.objects.get(re_idx=idx).seat)
   
    context = {
        'idx' : idx,
        'reservation' : reservation,
        'passenger' : passenger,
        'checkin_yn' : checkin_yn,
        'msg' : msg,
        'url' : url,
        'seat' : passenger_seat
    }

    return render(request, 'checkin/checkin.html' , context)









def checkin_suc(request:HttpRequest):
    
    idx = request.GET.get('re_idx')

    checkin = PassengerForm.objects.filter(re_idx=idx).values('check_in')
    end_checkin = 1
      
    
    try:
        PassengerForm.objects.filter(re_idx=idx).update(check_in = end_checkin)
        msg = "체크인이 완료되었습니다"
        url = '/'
    except:
        msg = "오류가 발생했습니다 다시 시도해주십시오."
        url = '/checkin/'
    
    
    context = {
        'idx' : idx,
        'msg' : msg,
        'url' : url,
    }
    
    
    return render(request, 'checkin/checkin_suc.html', context)







def boardingpass(request:HttpRequest):
    
    id = request.session['login']
    member = Member.objects.get(id = id)
    idx = request.GET.get('re_idx')
    reservation = Reservation.objects.get(idx=idx)
    passenger = PassengerForm.objects.get(re_idx=idx)

    print(idx)

    context = {
        'idx' : idx,
        'reservation' : reservation,
        'passenger' : passenger,
        'member' : member,
    }


    return render(request, 'checkin/boardingpass.html', context)


