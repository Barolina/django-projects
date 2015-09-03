from django.core.mail import send_mail
from django.template.loader import get_template
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.template import Context, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from books.models import Book
from yunfeng_site.forms import ContactForm
import datetime 

def hello(request):
	return HttpResponse('Hello,world')

def home_view(request):
	return HttpResponse('Welcome to yunfeng\'s site!')

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):

	try: 
		offset = int(offset)
	except ValueError:
		raise Http404()
	
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def test_bootstrap(request):
	return render_to_response('test_bootstrap.html')

def ua_display_1(request):
	try:
		ua = request.META['HTTP_USER_AGENT']
	except KeyError:
		ua = 'unknown'
	return HttpResponse('Your browser is %s'% ua)

def display_meta(request):
	data = request.META.items()
	data.sort()
	html = []
	for k,v in data:
		html.append('<tr><td>%s</td><td>%s</td></tr>'% (k,v))
	return HttpResponse('<table>%s</table>'%'\n'.join(html))

def display_meta_2(request):
	data = request.META.items()
	data.sort()
	return render_to_response('display_meta_2.html', {'data': data})

def display_post(request):
	data = request.POST.items()
	data.sort()
	html = []
	for k,v in data:
		html.append('<tr><td>%s</td><td>%s</td></tr>'% (k,v))
	return HttpResponse('<table>%s</table>'%'\n'.join(html))

def display_get(request):
	data = request.GET.items()
	data.sort()
	html = []
	for k,v in data:
		html.append('<tr><td>%s</td><td>%s</td></tr>'% (k,v))
	return HttpResponse('<table>%s</table>'%'\n'.join(html))

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	errors = [] 
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Please input a search item.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_result.html', {'books': books, 'query': q})
	
	return render_to_response('search_form.html', {'errors': errors})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)	
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(	
				cd['subject'],
				cd['message'],
				cd.get('email','noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			## set initial value for subject
			initial={'subject': 'I love your site!'}
		)
	return render_to_response('contact_form.html', {'form': form}, context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('thanks.html')

class ContactFormView(FormView):
	template_name = 'contact_form_bootstrap.html'
	form_class = ContactForm


