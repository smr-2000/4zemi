from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

#ページが存在すれば表示、しなければ404エラー
from django.shortcuts import get_object_or_404
from .models import login

# Create your views here.

def new_register(request):
    return render(request, 'myApp/new_register.html', {})

def topScreen(request):
    return render(request, 'myApp/topScreen.html', {})

def details_screen(request):
    return render(request, 'myApp/details-screen.html', {})

#ユーザ情報を辞書に格納して、users.htmlに返す
def showUsers(request):
    userinfo = login.objects.all()
    context = {
        'msg':'ユーザ数',
        'userinfo':userinfo,
        'count':userinfo.count,
    }
    return render(request, 'myApp/users.html', context)

#URLから受け取ったidを元にユーザの詳細情報を取得、detail.htmlに返す
def showDetail(request,id):
    userinfoDetail = get_object_or_404(login, pk=id)
    context = {
        'userinfoDetail':userinfoDetail,
    }
    return render(request, 'myApp/detail.html', context)

def showCreateUserForm(request):
    #フォームを変数にセット
    form = UserForm()

    context = {
        'userForm':form,
    }

    return render(request, 'myApp/create.html', context)

def addUser(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
        
        #登録後、全件データを抽出
        userinfo = login.objects.all()
        context = {
            'msg':'ユーザ数',
            'userinfo': userinfo,
            'count':userinfo.count,
        }
    return render(request, 'myApp/users.html', context)

def showEditUserForm(request, id):
    userinfo = get_object_or_404(login, pk=id)
    userForm = UserForm(instance=login)

    context = {
        'login':login,
        'userForm':userForm,
    }
    return render(request, 'myApp/user_edit.html', context)
