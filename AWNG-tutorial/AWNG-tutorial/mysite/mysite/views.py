
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def toPolls(request):
    return HttpResponseRedirect(reverse('polls:index'))