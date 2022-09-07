from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
# Create your views here.


def contactView(request):
	form=ContactForm()
	if request.method == "POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			subject=form.cleaned_data['subject']
			from_email=form.cleaned_data['from_email']
			message=form.cleaned_data['message']

			try:
				send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
			except BadHeaderError:
				return HttpResponse('invalid header found.')
			return redirect ('success')
	return render (request, 'email.html', {"form":form})



def successView(request):
    return HttpResponse("Success! Thank you for your message.")

# Quick note. i imported setting from django.conf to access my EMAIL_HOST_USER This is because 
# i wanted to send this mail to the same email. You can remove the setting.EMAIL_HOST_USER,
# and include any valid email of your choice. it mustn't be the one included in your backend code