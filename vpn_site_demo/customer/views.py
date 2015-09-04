from django.shortcuts import render, render_to_response
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect 
from django.template import RequestContext

from forms import LoginForm, SignUpForm, CreditsForm

def home_page(request):
	return render_to_response('home_page.html')

class LoginFormView(FormView):
	template_name = "login.html"
	form_class = LoginForm
def login(request):
    return render_to_response('login.html')

class SingUpFormView(FormView):
	template_name = "sign_up.html"
	form_class = SignUpForm 
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return  HttpResponseRedirect('/home/')
    else:
        form = UserCreationForm()
    return render_to_response('registration/register.html',{'form': form,}, context_instance=RequestContext(request))
	
class CreditsFormView(FormView):
	template_name = "credits.html"
	form_class = CreditsForm 
