# coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/4/15 11:43'
from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile


# 这些表单都是限制前端提交数据的
# 　ｒｅｑｕｉｒｅ是要求必填
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UpLoadImageForm(forms.ModelForm):
    # model中image字段已经存在,所以继承,使用ModelForm
    class Meta:
        model = UserProfile
        fields = ['image']


# 个人信息页面的表单
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birday', 'address', 'mobile']
