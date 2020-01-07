from django.shortcuts import render
# from django.http import HttpResponse
# from . import templates
from .models import userdb
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def new_user(request):
	if request.method=='POST':

		db= userdb()
		db.email_id = request.POST.get("Email_id")
		db.First_Name= request.POST.get("First_Name")
		db.LAst_Name = request.POST.get("Last_Name")
		db.save()
		subject = "You are registered"
		message = "Hi Thank you for registering"
		from_email = settings.EMAIL_HOST_USER
		to_list = [db.email_id, from_email]
		send_mail(subject, message, from_email, to_list, fail_silently=True)
		messages.success(request, "Thanks")

		return render(request, 'email_id_collection/sign_up_page.html')

	else:
		return render(request, 'email_id_collection/sign_up_page.html')
	# return HttpResponse("Hi I am shiv")
