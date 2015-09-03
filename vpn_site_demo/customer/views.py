from django.shortcuts import render, render_to_response
from django.views.generic import FormView

from forms import LoginForm, SignUpForm, CreditsForm

def home_page(request):
	return render_to_response('home_page.html')

class LoginFormView(FormView):
	template_name = "login.html"
	form_class = LoginForm

class SingUpFormView(FormView):
	template_name = "sign_up.html"
	form_class = SignUpForm 
	
class CreditsFormView(FormView):
	template_name = "credits.html"
	form_class = CreditsForm 
