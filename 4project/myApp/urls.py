from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', views.new_register, name='new_register'),
    path('<int:id>/topScreen', views.topScreen, name='topScreen'),
    path('<int:id>/<int:user_id>/details_screen', views.details_screen, name='details_screen'),
    #いいね
    path('<int:id>/Heart_add', views.Heart_add, name='Heart_add'),
    #いいね一覧
    path('<int:id>/Heart_list', views.Heart_list, name='Heart_list'),
     #性格診断
    path('<int:id>/personal', views.personal_view, name='personal'),
    path('<int:id>/select', views.select, name='select'),

     #フレンド申請
    path('<int:id>/<user_id>/friend_request', views.friend_request, name='friend_request'),
    path('<int:id>/friend_req_list', views.friend_req_list, name='friend_req_list'),
    path('<int:id>/friends_list', views.friends_list, name='friends_list'),
    path('<int:id>/<int:allow_id>/friend_allow', views.friend_allow, name='friend_allow'),
    path('<int:id>/<int:allow_id>/friend_delete', views.friend_delete, name='friend_delete'),
    
    #メッセージ
     path('<int:id>/<int:user_id>/message', views.message, name='message'),
    
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
    #ユーザ情報更新フォーム
    path("<int:id>/user_update",views.UserUpdate, name='user_update'),
    #ユーザ情報更新
    path('<int:id>/updateUser', views.updateUser, name='updateUser'),
    #マイページ登録画面を呼び出す
    path('<int:id>/user_adddetail', views.showUserDetail, name='user_adddetail'),
    #マイページ登録
    path('<int:id>/add_userdetail', views.addUserDetail, name='add_userdetail'),
    #マイページ更新画面を呼び出す
    path("<int:id>/mypage_update",views.MypageUpdate, name='Mypage_update'),
    #マイページ更新
    path('<int:id>/updateMypage', views.updateMypage, name='updateMypage'),
    #マイページ
    path('<int:id>/Mypage', views.showMypage, name='Mypage'),

    #趣味選択フォームを呼び出す
    path('<int:id>/show_selectHobby', views.showSelectHobby, name='show_selectHobby'),
    #趣味選択
    path('<int:id>/add_selectHobby', views.addSelectHobby, name='add_selectHobby'),

    #退会確認
    path('<int:id>/userCheckDelete', views.UserCheckDelete, name='userCheckDelete'),
    #退会
    path('<int:id>/userDelete', views.UserDelete, name='userDelete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
