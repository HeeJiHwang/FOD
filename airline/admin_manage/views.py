from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
# Create your views here.
from admin_manage.models import Admin , Departments , FlightSchedule, Qna, QnaCategory, Inform, InformCategory , AircraftType,Route,PassengerForm
from .forms import BoardWriteForm
from django.core.paginator import Paginator


def index(request):
    return render(request,'admin_manage/admin_result.html')

def admin_result(request):
    name = request.POST.get('name')
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    email = request.POST.get('email')
    d = request.POST.get('department')  # 숫자

    department = Departments.objects.get(no = d)
    print(name)
    print(id)
    print(pw)
    print(email)
    print(department)

    try:
        Admin.objects.create(id=id, pw=pw, email=email, d_no= department, name=name)
    except Exception as e:
        msg= '계정 생성에 실패하였습니다.'
    else:
        msg= '계정 생성에 성공하였습니다.'

    context = {
        'msg' :msg
    }

    return redirect('/admin_manage/')

    
def flight_schedule(request:HttpRequest):
    flight = FlightSchedule.objects.all()

    context = {
        'flight' :flight
    }

    return render(request, 'admin_manage/flight_schedule.html', context)


# 인사과  / 직원 계정 생성 및 관리
def list_admin(request):
    admin = Admin.objects.all()

    context={
        'admin' :admin
    }

    return render(request,'admin_manage/list_admin.html',context)


def create_admin(request):
    
    return render(request,'admin_manage/create_admin.html' )



# 게시판 / 공지사항 및 QnA 관리
def qna(request:HttpRequest):

    MAX_PAGE_CNT = 10
    MAX_LIST_CNT = 5

    boardList = Qna.objects.all().order_by('no')

    page = request.GET.get('page','1')# page 파라미터가 있으면 값을 가져오고 없으면 1을 반환하겟다..

    #페이징처리
    paginator = Paginator(boardList,MAX_LIST_CNT)
    # Paginator 객체 생성할때 리스트값이랑 한페이지당 띄울 글개수
    page_obj = paginator.get_page(page)
    # 해당페이지에 해당하는 글을 저장....
    
    #끝페이지.
    last_page = 0
    for last_page in paginator.page_range:
        last_page += 1

    #페이지그룹의 블록...
    current_block = ((int(page) - 1) // MAX_PAGE_CNT) + 1
    
    start_page = (current_block - 1) * MAX_PAGE_CNT + 1

    end_page = start_page + MAX_PAGE_CNT - 1

    context = {
        'list' : page_obj,
        'last_page' : last_page,
        'start_page' : start_page,
        'end_page' : end_page,
    }
    return render(request,'admin_manage/qna/qna.html',context)

    # qna리스트는 어드민 아이디로는 무조건 다 나와야됨

    
def adminqnaread(request:HttpRequest):

    no = request.GET.get('no')

    board = Qna.objects.get(no = no )

    board.save()

    comments = Qna.objects.filter(answer = no)
    context = {
        'content' : board,
        'comments' : comments,
    }

    return render(request,'admin_manage/qna/adminqnaread.html',context)




def adminqnadelete(request:HttpRequest):
    no = request.GET.get('no')
    
    url = None
    msg = None
    try:
        board = Qna.objects.get(no=no).delete()
    except Exception as e:
        print(e)
        url = '/admin_manage/qna/adminqnaread/?no=' + no
        msg = '글삭제에 실패 하였습니다.'
    else:
        url = '/admin_manage/qna/qna/'
        msg = '글삭제에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'admin_manage/qna/adminqnaresult.html',context)   

def qnacommentInsert(request:HttpRequest,no):

    # id = request.session['admin']
    # admin = Admin.objects.get(d_no = id)  

    content = request.POST.get('content')
   
    content = content.replace('\r\n','<br>')
    

    try:
        comment = Qna.objects.filter(no=no).update(no=no,answer=content)
    except Exception as e:
        print(e)
    return redirect('/admin_manage/qna/adminqnaread/?no=' + str(no))

def inform(request:HttpRequest):
    
    MAX_PAGE_CNT = 10
    MAX_LIST_CNT = 4

    boardList = Inform.objects.all().order_by('no')
    page = request.GET.get('page','1') # page 파라미터가 있으면 값을 가져오고 없으면 1을 반환하겠다.
    #페이징처리
    paginator = Paginator(boardList,MAX_LIST_CNT)
    # Paginator 객체 생성할때 리스트 값이랑 한페이지당 띄울 글 갯수 -----위에는 지금 5개 

    page_obj = paginator.get_page(page)
    # 해당페이지에 해당하는 글을 저장


    # 끝페이지
    last_page = 0
    for last_page in paginator.page_range:
        last_page += 1

    # 페이지 그룹의 블록 # 아래에 1 2 3 4 5 6 7 8 9 10 뜨는거
    current_block = ((int(page) - 1) // MAX_PAGE_CNT) + 1
    
    start_page = (current_block - 1) * MAX_PAGE_CNT + 1 

    end_page = start_page + MAX_PAGE_CNT - 1  # +9 로 해도 상관없음 같은 값

    context = {
        'list' : page_obj,
        'last_page' : last_page,
        'start_page' : start_page,
        'end_page' : end_page,
    }
    return render(request, 'admin_manage/inform/inform.html',context)

def admininformread(request:HttpRequest):
    no = request.GET.get('no')

    board = Inform.objects.get(no = no)

    board.save()

    context = {
        'content' : board
    }

    return render(request,'admin_manage/inform/admininformread.html',context)

def admininformwrite(request):
    board = InformCategory.objects.all()
    forms = BoardWriteForm()
    context = {
        'forms' : forms,
        'board' : board
    }
    return render(request,'admin_manage/inform/admininformwriteForm.html',context)



def admincheckWrite(request:HttpRequest):
    
    id = request.session['admin']
    admin = Admin.objects.get(d_no = id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = request.POST.get('cate')
    cate = InformCategory.objects.get(no=board)
    date = request.POST.get('date')


    try:
        Inform.objects.create(title = title,content = content,a_no=admin, ic_no=cate, date=date)
    except Exception as e:
        print(e)
        url = '/admin_manage/inform/admininformwrite/'
        msg = '글쓰기에 실패 하였습니다.'
    else:
        url = '/admin_manage/inform/inform/'
        msg = '글쓰기에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'admin_manage/inform/admininformresult.html',context)

def admininformupdate(request:HttpRequest):
    no = request.GET.get('no')

    board = Inform.objects.get(no = no)

    forms = BoardWriteForm(instance=board)
    context = {
        'forms' : forms,
        'no' : no,
    }

    return render(request,'admin_manage/inform/admininformupdateForm.html',context)

def admininformcheckUpdate(request:HttpRequest):
    no = request.POST.get('no')
    title = request.POST.get('title')
    content = request.POST.get('content')

    content = content.replace('\r\n','<br>')

    url = None
    msg = None
    try:
        board = Inform.objects.filter(no=no).update(title = title,content = content)
    except Exception as e:
        print(e)
        url = '/admin_manage/inform/admininformupdate/?no=' + no
        msg = '글수정에 실패 하였습니다.'
    else:
        url = '/admin_manage/inform/admininformread/?no=' + no
        msg = '글수정에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'admin_manage/inform/admininformresult.html',context)

def admininformdelete(request:HttpRequest):
    no = request.GET.get('no')
    
    url = None
    msg = None
    try:
        board = Inform.objects.get(no=no).delete()
    except Exception as e:
        print(e)
        url = '/admin_manage/inform/admininformread/?no=' + no
        msg = '글삭제에 실패 하였습니다.'
    else:
        url = '/admin_manage/inform/inform/'
        msg = '글삭제에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }
    

    return render(request,'admin_manage/inform/admininformresult.html',context)


def create_schedule(request):
    

    return render(request, 'admin_manage/create_schedule.html')

def create_result(request):
    no = len(FlightSchedule.objects.all()) + 1

    fk_at_no = request.POST.get('at_no')  # FK
    at_no = AircraftType.objects.get(no=fk_at_no)

    fk_route_no = int(request.POST.get('route_no')) # FK
    print(fk_route_no)
    route_no = Route.objects.get(no = fk_route_no)
    print(route_no)

    departure_date = request.POST.get('departure_date')
    arrival_date = request.POST.get('arrival_date')
    departure_time = request.POST.get('departure_time')
    arrival_time = request.POST.get('arrival_time')
    gate_number = request.POST.get('gate_number')

    seats = AircraftType.objects.get(no=fk_at_no).seats

    try:
        FlightSchedule.objects.create(no=no, at_no=at_no, route_no=route_no, departure_date=departure_date, departure_time=departure_time,
        arrival_date=arrival_date, arrival_time=arrival_time, gate_number=gate_number, remain_seats=seats)
        return redirect('/admin_manage/')

    except Exception as e:
        return render(request, 'admin_manage/create_schedule.html')
        

# 혜지  
def list_passenger(request):

    schedule = FlightSchedule.objects.all().order_by('no')

    passenger = PassengerForm.objects.all()



    context = {
        'schedule' : schedule,
        'passenger' : passenger,
    }

    return render(request, 'admin_manage/list_passenger.html', context)