from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_register, name='new_register'),
    path('topScreen', views.topScreen, name='topScreen'),
    path('details_screen', views.details_screen, name='details_screen'),
    

    #ユーザの詳細情報を表示する処理を呼び出す
    path('<int:id>', views.showDetail, name='showDetail'),
    #ユーザの登録フォームを呼び出す
    path('create', views.showCreateUserForm, name='showCreateForm'),
    #ユーザ情報
    path('showUsers', views.showUsers, name='showUsers'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addUser, name='addUser'),
    
]
