# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm

RADIO_CHOCIES = (
	('1', '学生'),
	('2', '老师'),
) 

class SignUpForm(UserCreationForm):
	realName = forms.CharField(max_length=100, label="真实姓名")
	email = forms.EmailField(label = "USTC 邮箱地址")
	cardID = forms.CharField(max_length=100, label="学号/工资号")
	shenfen = forms.ChoiceField(choices=RADIO_CHOCIES,label="身份选择")

class LoginForm(forms.Form):
	email = forms.EmailField(label = "学校邮箱")
	password = forms.CharField(widget=forms.PasswordInput, label="密码")	
class CreditsForm(forms.Form):
	email = forms.EmailField(label = "学校邮箱")
	password = forms.CharField(widget=forms.PasswordInput, label="密码")	
