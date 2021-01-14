from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import os
from django.db.models import Sum

# Create your models here.
is_finished = (
    ('Yes','Yes'),
    ('No','No'),
)
rating = (
    (0,'0'),
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
    (6,'6'),
    (7,'7'),
    (8,'8'),
    (9,'9'),
    (10,'10'),
)
def profile_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "profile_%s.%s" % (instance.id, ext)
    return os.path.join('profile_images', filename)
class Todo(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    is_finished = models.CharField(default='No',max_length=3,choices=is_finished, null=True, blank=True)
    rate = models.IntegerField(default=0,choices=rating, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    class Meta:
        verbose_name_plural = "Todo"

    def __str__(self):
        return self.task
    def clean(self):
        self.task = self.task.capitalize()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to=profile_img,null=True, blank=True)
    membership_day = models.CharField(default=0,max_length=2)
    membership = models.CharField(default="Normal",max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def t_rate(self):
        get_tasks = Todo.objects.filter(user=self.user,is_finished="Yes")
        get_tasks_count = Todo.objects.filter(user=self.user,is_finished="Yes").count()
        get_tasks_count = get_tasks_count*10
        total = sum([r.rate for r in get_tasks]) / get_tasks_count * 100
        return total
    class Meta: 
        verbose_name_plural = "User Profile"
    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
