from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inquiry),
    path('detail/', views.inquiry_detail),
    path('reser_cancel/', views.reser_cancel),  # 은수가 추가!(예약 취소)
]
