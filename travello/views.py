from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City that never sleeps'
    # dest1.price = 'koi kimat nhi laga sakta appni'
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False
    # dest2 = Destination()
    # dest2.name = 'Coimbatore'
    # dest2.desc = 'Is this even a city'
    # dest2.price = 'apun phukat hai'
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True

    # dests = [dest1,dest2]
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dest':dests})
