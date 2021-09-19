from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import UserForm
from .forms import LoginForm
from .forms import AddUserForm
from .forms import UserDetailForm
from .forms import SelectHobby

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#ページが存在すれば表示、しなければ404エラー
from django.shortcuts import get_object_or_404
from .models import login
from .models import UserDetail

# Create your views here.

def new_register(request):
    return render(request, 'myApp/new_register.html', {})

def details_screen(request):
    return render(request, 'myApp/details-screen.html', {})

def create_completion(request):
    return render(request, 'myApp/create_completion.html', {})

#診断
def select(request):
    return render(request, 'myApp/select.html', {})

#性格診断
def personal(request):
    return render(request, 'myApp/personal.html', {})

#趣味診断
def selectHobby(request):
    favorite_hobby = SelectHobby()
    context = {
        'favorite_hobby':favorite_hobby,
        }
    return render(request, 'myApp/selectHobby.html', context)

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
    params = {
        "AccountCreate":False,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
    }
    params["account_form"] = UserForm()
    params["add_account_form"] = AddUserForm()
    params["AccountCreate"] = False
    return render(request, "myApp/create.html", context=params)

def addUser(request):
    params = {
        "AccountCreate":False,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
    }
    #リクエストがPOSTの場合
    if request.method == 'POST':
        params["account_form"] = UserForm(request.POST)
        params["add_account_form"] = AddUserForm(request.POST,request.FILES)
        
        if params["account_form"].is_valid() and params["add_account_form"].is_valid():
           #アカウント情報をDB保存
                account = params["account_form"].save()
                account.set_password(account.password)
                account.save()

                #追加情報
                add_account = params["add_account_form"].save(commit=False)
                #UserFormとAddUserForm 1vs1 紐付け
                add_account.user = account

                add_account.save()

                #アカウト作成情報更新
                params["AccountCreate"] = True

        else:
                #フォームが有効でない場合
            print(params["account_form"].errors)
            return render(request, 'myApp/create.html', context=params)
        
    return render(request, 'myApp/create_completion.html')


def Login(request):
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        user = authenticate(username=ID, password=Pass)

        if user:
            if user.is_active:
                #ログイン
                login(request, user)
                return render(request, 'myApp/topScreen.html', {'user':user})
            else:
                #アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        #ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    #GET
    else:
        return render(request, 'myApp/login_user.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myApp/login_user'))

#ログイン後ホーム
@login_required
def topScreen(request):
    return render(request, "myApp/topScreen.html")

def UserUpdate(request, id):
    userinfo = get_object_or_404(login, pk=id)
    userUpdateForm = AddUserForm(instance=userinfo)
    context = {
        'userinfo':userinfo,
        'userUpdateForm':userUpdateForm,
    }
    return render(request, 'myApp/user_update.html',context)

def updateUser(request,id):
    if request.method == 'POST':
        userInfo = get_object_or_404(login,pk=id)
        userUpdateForm = AddUserForm(request.POST, request.FILES, instance=userInfo)
        if userUpdateForm.is_valid():
            userUpdateForm.save()
 
    return render(request, 'myApp/new_register.html')


def showUserDetail(request, id):
    userinfo = get_object_or_404(login, pk=id)
    #フォームを変数にセット
    params = {
        "userinfo":userinfo,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
        "user_detail_form":UserDetailForm(),
    }
    params["account_form"] = UserForm()
    params["add_account_form"] = AddUserForm()
    params["user_detail_form"] = UserDetailForm()
    return render(request, "myApp/user_adddetail.html", context=params)

def addUserDetail(request ,id):
    userinfo = get_object_or_404(login, pk=id)
    params = {
        "userinfo":userinfo,
        "account_form":UserForm(),
        "add_account_form":AddUserForm(),
        "user_detail_form":UserDetailForm(),
    }
    if request.method == 'POST':
        userDetailForm = UserDetailForm(request.POST, request.FILES)
        if  userDetailForm.is_valid():
            userDetailPost = userDetailForm.save(commit=False)
            userDetailPost.login_user = userinfo
            userDetailPost.save()


        else:
            #フォームが有効でない場合
            print(userDetailForm.errors)
            return render(request, 'myApp/user_adddetail.html', context=params)
        
    return render(request, 'myApp/create_completion.html')

def showMypage(request,id):
    userinfo = get_object_or_404(login, pk=id)
    userinfoMypage = get_object_or_404(UserDetail, pk=id)
    
    context = {
        'userinfo':userinfo,
        'userinfoMypage':userinfoMypage
    }
    return render(request, 'myApp/mypage.html', context)
    

def MypageUpdate(request, id):
    userinfoMypage = get_object_or_404(UserDetail, pk=id)
    user_detail_form = UserDetailForm(instance=userinfoMypage)
    context = {
        'userinfoMypage':userinfoMypage,
        'user_detail_form':user_detail_form,
    }
    return render(request, 'myApp/mypage_update.html',context)

def updateMypage(request,id):
    if request.method == 'POST':
        userinfoMypage = get_object_or_404(UserDetail,pk=id)
        user_detail_form = UserDetailForm(request.POST, request.FILES, instance=userinfoMypage)
        if user_detail_form.is_valid():
            user_detail_form.save()


    userinfo = get_object_or_404(login, pk=id)      
    context = {
        'userinfo':userinfo,
        'userinfoMypage':userinfoMypage
    }
    
    return render(request, 'myApp/mypage.html', context)
