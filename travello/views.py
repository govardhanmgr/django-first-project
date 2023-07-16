from django.shortcuts import render
from .models import Destination

# Create your views here.



def index(request):

	dest1 = Destination()
	dest1.name = "Hyderbad"
	dest1.desc = "Dum Biryani"
	dest1.img= "destination_1.jpg"
	dest1.offer = True
	dest1.price = 700

	dest2 = Destination()
	dest2.name = "Mumbai"
	dest2.desc = "City Never Sleeps"
	dest2.img= "destination_2.jpg"
	dest2.offer = False
	dest2.price = 650

	dest3 = Destination()
	dest3.name = "Bangalore"
	dest3.desc = "Smart City"
	dest3.img= "destination_3.jpg"
	dest3.offer = False
	dest3.price = 800

	dests = [dest1, dest2, dest3]

	return render(request, "index.html", {'dests':dests})
