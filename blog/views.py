from django.shortcuts import render,redirect
from .models import Contestant,Vote
# Create your views here.
from django.http import HttpResponse


def index(request):
    conts = Contestant.objects.all()
    total=0
    for c in conts:
        total = total + c.votes
    return render(request,'blog/home.html',{'conts':conts,'total':total})

def vote(request,pk=None):
    c = Contestant.objects.get(pk=pk)
    vote = c.votes + 1
    Contestant.objects.filter(pk=pk).update(votes=vote)
    return redirect('/blog')
