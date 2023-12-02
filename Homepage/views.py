from django.shortcuts import render, redirect
from django.urls import reverse
import random
from .models import User, Message


# Create your views here.
def homepage(request):
    messages = Message.objects.all().order_by("time")
    context = {
        "messages": messages,
    }
    return render(request, "Homepage/index.html", context)


def send_message(request):
    uid = str(request.session.session_key)[:2]
    try:
        user = User.objects.get(uid=uid)
    except User.DoesNotExist:
        user = User.objects.create(
            uid=uid,
            gender=random.choice(["male", "female"]),
            name="lkdlkj",
        )
        # user.save()

    text = request.POST["message"]
    if len(text) > 0:
        message = Message.objects.create(author=user)
        message.text = text
        message.save()

    return redirect(reverse("homepage") + "#bottom")
