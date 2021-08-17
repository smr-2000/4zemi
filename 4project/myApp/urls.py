from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.new_register, name='new_register'),
    path('topScreen', views.topScreen, name='topScreen'),
    

    #ユーザの詳細情報を表示する処理を呼び出す
    path('<int:id>', views.showDetail, name='showDetail'),
    #ユーザの登録フォームを呼び出す
    path('create', views.showCreateUserForm, name='showCreateForm'),
    #ユーザ情報
    path('showUsers', views.showUsers, name='showUsers'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addUser, name='addUser'),
    #ユーザ情報編集
    path('<int:id>/edit', views.showEditUserForm, name='showEditUserForm'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
