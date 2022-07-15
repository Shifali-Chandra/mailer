from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'django111test@gmail.com',
#     ['divyanshujain20010808@gmail.com'],
#     fail_silently=False,
# )
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['divyanshujain20010808@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "emails.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate, logout
# from django.conf import settings
# from django.core.mail import send_mail
# from stripe import Recipient

# def signup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']

#         user = User.objects.create_user(
#             username = username,
#             password = password,
#             email = email
#         )

#         login(request, user)
#         subject = 'Welcome to the app'
#         message = f'Hi {user.username}, thank you for registering in the app'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [user.email,]
#         send_mail(subject, message, email_from, recipient_list)
#         return redirect("/dashboard/")
#     return render(request, "emails.html")