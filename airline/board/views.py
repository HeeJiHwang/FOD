
from django.http import HttpRequest
from .forms import BoardWriteForm
from django.shortcuts import render,redirect

from django.core.paginator import Paginator
from .models import Inform
from .models import InformCategory
from .models import Qna
from .models import QnaCategory
from .models import Member
from .models import Admin
# from .models import Admin
# Create your views here.

def list(request:HttpRequest):
    
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
    return render(request, 'board/inform/informlist.html',context)

def write(request):
    board = InformCategory.objects.all()
    forms = BoardWriteForm()
    context = {
        'forms' : forms,
        'board' : board
    }
    return render(request,'board/inform/writeForm.html',context)

def checkWrite(request:HttpRequest):
    
    id = request.session['admin']
    admin = Admin.objects.get(d_no = id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = request.POST.get('cate')
    cate = InformCategory.objects.get(no=board)
    date = request.POST.get('date')
    print(cate)
    print(board)
    # print(cate)
    # print(type(cate))
    # context = {
    #     'title' : title,
    #     'content' : content,
    #     'cate' : cate,
    #     'date' : date
    # }
    
    # # cate.update(ic_no=1)
    # # Inform.objects.update(title=title,content=content,ic_no=1, date=date)
    # Inform.objects.create(title = title,content = content,ic_no=cate,date=date)


    try:
        Inform.objects.create(title = title,content = content,a_no=admin, ic_no=cate, date=date)
    except Exception as e:
        print(e)
        url = '/board/inform/write/'
        msg = '글쓰기에 실패 하였습니다.'
    else:
        url = '/board/list/'
        msg = '글쓰기에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'board/inform/result.html',context)

def read(request:HttpRequest):
    
    no = request.GET.get('no')

    board = Inform.objects.get(no = no)

    board.save()

    context = {
        'content' : board
    }

    return render(request,'board/inform/read.html',context)

def update(request:HttpRequest):
    no = request.GET.get('no')

    board = Inform.objects.get(no = no)

    forms = BoardWriteForm(instance=board)
    context = {
        'forms' : forms,
        'no' : no,
    }

    return render(request,'board/inform/updateForm.html',context)

def checkUpdate(request:HttpRequest):
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
        url = '/board/inform/update/?no=' + no
        msg = '글수정에 실패 하였습니다.'
    else:
        url = '/board/inform/read/?no=' + no
        msg = '글수정에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'board/inform/result.html',context)

def delete(request:HttpRequest):
    no = request.GET.get('no')
    
    url = None
    msg = None
    try:
        board = Inform.objects.get(no=no).delete()
    except Exception as e:
        print(e)
        url = '/board/read/?no=' + no
        msg = '글삭제에 실패 하였습니다.'
    else:
        url = '/board/list/'
        msg = '글삭제에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }
    
    



    return render(request,'board/inform/result.html',context)


def qnalist(request:HttpRequest):
    try:
        iid = request.session['login']  # id 값 뽑기
        b = Member.objects.filter(id = iid).values('no')[0]['no']
        boardList = Qna.objects.filter(m_no = b).order_by('no')
        MAX_PAGE_CNT = 10
        MAX_LIST_CNT = 5
        # id = request.session['login']


        # boardList = Qna.objects.all().order_by('no')
        
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
        msg = ''
        context = {
        'list' : page_obj,
        'last_page' : last_page,
        'start_page' : start_page,
        'end_page' : end_page,
        'msg' : msg
        
    }
        
    except Exception as e:
        msg = ''
        context = {
            'msg' : msg
        }

    # qna리스트는 어드민 아이디로는 무조건 다 나와야됨

    
    

    
    return render(request, 'board/qna/qnalist.html',context)


def qnawrite(request):
    board = QnaCategory.objects.all()
    forms = BoardWriteForm()
    context = {
        'forms' : forms,
        'board' : board
    }
    return render(request,'board/qna/qnawriteForm.html',context)

def qnacheckWrite(request:HttpRequest):
    

    id = request.session['login']
    member = Member.objects.get(id = id)    
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = request.POST.get('cate')
    cate = QnaCategory.objects.get(no=board)
    date = request.POST.get('date')
    
    url = None
    msg = None
    
    try:
        board = Qna.objects.create(title = title,content = content,m_no=member, qc_no=cate, date=date)
    except Exception as e:
        print(e)
        url = '/board/qna/qnawrite/'
        msg = '글쓰기에 실패 하였습니다.'
    else:
        url = '/board/qnalist/'
        msg = '글쓰기에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
        'id' : id,
    }

    return render(request,'board/qna/qnaresult.html', context)


def qnaread(request:HttpRequest):

    no = request.GET.get('no')

    board = Qna.objects.get(no = no )

    board.save()

    comments = Qna.objects.filter(answer = no)
    context = {
        'content' : board,
        'comments' : comments,
    }

    return render(request,'board/qna/qnaread.html',context)

def qnaupdate(request:HttpRequest):
    no = request.GET.get('no')

    board = Qna.objects.get(no = no)

    forms = BoardWriteForm(instance=board)
    context = {
        'forms' : forms,
        'no' : no,
    }

    return render(request,'board/qna/qnaupdateForm.html',context)

def qnacheckUpdate(request:HttpRequest):
    no = request.POST.get('no')
    title = request.POST.get('title')
    content = request.POST.get('content')

    content = content.replace('\r\n','<br>')

    url = None
    msg = None
    try:
        board = Qna.objects.filter(no=no).update(title = title,content = content)
    except Exception as e:
        print(e)
        url = '/board/qna/qnaupdate/?no=' + no
        msg = '글수정에 실패 하였습니다.'
    else:
        url = '/board/qna/qnaread/?no=' + no
        msg = '글수정에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'board/qna/qnaresult.html',context)

def qnadelete(request:HttpRequest):
    no = request.GET.get('no')
    
    url = None
    msg = None
    try:
        board = Qna.objects.get(no=no).delete()
    except Exception as e:
        print(e)
        url = '/board/qnaread/?no=' + no
        msg = '글삭제에 실패 하였습니다.'
    else:
        url = '/board/qnalist/'
        msg = '글삭제에 성공하였습니다.'

    context = {
        'url' : url,
        'msg' : msg,
    }

    return render(request,'board/qna/qnaresult.html',context)

def qnacommentInsert(request:HttpRequest,no):
    id = request.session['login']
    member = Member.objects.get(id = id)  
    # board = Qna.objects.get(no=no)
    content = request.POST.get('content')
   
    content = content.replace('\r\n','<br>')
    

    try:
        comment = Qna.objects.filter(no=no).update(no=no, m_no = member,answer=content)
    except Exception as e:
        print(e)
    return redirect('/board/qna/qnaread/?no=' + str(no))