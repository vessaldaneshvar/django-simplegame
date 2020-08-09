from django.shortcuts import render

# Create your views here.

def rock(request):
    if not 'session_game' in request.session.keys():
        request.session['session_game'] = ''

    return render(request,'rock-paper-scissor/rock.html')

def dotsbox(request):
    return render(request,'dotsbox/dotsandboxes.html')