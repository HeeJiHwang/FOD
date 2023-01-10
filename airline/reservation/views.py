from django.shortcuts import render, redirect
from django.http import HttpRequest
from reservation.models import Airports, FlightSchedule, Route, Member, PassengerInfo, PassengerForm , Transaction,Reservation
from datetime import date
import random



from django.db.models import Sum, Avg

# 빠른 예매쪽에서 reservation으로 보내는 함수
def reservation(request):

    try:
        airport = Airports.objects.all()
    except Exception as e:
        airport = ""

    user_id = request.session.get('login')  # 로그인 했는지 체크
    if(user_id == None):
        user_id = ""

    context = {
        'airport' : airport,
        'user_id' : user_id
    }
    
    return render(request, 'reservation/reservation.html', context)


# 가는 항공스케쥴 뽑는 함수
def selectflight(request:HttpRequest):
    # 필요한 데이터 가져오기(index.html)에서
    re_type = request.POST.get('re_type')    # 예매 or 마일리지예매
    way_type = request.POST.get('way_type')  # 왕복 or 편도

    print('re_type: ', re_type)
    print('way_type: ', way_type)

    depart = request.POST.get('depart')      # 출발지
    arri = request.POST.get('arri')          # 도착지

    goDate = request.POST.get('goDate')      # 출발일
    comeDate = request.POST.get('comeDate')  # 도착일

    # 마일리지 예매를 위해 회원정보를 가져온다
    if re_type == "마일리지예매":
        user_id = request.session.get('login')  # 사용자의 session
        # 마일리지 예매 선택시 회원의 마일리지 정보 가져오기
        try:
            m_point = Member.objects.filter(id = user_id).values('p_points')[0]['p_points']
        except Exception as e:
            m_point = ""

    else:   # 단순 예매이면 point는 필요없다
        m_point = ""

    
    print("회원의 포인트 : " , type(m_point))


    # 항공 코드 가져온다
    try:
        depart_code = Airports.objects.get(name=depart)
        arri_code = Airports.objects.get(name=arri)
    except Exception as e:
        depart_code = ""
        arri_code = ""
        print("항공 정보를 가져오는데 실패")

    # Airport 테이블에서 출발지와 도착지가 같은 no를 뽑는다
    try:
        a = Airports.objects.filter(name=depart).values('no')[0]['no']
        b = Airports.objects.filter(name=arri).values('no')[0]['no']
    except Exception as e:
        a = ""
        b = ""
        print("항공 no를 가져오는데 실패")

        
    # Route 테이블에서 경로 no를 가져온다
    try:
        route_no= Route.objects.filter(departure=a).filter(arrival=b).values('no')[0]['no']
    except Exception as e:
        route_no = ""
        print("경로 no를 가져오는데 실패했습니다.")


    # 항공스케줄을 가져온다
    try:
        schedule = FlightSchedule.objects.filter(departure_date=goDate).filter(route_no =route_no)
        # print('💛💛💛💛💛💛 schedule', schedule)
        # print('schedule[0].route_no', schedule[0].route_no)

        # print('gmlwlwllwlwwwwwwwwww   : ', FlightSchedule.objects.values('route_no'))
        # print('gmlwlwllwlwwwwwwwwww   : ', FlightSchedule.objects.values('route_no').annotate(Avg('remain_seats')))
        # print('gmlwlwllwlwwwwwwwwww   : ', FlightSchedule.objects.values('route_no').annotate(avv = Avg('remain_seats')).values('avv'))
 





    except Exception as e:
        schedule = ""
        print("항공스케줄을 가져오는데 실패했습니다.")

    print('마일리지예매:', re_type)
    context = {
        're_type' : re_type,
        'way_type' : way_type,
        'depart' : depart,
        'arri' : arri,
        'goDate' : goDate,
        'comeDate' : comeDate,
        'depart_code' : depart_code,
        'arri_code' : arri_code,
        'schedule': schedule,
        'm_point' : m_point
    }
    return render(request, 'reservation/selectflight.html', context)


# 편도 선택시 항공스케쥴 가져오는 함수
def ow_selectflight(request:HttpRequest):
    # 필요한 데이터 가져오기(index.html)에서
    re_type = request.POST.get('re_type')    # 예매 or 마일리지 예매
    way_type = request.POST.get('way_type')  # 왕복 or 편도

    depart = request.POST.get('depart')      # 출발지
    arri = request.POST.get('arri')          # 도착지

    goDate = request.POST.get('goDate')      # 출발일
    comeDate = request.POST.get('comeDate')  # 도착일


    print(way_type)
    print(comeDate)

    # 마일리지 예매를 위해 회원정보를 가져온다
    if re_type == "마일리지예매":
        user_id = request.session.get('login')  # 사용자의 session
        # 마일리지 예매 선택시 회원의 마일리지 정보 가져오기
        try:
            m_point = Member.objects.filter(id = user_id).values('p_points')[0]['p_points']
        except Exception as e:
            m_point = ""

    else:   # 단순 예매이면 point는 필요없다
        m_point = ""

    
    print("회원의 포인트 : " , m_point)


    # 항공 코드 가져온다
    try:
        depart_code = Airports.objects.get(name=depart)
        arri_code = Airports.objects.get(name=arri)
    except Exception as e:
        depart_code = ""
        arri_code = ""
        print(e + "\n항공 코드를 못 가져왔습니다." )

    # Airport 테이블에서 출발지와 도착지 no를 뽑는다
    try:
        a = Airports.objects.filter(name=depart).values('no')[0]['no']
        b = Airports.objects.filter(name=arri).values('no')[0]['no']
    except Exception as e:
        a = ""
        b = ""
        print("출발지와 도착지의 no를 뽑지 못 했습니다.")

    print(Route.objects.filter(departure=a).filter(arrival=b).values('no'))

    # 경로를 가져온다
    try:
        c= Route.objects.filter(departure=a).filter(arrival=b).values('no')[0]['no']
        schedule = FlightSchedule.objects.filter(departure_date=goDate).filter(route_no =c)
    except:
        c = ""
        schedule = ""
        print("경로를 가져오는데 실패했습니다.")


    context = {
        're_type' : re_type,
        'way_type' : way_type,
        'depart' : depart,
        'arri' : arri,
        'goDate' : goDate,
        'comeDate' : comeDate,
        'depart_code' : depart_code,
        'arri_code' : arri_code,
        'schedule': schedule,
        'm_point' : m_point
    }
    return render(request, 'reservation/ow_selectflight.html', context)





# 항공스케쥴 뽑는 함수(오는날)
def selectflight2(request:HttpRequest):
    # 예매 or 마일리지 예매
    re_type = request.POST.get('re_type')

    # 왕복 편도 선택
    way_type = request.POST.get('way_type')

    print(way_type)

    # 마일리지 예매를 위해 회원정보를 가져온다
    if re_type == "마일리지예매":
        user_id = request.session.get('login')  # 사용자의 session
        # 마일리지 예매 선택시 회원의 마일리지 정보 가져오기
        try:
            m_point = Member.objects.filter(id = user_id).values('p_points')[0]['p_points']
        except Exception as e:
            m_point = ""
            
    else:   # 단순 예매이면 point는 필요없다
        m_point = ""

    # 출발지 도착지 서로 바꾸기 
    depart_no = request.POST.get('arri_no')
    arri_no = request.POST.get('depart_no')

    # 공항의 no, name 가져오기
    try:
        depart = Airports.objects.get(no = depart_no)  # name, code뽑기
        arri = Airports.objects.get(no = arri_no)  # name, code뽑기
    except Exception as e:
        depart = ""
        arri = ""
        print("공항 id를 가져오는데 실패했습니다.")

    goDate = request.POST.get('goDate')  #가는 날
    comeDate = request.POST.get('comeDate')  # 도착일
    
    
    # 가는 스케쥴에 대해서
    go_no = request.POST.get('no') # 가는 날 항공 스케쥴 id
    go_money = request.POST.get('money')
    go_type = request.POST.get('type')
    print(go_no)

    print("오는 날 " + comeDate)


    # 오는 스케쥴 뽑기
    try:
        c = Route.objects.filter(departure=depart_no).filter(arrival=arri_no).values('no')[0]['no']
        schedule = FlightSchedule.objects.filter(departure_date=comeDate).filter(route_no =c)
    except Exception as e:
        c = ""
        schedule = ""
        print('오는 스케줄을 뽑는데 실패했습니다.')
    print("--------------------")
    print(re_type)
    context = {
        're_type' : re_type,
        'way_type' : way_type,
        'depart' : depart,
        'arri' : arri ,
        'goDate' : goDate,
        'comeDate' : comeDate,
        'schedule' : schedule,
        'go_no' :go_no,
        'go_type':go_type,
        'go_money':go_money,
        'depart_no':depart_no,
        'arri_no':arri_no,
        }

    return render(request,'reservation/selectflight2.html', context)



def transaction(request):
    # 예매 or 마일리지예매 선택
    re_type = request.POST.get('re_type')
    # 왕복 편도 선택
    way_type = request.POST.get('way_type')

    user_id = request.session['login']

    try:
        if user_id == None:
            return HttpRequest(request, '/login/loginForm/')
        else:
            member= Member.objects.get(id = user_id)  # 레코드 한줄
    except Exception as e:
        member = ""
        print('회원 정보를 가져오는데 실패했습니다.')

    # 가는 스케쥴 받아오기
    go_no = request.POST.get('go_no') 
    print('go_no: ',go_no )
    go_type = request.POST.get('go_type') 
    go_money = request.POST.get('go_money') 


    # 오는 스케쥴에 대해서
    come_no = request.POST.get('no') # 오는 날 항공 스케쥴 id
    print(come_no)
    come_money = request.POST.get('money')
    come_type = request.POST.get('type')

    print(come_no)

    # 가는 스케쥴 레코드
    try:
        go_schedule = FlightSchedule.objects.get(no=go_no)
    except Exception as e:
        print(e)
        go_schedule = ""
        print('가는 스케줄을 뽑는데 실패했습니다.')

    # 오는 스케쥴 레코드
    try:
        come_schedule = FlightSchedule.objects.get(no = come_no)
    except Exception as e:
        print(e)
        come_money = ""
        print('오는 스케줄을 뽑는데 실패했습니다.')

    context = {
        're_type' : re_type,
        'way_type' : way_type,
        'go_type' : go_type,
        'go_money': go_money,
        'come_type': come_type,
        'come_money': come_money,
        'go_schedule' : go_schedule,
        'come_schedule': come_schedule,
        'member' : member,
        'go_no':go_no,
        'come_no':come_no,
    }

    return render(request,'reservation/transaction.html' , context)


# 편도에 대한 transaction
def ow_transaction(request):
    # 예매 or 마일리지예매 선택
    re_type = request.POST.get('re_type')
    # 왕복 편도 선택
    way_type = request.POST.get('way_type') # '편도'

    user_id = request.session['login']

    try:
        if user_id == None:
            return HttpRequest(request, '/login/loginForm/')
        else:
            member= Member.objects.get(id = user_id)  # 레코드 한줄
    except Exception as e:
        print(e)
        member = ""
        print('회원 정보를 가져오는데 실패했습니다.')


    # 가는 스케쥴 받아오기
    go_no = request.POST.get('no') 
    print('go_no1: ',go_no )
    go_type = request.POST.get('type') 
    go_money = request.POST.get('money') 
    print('go_money1: ', go_money)

    # 가는 스케쥴 레코드 한 줄
    try:
        go_schedule = FlightSchedule.objects.get(no = go_no)
    except Exception as e:
        go_schedule = ""
        print('가는 스케줄을 뽑는데 실패했습니다.')


    context = {
        're_type' : re_type,
        'way_type' : way_type,
        'go_type' : go_type,
        'go_money': go_money,
        'go_schedule' : go_schedule,
        'member' : member,
        'go_schedule_id': go_no,
    }

    return render(request,'reservation/ow_transaction.html' , context)




# 받은 탑승객 정보를 토대로 PassangerInfo에 등록 함수 + 결제(왕복)
def paymentpage(request:HttpRequest):
    # 예매 or 마일리지예매 선택
    re_type = request.POST.get('re_type')
    # 왕복 편도 선택
    way_type = request.POST.get('way_type')

    # 탑승객 정보 가져오기
    info_collect = request.POST.get('info_collect')
    rule_agree = request.POST.get('rule_agree')
    danger_agree = request.POST.get('danger_agree')
    member_no = request.POST.get('member_no')    # 스카이패스 번호
    nationality = request.POST.get('nationality')   # 국적 번호
    insert_no = Member.objects.get(no = member_no)

    # 결제에 필요한 항공 스케줄 정보
    go_schedule_id = request.POST.get('go_schedule_id')
    print('go_schedule_id:',go_schedule_id)
    come_schedule_id = request.POST.get('come_schedule_id')
    print('come_schedule_id:',come_schedule_id)
    go_money = request.POST.get('go_money')
    come_money = request.POST.get('come_money')
    go_type = request.POST.get('go_type')
    come_type = request.POST.get('come_type')
    print(go_schedule_id)

    # 최종 결제금액
    final_money = int(go_money) + int(come_money)


    # 탑승객 정보(PassengerInfo) insert(입력)
    try:
        PassengerInfo.objects.create(info_collect = info_collect, nationality = nationality, rule_agree = rule_agree, danger_agree = danger_agree, m_no = insert_no)
    except Exception as e:
        print(e)
        print("탑승객 정보(PassengerInfo)등록에 실패하였습니다.")


    context = {
        're_type' : re_type,
        'way_type' : way_type,
        'insert_no' : insert_no,
        'go_schedule_id' : go_schedule_id,
        'come_schedule_id' : come_schedule_id,
        'final_money' : final_money,
        'go_type' : go_type,
        'come_type' : come_type,
    }
    

    return render(request, 'reservation/paymentpage.html', context)



# 편도에 대한 paymentpage
def ow_paymentpage(request:HttpRequest):
    # 예매 or 마일리지예매 선택
    re_type = request.POST.get('re_type')
    # 왕복 편도 선택
    way_type = request.POST.get('way_type')
    # 회원의 포인트
    m_point = request.POST.get('m_point')

    # 탑승객 정보 가져오기
    info_collect = request.POST.get('info_collect')
    rule_agree = request.POST.get('rule_agree')
    danger_agree = request.POST.get('danger_agree')
    member_no = request.POST.get('member_no')    # 스카이패스 번호
    nationality = request.POST.get('nationality')   # 국적 번호
    insert_no = Member.objects.get(no = member_no)

    # 결제에 필요한 항공 스케줄 정보
    go_schedule_id = request.POST.get('go_schedule_id')
    go_money = request.POST.get('go_money')
    go_type = request.POST.get('go_type')
    print(go_schedule_id)

    # 최종 결제금액
    final_money = int(go_money)


    # 탑승객 정보(PassengerInfo) insert(입력)
    try:
        PassengerInfo.objects.create(info_collect = info_collect, nationality = nationality, rule_agree = rule_agree, danger_agree = danger_agree, m_no = insert_no)
    except Exception as e:
        print("탑승객 정보 입력 실패")


    context = {
        're_type' : re_type,
        'way_type' : way_type,
        'insert_no' : insert_no,
        'go_schedule_id' : go_schedule_id,
        'final_money' : final_money,
        'go_type' : go_type,
        'm_point' : m_point
    }
    
    return render(request, 'reservation/ow_paymentpage.html', context)


from django.db.models import F

def inquiry(request):

    # 필요한 정보 받아오기
    go_type = request.POST.get('go_type')  # 가는 비행기 운임 타입
    come_type = request.POST.get('come_type') # 오는 비행기 운임 타입
    
    re_type = request.POST.get('re_type')   # 예매 or 마일리지예매 선택
    way_type = request.POST.get('way_type') # 왕복 편도 선택

    print('go_type: ' ,go_type)

    # print(type(come_type))
    
    print(way_type)

    # -----------------------------결제 승인번호 생성 ------------------------------------
    # 결제 승인번호 만들기
    # 결제(예매)한 날짜 (년+월+일), 스카이패스번호, 랜덤(0~9)
    # ex>2022091300018

    # 날짜 뽑기
    year = str(date.today().year)
    month = str(date.today().month)
    day = str(date.today().day)

    # 스카이패스번호 뽑기
    # 로그인 했는지 파악
    a = request.session.get('login')
    if a == "" or a == None:
        return HttpRequest(request, '/login/loginForm/')
    
    # 회원의 no를 뽑는 함수
    try:
        b= Member.objects.filter(id = a).values('no')[0]['no']
    except Exception as e:
        print("회원의 no를 가져오는데 실패했습니다.")

    # 랜덤값 한 자리 뽑기
    ran = str(random.randint(0,9))
    
    # 최종 결제승인번호
    transaction_no= year+month+day+b+ran

    # -----------------------------결제 테이블 Insert ------------------------------------

    method = int(request.POST.get('method'))
    print("method : ", method)

    # 카드번호 받아오기
    card_num1 = request.POST.get('card_num1')
    card_num2 = request.POST.get('card_num2')
    card_num3 = request.POST.get('card_num3')
    card_num4 = request.POST.get('card_num4')

    # 카드번호 합치기
    card_num = card_num1 + card_num2 + card_num3 + card_num4

    # 결제일
    pay_day = date.today()

    # 결제 금액
    final_money = request.POST.get('final_money') # 최종 결제 금액
    print("final money : ", final_money)

    print("transaction_no : ", transaction_no)

    # 탑승객 ID
    try:
        pi_no = PassengerInfo.objects.filter(m_no = b)[0]
        print('pi_no: ',pi_no)
    except Exception as e:
        print("탑승객 id 가져오는데 실패")

    # Transaction.objects.create(no=transaction_no, method=method, date = pay_day, pi_no = pi_no, price = final_money)

    # 결재 table에 insert
    try:
        if method==0:
            Transaction.objects.create(no=transaction_no, method=method, card_number = card_num, date = pay_day, pi_no = pi_no, price=final_money)
        elif method ==1:
            Transaction.objects.create(no=transaction_no, method=method, date = pay_day, pi_no = pi_no, price=final_money, account_number = "제발")
        elif method ==2:
            Transaction.objects.create(no=transaction_no, method=method, date = pay_day, pi_no = pi_no, price = final_money)
    except Exception as e:
        print("결재 table에 insert 실패")


    # -----------------------------항공권 번호 생성 ------------------------------------
    go_schedule_id = request.POST.get('go_schedule_id')  #가는 항공 스케쥴 id
    print('go_schedule_id : ', go_schedule_id)
    come_schedule_id = request.POST.get('come_schedule_id') #오는 항공 스케쥴 id
    
    # b : 스카이패스번호, pay_day: 결제한 날짜


    user_id = request.session.get('login')  # 사용자의 session
    # 회원의 마일리지 정보 가져오기
    m_point = Member.objects.filter(id = user_id).values('p_points')[0]['p_points']


    # 경로id 왕복은 go_id, come_id, 편도는 come_id
    try:
        if way_type == "왕복":
            print(type(go_schedule_id))
            go_id = FlightSchedule.objects.filter(no=go_schedule_id).values('no')[0]['no']
            print(type(go_id))
            come_id = FlightSchedule.objects.filter(no=come_schedule_id).values('no')[0]['no']
            print(come_id)

            # 항공권 번호 생성
            go_flightnumber = go_schedule_id+b+ month+day+go_id
            come_flightnumber = come_schedule_id+b+ month+day+come_id

            #------------------------마일리지 결제인 경우 회원의 포인트 차감----------------------
            user_id = request.session.get('login')  # 사용자의 session
            # 마일리지 예매를 위해 회원정보를 가져온다
            if re_type == "마일리지예매":
                # 마일리지 예매 선택시 회원의 마일리지 정보 가져오기
                try:
                    if re_type == "마일리지예매":
                        # 비행 마일리지
                        go_route_no = FlightSchedule.objects.filter(no = go_schedule_id).values('route_no')[0]['route_no']
                        come_route_no = FlightSchedule.objects.filter(no = go_schedule_id).values('route_no')[0]['route_no']
                        go_mileage = Route.objects.filter(no = go_route_no).values('mileage')[0]['mileage']
                        come_mileage = Route.objects.filter(no = come_route_no).values('mileage')[0]['mileage']
                        
                        final_mileage = int(m_point) - (int(go_mileage) + int(come_mileage))
                        Member.objects.filter(id = user_id).update(p_points = final_mileage)
                except Exception as e:
                    print("회원 마일리지 변경 실패")
            #-----------------------일반결제인 경우 회원 포인트 추가
            elif re_type == "예매":
                # 비행 포인트
                go_route_no = FlightSchedule.objects.filter(no = go_schedule_id).values('route_no')[0]['route_no']
                come_route_no = FlightSchedule.objects.filter(no = go_schedule_id).values('route_no')[0]['route_no']
                go_points = Route.objects.filter(no = go_route_no).values('points')[0]['points']
                come_points = Route.objects.filter(no = come_route_no).values('points')[0]['points']

                final_points = int(m_point) + int(go_points) + int(come_points)
                Member.objects.filter(id = user_id).update(p_points =  final_points)

        elif way_type == "편도":
            print(type(go_schedule_id))
            go_id = FlightSchedule.objects.filter(no=go_schedule_id).values('no')[0]['no']
            print('go_id: ', go_id)
            come_id = ""
            
            # 항공권 번호 생성
            go_flightnumber = go_schedule_id+b+ month+day+go_id
            print('go_flightnumber: ', go_flightnumber)

            #------------------------마일리지 결제인 경우 회원의 포인트 차감----------------------
            # 마일리지 예매를 위해 회원정보를 가져온다
            if re_type == "마일리지예매":
                # 비행 마일리지
                go_route_no = FlightSchedule.objects.filter(no = go_schedule_id).values('route_no')[0]['route_no']
                go_mileage = Route.objects.filter(no = go_route_no).values('mileage')[0]['mileage']
                
                final_mileage = int(m_point) - int(go_mileage)
                Member.objects.filter(id = user_id).update(p_points = final_mileage)
            #-----------------------일반결제인 경우 회원 포인트 추가
            elif re_type == "예매":
                # 비행 포인트
                go_route_no = FlightSchedule.objects.filter(no = go_schedule_id).values('route_no')[0]['route_no']
                go_points = Route.objects.filter(no = go_route_no).values('points')[0]['points']

                final_points = int(m_point) + int(go_points)
                Member.objects.filter(id = user_id).update(p_points = final_points)

    except Exception as e:
        print(e)
        print("항공스케줄 가져오는데 실패")



    # -----------------------------예매 번호 생성 ------------------------------------

    rann1 = random.randint(65,90)
    rann2 = random.randint(65,90)
    alpha= chr(rann1) + chr(rann2)

    # 왕복, 편도에 따라 다르게 예매번호 생성
    if way_type == "왕복":
        reservation_number = alpha + go_schedule_id + come_schedule_id + b
    elif way_type == "편도":
        reservation_number = alpha + go_schedule_id + b

    print(reservation_number)

    # -----------------------------예매 테이블 INSERT------------------------------------
    c = Member.objects.get(id = a)

    # 왕복, 편도에 따라 go, come 뽀린키(no) 뽑아내기
    try:
        if way_type == "왕복":
            go_id_re = FlightSchedule.objects.get(no=go_schedule_id)
            come_id_re = FlightSchedule.objects.get(no=come_schedule_id)

            print(go_id_re)
            print(come_id_re)
        elif way_type == "편도":
            go_id_re = FlightSchedule.objects.get(no=go_schedule_id)
            come_id_re = ""
            print('go_id_re:' ,go_id_re)
    except Exception as e:
        print("항공 스케줄 가져오는데 실패")


    # 결재승인번호 가져오기
    try:
        t_no = Transaction.objects.filter(no = transaction_no)[0]
        print(t_no)
    except Exception as e:
        print("결재승인번호 가져오는데 실패")

    
    # 왕복이면 같은 예매번호로 2개 생성, 편도면 1개만 생성
    try:
        if way_type == "왕복":
            Reservation.objects.create(re_no = reservation_number,m_no= c, flight_no = go_flightnumber,
            f_no =go_id_re, fare_type = go_type,baggage_check=0, t_no= t_no)
            Reservation.objects.create(re_no = reservation_number,m_no= c, flight_no = come_flightnumber,
            f_no =come_id_re, fare_type = come_type,baggage_check=0, t_no= t_no)

            # re_idx1 = Reservation.objects.get(re_no = reservation_number, m_no= c, flight_no = go_flightnumber)
            re_idx1 = Reservation.objects.get(re_no = reservation_number, m_no= c, f_no = go_id_re)
            PassengerForm.objects.create(re_idx = re_idx1 )

            re_idx2 = Reservation.objects.get(re_no = reservation_number, m_no= c, f_no = come_id_re)
            PassengerForm.objects.create(re_idx = re_idx2 )

            # 항공스케쥴 좌석 하나 까기
            # 가는편
            FlightSchedule.objects.filter(no=go_id_re.no).update(remain_seats = F('remain_seats') - 1)

            # 오는편           
            FlightSchedule.objects.filter(no=come_id_re.no).update(remain_seats = F('remain_seats') - 1)

        
        elif way_type == "편도":
            Reservation.objects.create(re_no = reservation_number,m_no= c, flight_no = go_flightnumber,
            f_no =go_id_re, fare_type = go_type,baggage_check=0, t_no= t_no)

            re_idx1 = Reservation.objects.get(re_no = reservation_number, m_no= c,  f_no = go_id_re)
            PassengerForm.objects.create(re_idx = re_idx1)

            FlightSchedule.objects.filter(no=go_id_re.no).update(remain_seats = F('remain_seats') - 1)

    except Exception as e:
        print("예매 table에 insert 실패")
    
    else:
        msg = '예약이 완료되었습니다.'
        url = '/inquiry/'

    context={
        'msg':msg,
        'url' : url
    }
    

    return render(request, 'reservation/inquiry.html',context)






