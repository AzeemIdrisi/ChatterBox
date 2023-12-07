from django.shortcuts import render, redirect
from django.urls import reverse
import random
from .models import User, Message, Reply


# Create your views here.
def homepage(request):
    if not request.session.session_key:
        request.session.create()

    messages = Message.objects.all().order_by("time")
    context = {
        "messages": messages,
    }
    return render(request, "Homepage/index.html", context)


def send_message(request):
    if not request.session.session_key:
        request.session.create()
    uid = str(request.session.session_key)[0:3]
    try:
        user = User.objects.get(uid=uid)
    except User.DoesNotExist:
        user = User.objects.create(
            uid=uid,
            gender=random.choice(["male", "female"]),
            name="anon",
        )

    text = request.POST["message"]
    if len(text) > 0:
        message = Message.objects.create(author=user)
        message.text = text
        message.save()

    return redirect(reverse("homepage") + "#home")


def send_reply(request):
    uid = str(request.session.session_key)[0:3]
    try:
        user = User.objects.get(uid=uid)
    except User.DoesNotExist:
        user = User.objects.create(
            uid=uid,
            gender=random.choice(["male", "female"]),
            name="anon",
        )

    text = request.POST["reply"]
    id = request.POST["original_message"]
    if len(text) > 0:
        message = Message.objects.get(id=id)
        reply = Reply.objects.create(author=user, original_message=message)
        reply.text = text
        reply.save()

    return redirect(reverse("homepage") + f"#m{id}")


def like(request, message_id, type):
    if type == "message":
        message = Message.objects.get(id=message_id)
        message.likes += 1
        message.save()

    else:
        reply = Reply.objects.get(id=message_id)
        reply.likes += 1
        reply.save()
    return redirect("homepage")
