from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import MailForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def send_test_email(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            recipient_email = form.cleaned_data['recipient_email']
            recipient_list = form.cleaned_data['recipient_list']
            # 宛先が１件の場合はrecipient_listをrecipient_emailに変更
            send_mail(subject, message, from_email, [recipient_email])
            messages.success(request, 'コンソールにメールを送信しました')
            
            return redirect('home')
        else:
            messages.error('入力に誤りがあります。')
    else:
        form = MailForm()
    return render(request, 'send_test_email.html', {'form': form})