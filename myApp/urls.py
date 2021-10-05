from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls import url




urlpatterns = [
    path('', views.new_register, name='new_register'),
    path('topScreen', views.topScreen, name='topScreen'),
    path('details_screen', views.details_screen, name='details_screen'),
    #性格診断
    path('<int:id>/personal', views.personal_view, name='personal'),
    path('<int:id>personal2', views.personal2, name='personal2'),
    path('<int:id>/select', views.select, name='select'),
    
    #ユーザの詳細情報を表示する処理を呼び出す
    path('<int:id>', views.showDetail, name='showDetail'),
    #ユーザの登録フォームを呼び出す
    path('create', views.showCreateUserForm, name='showCreateForm'),
    #ユーザ登録完了
    path('create_completion', views.create_completion, name='create_completion'),
    #ユーザ情報
    path('showUsers', views.showUsers, name='showUsers'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addUser, name='addUser'),
    #ログイン
    path('login_user', views.Login, name='login_user'),
    #ログアウト
    path("logout",views.Logout,name="Logout"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
