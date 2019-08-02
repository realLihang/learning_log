from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """注销用户"""
    LogoutView(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreation()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登陆，再重定向到主页
            authenticated_user = auth.authenticate(username=new_user.username,
                    password=request.POST['password1'])
            auth.login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
