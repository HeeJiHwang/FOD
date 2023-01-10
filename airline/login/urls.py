from django.urls import path
from . import views

urlpatterns = [

    # 일반 회원
    path('loginForm/',views.loginForm),
    path('checkLogin/',views.checkLogin),
    path('logout/',views.logout),

    # 마이페이지
    path('my/',views.my),
    path('mymileges/',views.mymileges),

    # 관리자
    path('admin_loginForm/',views.admin_loginForm),
    path('admin_checkLogin/',views.admin_checkLogin),
    
    #회원 탈퇴(은수가 추가)
    path('memberOut/', views.memberOut),
]