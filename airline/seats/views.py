from django.shortcuts import render
from checkin.models import AircraftType, Member, PassengerForm, Reservation, PassengerForm, FlightSchedule

# Create your views here.
def seat(request):
    # 로그인한 id
    my_id = request.session.get('login')
    print('my_id : ', my_id)
    
    # 로그인한 id 계정의 스카이패스 번호
    skypass_num = Member.objects.get(id = my_id).no
    print('skypass_num: ', skypass_num)

    # 내가 선택한 예매 idx
    reservation_idx = request.GET.get('re_idx')
    print('reservaion_idx: ', reservation_idx)  

    #내가 탈 항공기의 행/열
    # 예매 - 항공스케쥴 - 항공기 - 행/열

    reservation = Reservation.objects.get(idx = reservation_idx)

    flight_schedule_no = reservation.f_no.no  # 내가 선택한 항공 스케쥴 id
    print('flight_schedule_no: ', flight_schedule_no)

    row= int(reservation.f_no.at_no.seat_row) +1
    col= int(reservation.f_no.at_no.seat_column)+1
    print('reservation: ' ,reservation)
    print('row: ', row)
    print('col: ', col)

    # 내가 선택한 항공 스케쥴id를 가지고 있는 모든 예매 idx뽑기
    all_idx = Reservation.objects.filter(f_no=flight_schedule_no).values_list('idx',flat=True)
    reservation_list = list(all_idx)
    print('reservation_list: ', reservation_list)

    # 내가 선택한 항공 스케쥴 id를 가지고있는 모든 예매 idx를 이용한 선택된 좌석 뽑기
    selected_seat = PassengerForm.objects.filter(re_idx__in = reservation_list).values_list('seat', flat=True)
    selected_seat_list = list(selected_seat)
    print('selected_seat_list: ',selected_seat_list)

    # 뽑힌 좌석들의 열을 str 형태의 숫자로 변환시켜주기   3B , 10C
    s = '0ABCDEFGHI'
    
    change_seat =[]
    for i in range(len(selected_seat_list)):
        if selected_seat[i]==None:
            pass
        else:
            iint = selected_seat[i][-1]
            change = s.find(iint)
            real_seat = selected_seat[i][:-1] + str(change)
            change_seat.append(real_seat)
    print('change_seat:',change_seat)



    # 좌석 열 리스트 뽑기
    col_list = []
    for i in range(65,65+col-1):
        col_list.append(chr(i))
    print(col_list)

    context={
        'row' : row,
        'col' : col,
        'change_seat' : change_seat,
        'idx' : reservation_idx,
        'col_list':col_list

    }


    # 그 스카이 패스번호랑 같고
    # + 내가 선택한 예매idx 와 같은 예매





    return render(request, 'seats/seat.html',context)





def seatresult(request):

    # 내가 선택한 예매의 idx
    idx = request.GET.get('idx')
    print('idx: ㅠㅠ' , idx)

    id = request.session['login']

    seat = request.GET.get('seat')   #  내가 선택한 좌석 번호
    print(seat)
    
    li = '0ABCDEFGH'            # 열의 값을 치환해줄 문자열
    ind= int(seat[-1])

    st = li[ind]
    real_seat = seat[:-1] +st

    
    member = Member.objects.get(id = id)    #로그인된 멤버 데이터
    mem = Reservation.objects.get(idx=idx )
    print(member)
    
    try:
        PassengerForm.objects.filter(re_idx=mem).update(seat = real_seat)
        msg = "자리 지정이 완료되었습니다.   선택된 좌석 : "+real_seat
        url = '/'
    except:
        msg = "오류가 발생했습니다 다시 시도해주십시오."
        url = '/checkin/'


    context = {
        'seat' : seat,
        # 'passenger' : passenger,
        'real_seat' : real_seat,
        'msg' : msg,
        'url' : url,
    }


    return render(request, 'seats/seatresult.html',context)
    
    






