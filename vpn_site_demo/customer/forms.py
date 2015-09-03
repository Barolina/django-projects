# -*- coding: utf-8 -*-

from django import forms

RADIO_CHOCIES = (
	('1', '学生'),
	('2', '老师'),
) 

class SignUpForm(forms.Form):
	realName = forms.CharField(max_length=100, label="真实姓名")
	email = forms.EmailField(label = "学校邮箱")
	cardID = forms.CharField(max_length=100, label="学号/教工号")
	shenfen = forms.ChoiceField(choices=RADIO_CHOCIES,label="身份")
	password = forms.CharField(widget=forms.PasswordInput, label="密码")	

class LoginForm(forms.Form):
	email = forms.EmailField(label = "学校邮箱")
	password = forms.CharField(widget=forms.PasswordInput, label="密码")	
class CreditsForm(forms.Form):
	email = forms.EmailField(label = "学校邮箱")
	password = forms.CharField(widget=forms.PasswordInput, label="密码")	
