from django.urls import path
from . import views

urlpatterns = [
    path('',views.list),
    path('list/',views.list),
    path('inform/write/',views.write),
    path('inform/checkWrite/',views.checkWrite),
    path('inform/read/',views.read),
    path('inform/update/',views.update),
    path('inform/checkUpdate/',views.checkUpdate),
    path('inform/delete/',views.delete),
    path('qnalist/',views.qnalist),
    path('qna/qnawrite/',views.qnawrite),
    path('qna/qnacheckWrite/',views.qnacheckWrite),
    path('qna/qnaread/',views.qnaread),
    path('qna/qnaupdate/',views.qnaupdate),
    path('qna/qnacheckUpdate/',views.qnacheckUpdate),
    path('qna/qnadelete/',views.qnadelete),
    path('<int:no>/comment',views.qnacommentInsert),
]
