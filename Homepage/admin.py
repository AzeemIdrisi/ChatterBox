from django.contrib import admin
from .models import User, Message, Reply

# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Reply)
