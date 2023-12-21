# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils import timezone


# # Create your models here.

# class Client(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# # class Notification(models.Model):
# #     admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
# #     message = models.CharField(max_length=255)
# #     created_at = models.IntegerField(default=int(timezone.now().timestamp()), editable=False)

# # @receiver(post_save, sender=Client)
# # def send_notification(sender, instance, **kwargs):
# #     admin_user = User.objects.get(username='admin')  # Replace 'admin' with your admin username
# #     Notification.objects.create(admin=admin_user, message=f'New client registered: {instance.user.username}')

# #     subject = 'New Client Registration'
# #     message = f'A new client has registered: {instance.user.username}'
# #     from_email = 'sruthi20699@gmail.com'  # Replace with your email
# #     to_email = 'sruthipillai06@gmail.com'   # Replace with admin's email
# #     send_mail(subject, message, from_email, [to_email])


# class Notification(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
#     recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notification')
#     message = models.TextField()
#     created_at = models.IntegerField(default=int(timezone.now().timestamp()), editable=False)

#     def __str__(self):
#         return f'{self.sender.username} -> {self.recipient.username} : {self.message}'


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notifications')
    message = models.TextField()
    created_at = models.IntegerField(default=int(timezone.now().timestamp()), editable=False)

    def __str__(self):
        return f'{self.sender.username} -> {self.recipient.username} : {self.message}'




