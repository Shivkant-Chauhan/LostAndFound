from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "lostfound/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "lostfound/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "lostfound/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def new_item(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        email += "@iiitdmj.ac.in"
        mobileNumber = request.POST["mobileNumber"]
        rollNumber = request.POST["rollNumber"]
        roomNumber = request.POST["roomNumber"]
        title = request.POST["title"]
        description = request.POST["description"]
        category = Category.objects.get(title=request.POST["category"])

        image = request.FILES.get('image')

        it = item(person_first_name = firstName, person_last_name = lastName, email = email, phone_number = mobileNumber, roll_number = rollNumber, room_number = roomNumber, title = title, description = description, category=category, image=image, lost_by=request.user)

        it.save()
        Category.objects.get(title=category).items.add(it)

        return HttpResponseRedirect(reverse("item", args=[str(it.id)]))

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, "lostfound/itemform.html", {
        "categories": Category.objects.all(), 
    })

def category_view(request, category):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    category = Category.objects.get(title=category)
    items = category.items.all()
    return render(request, "lostfound/category.html", {
        "category": category,
        "items": items,
    })


def item_view(request, item_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    lost_item = item.objects.get(pk=item_id)
    return render(request, "lostfound/item.html", {
        "item": lost_item,
    })

def my_requests(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    items = request.user.lost.all()

    return render(request, "lostfound/my_requests.html", {
        "items": items
    })

def found(request):
    if request.method == "POST":
        entry = item.objects.filter(pk=request.POST["id"])
        entry.delete()
        return HttpResponseRedirect(reverse('my_requests'))
