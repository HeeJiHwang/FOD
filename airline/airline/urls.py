"""airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 메인페이지
    path('', views.index),

    # 관리자 페이지
    path('admin_manage/', include('admin_manage.urls')),

    # 항공권 예매하기
    path('reservation/', include('reservation.urls')),

    # 회원가입 및 로그인
    path('login/', include('login.urls')),
    path('join/', include('join.urls')),

    # 게시판
    path('board/',include('board.urls')),

    # 예약조회/체크인/좌석지정
    path('inquiry/', include('inquiry.urls')),
    path('seats/', include('seats.urls')),
    path('checkin/', include('checkin.urls')),

    #수하물
    path('airline/airplane/',views.airplane),
    path('airline/baggage/', views.baggage),
    path('airline/restricteditems/',views.restricteditems),
    path('airline/carryon/',views.carryon),
    path('airline/damagedorlost/',views.damagedorlost),
    path('airline/broke/',views.broke),
    path('airline/lost/',views.lost),
    path('airline/checkno/',views.checkno),
    path('airline/no/',views.no),
    path('airline/aircraft737/',views.aircraft737),
    path('airline/aircraft747/',views.aircraft747),
    path('airline/aircraft777/',views.aircraft777), 
]
