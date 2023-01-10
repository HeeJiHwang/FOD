from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('admin_result/', views.admin_result),
    path('flight_schedule/' , views.flight_schedule),
    path('list_admin/', views.list_admin),
    path('create_admin/', views.create_admin),

    # board
    path('board/',include('board.urls')),
    path('qna/qna/',views.qna),
    path('qna/adminqnaread/',views.adminqnaread),
    path('qna/adminqnadelete/',views.adminqnadelete),
    path('<int:no>/comment',views.qnacommentInsert),
    path('inform/inform/',views.inform),
    path('inform/admininformread/',views.admininformread),    
    path('inform/admininformwrite/',views.admininformwrite),
    path('inform/admincheckWrite/',views.admincheckWrite),
    path('inform/admininformupdate/',views.admininformupdate),
    path('inform/admininformcheckUpdate/',views.admininformcheckUpdate),
    path('inform/admininformdelete/',views.admininformdelete),


    # flight schedule
    path('create_schedule/', views.create_schedule),
    path('create_result/', views.create_result),

    # inquiry/checkin
    path('list_passenger/', views.list_passenger),
]