from django.shortcuts import render
from .models import State, National, Professional
# Create your views here.
def main(request):
    state = State.objects.all()
    return render(request, 'red_letter_day/main.html', {'info': state})

def state(request):
    state = State.objects.all()
    return render(request, 'red_letter_day/state.html', {'info': state})

def national(request):
    national = National.objects.order_by('-on_date')
    return render(request, 'red_letter_day/national.html', {'info': national})

def professional(request):
    professional = Professional.objects.all()
    return render(request, 'red_letter_day/professional.html', {'info': professional})