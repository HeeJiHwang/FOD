
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpRequest
from inquiry.models import Reservation, FlightSchedule, Member, Route, Airports, PassengerInfo, PassengerForm, AircraftType,Transaction


# 로그인된 id에 대한 예약 조회함수
def inquiry(request:HttpRequest):

    id = request.session.get('login')
  
    #print(id)
    
    msg = None  #오류방지 초기값
    login = None
    no = None
    su = None
    url = None
    check = True
    

    try:
        user = Member.objects.get(id=id)
    except Member.DoesNotExist:
        user = None




    # 로그인하고 하라고
    if id == None:
        msg = '로그인이 필요한 기능입니다.'
        url = '/login/loginForm/'
    else:
        url = '/inquiry/'
        login = Member.objects.get(id = id) # 로그인한 사람의 정보
        no = Reservation.objects.filter(m_no=login)  # id.예매      #예매번호를 쓰므로 여러값이 도출될 수 있음
        su = len(no)        # 로그인한 사람의 예매내역 개수
        check = False
  
        
    
    
    context = {
        'id' : id,
        'no' : no,
        'login' : login,
        'su' : su,
        'msg' : msg,
        'url' : url,
        "check" :  check,
        'user' : user,
    }
    
    
    return render(request,'inquiry/inquiry.html',context)





def inquiry_detail(request:HttpRequest):

    # 내가 선택한 예약 번호 가져오기
    try:
        idx = request.GET.get('re_idx')    # 로그인세션의 예매idx를 reservation으로 받아옴  #값은 하나뿐!
    except Exception as e:
        idx = ""
        print("idx 데이터를 불러오는데 실패")

    try:
        reservation = Reservation.objects.get(idx=idx)
    except Exception as e:
        reservation = ""
        print(" Reservation 데이터를 불러오는데 실패")
    
    try:
        passenger = PassengerForm.objects.get(re_idx=idx)
    except Exception as e:
        passenger = ""
        print(" Passenger 데이터를 불러오는데 실패")
    
    try:
        reservation = Reservation.objects.get(idx=idx)
    except Exception as e:
        reservation = ""
        print(" Reservation 데이터를 불러오는데 실패")

    id = request.session['login']
    login = Member.objects.get(id = id)


    print(idx)
    
    context = {
        'idx' : idx,
        'reservation' : reservation,
        'passenger' : passenger,
        'login' : login,
    }
    return render(request, 'inquiry/inquiry_detail.html', context)


# 은수가 추가!!(예약 취소 함수)
def reser_cancel(request:HttpRequest):

    user_id = request.session['login']

    # 가져온 idx
    get_idx = int(request.GET.get('idx'))

    if user_id != None:
        user_no = Member.objects.filter(id = user_id).values('no')[0]['no']

        # 예매 번호 가져오기
        re_no = Reservation.objects.filter(idx = get_idx, m_no = user_no).values_list('re_no', flat=True)
        re_re_no_list = list(re_no)

        # 결제 번호 가져오기
        t_no = Reservation.objects.filter(idx = get_idx, m_no = user_no).values_list('t_no', flat=True)
        re_t_no_list = list(t_no)

        print('예매번호list: ', re_re_no_list)
        print('결제번호list: ', re_t_no_list)

        # 카드번호와 통장번호 가져오기
        card_number_val = Transaction.objects.filter(no = re_t_no_list[0]).values('card_number')[0]['card_number']
        account_number_val = Transaction.objects.filter(no = re_t_no_list[0]).values('account_number')[0]['account_number']

        print("card 번호 : ", card_number_val)
        print("card 타입 : ", type(card_number_val))
        print("통장 번호 : ", account_number_val)


        try:

            # 마일리지 예매시 차감했던 포인트 돌려준다
            if card_number_val == None and account_number_val == None:
                print("마일리지 예매를 하셨군요")

                # 운임마일리지 가져오기
                mileage = Reservation.objects.filter(idx = get_idx, m_no = user_no)[0].f_no.route_no.mileage
                print('차감했던 mileage : ', mileage)

                # Member의 포인트
                m_points = Member.objects.filter(id = user_id).values('p_points')[0]['p_points']
                print('멤버의 포인트', m_points)

                # 차감했전 포인트 돌려주기
                Member.objects.filter(id = user_id).update(p_points = m_points + mileage)

            
            # 예약번호와 항공스케줄 번호 비교해서 삭제
            Reservation.objects.filter(idx = get_idx).delete()

        except Exception as e:
            print("삭제할 예약번호가 없습니다.")



    return redirect('/inquiry/')





