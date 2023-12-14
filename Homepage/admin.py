from django.contrib import admin
from .models import User, Message, Reply

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "uid",
        "message_count",
        "last_message_time",
    ]

    def message_count(self, obj):
        return obj.message_set.count() + obj.reply_set.count()

    def last_message_time(self, obj):
        last_message = obj.message_set.last()
        return last_message.time if last_message else None


admin.site.register(User, UserAdmin)
admin.site.register(Message)
admin.site.register(Reply)
