from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.conf import settings
from django.template.loader import render_to_string 
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def contactView(request):
	form=ContactForm()
	if request.method == "POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			subject=form.cleaned_data['subject']
			from_email=form.cleaned_data['from_email']
			message=form.cleaned_data['message']
			email_template_name="custom-msg.html"
			email = render_to_string(email_template_name)

			try:
				send_mail(subject, email, from_email, [settings.EMAIL_HOST_USER])
			except BadHeaderError:
				return HttpResponse('invalid header found.')
			return redirect ('success')
	return render (request, 'email.html', {"form":form})



def successView(request):
    return HttpResponse("Success! Thank you for your message.")

# Quick note. i imported setting from django.conf to access my EMAIL_HOST_USER This is because 
# i wanted to send this mail to the same email. You can remove the setting.EMAIL_HOST_USER,
# and include any valid email of your choice. it mustn't be the one included in your backend code


# working on  a like button using AJAX

def posts(request):
	posts=Post.objects.all()
	return render(request, 'posts.html', {'posts':posts})

def postdetail(request, pk):
	post=Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post':post})

@csrf_exempt
@ login_required
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            # post.like_count -= 1
            # result = post.like_count
            result = post.total_likes
           
            post.save()
        else:
            post.likes.add(request.user)
            # post.like_count += 1
            # result = post.like_count
            # using my model property instead
            result = post.total_likes
            post.save()

        return JsonResponse({'result': result, })
