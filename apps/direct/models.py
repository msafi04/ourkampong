#https://www.youtube.com/watch?v=YYSx4xD7wfE&list=PL9tgJISrBWc5619CclyqYrnnMkVOPzVYM&index=18
from django.db import models
from django.db.models import Max

from apps.member.models import Member

class Message(models.Model):
    user = models.ForeignKey(Member, related_name = 'user', on_delete = models.CASCADE)
    sender = models.ForeignKey(Member, related_name = 'from_user', on_delete = models.CASCADE)
    receiver = models.ForeignKey(Member, related_name = 'to_user', on_delete = models.CASCADE)
    body = models.TextField(max_length = 1000, blank = True, null = True)
    date = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default = False)

    def send_message(from_user, to_user, body):

        sender_message = Message(
            user = from_user,
            sender = from_user,
            receiver = to_user,
            body = body,
            is_read = True
        )
        sender_message.save()

        receiver_message = Message(
                user = to_user,
                sender = from_user,
                receiver = from_user,
                body = body
        )
        receiver_message.save()

        return sender_message

    def get_messages(user):
        users = []
        messages = Message.objects.filter(user = user).values('receiver').annotate(last = Max('date')).order_by('-last')
        for message in messages:
            users.append({
                'user': Member.objects.get(pk = message['receiver']),
                'last': message['last'],
                'unread': Message.objects.filter(user = user, receiver__pk = message['receiver'], is_read = False).count()
            })
        return users

