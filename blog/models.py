from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#manager
class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISH)

class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.DRAFT)

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DR" , "Draft"
        PUBLISH = "PB" , "Publish"
        REJECTED = "RC" , "Reject"
    author = models.ForeignKey(User , on_delete=models.CASCADE, related_name ="user_postes" , verbose_name="نویسنده")
    title = models.CharField(max_length=250,verbose_name="عنوان")
    discription = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add =True)
    updeted = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2 , choices=Status.choices , default= Status.DRAFT , verbose_name="وضعیت")
    objects= models.Manager()
    published = PublishManager()
    draft = DraftManager()

    class Meta:
        ordering = ['-publish']
        indexes =[
             models.Index(fields=['-publish'])
         ]
        verbose_name  ="پست"
        verbose_name_plural = "پست ها"
    def get_absolute_url(self):
        return reverse("blog:post_detail" , args=[self.id])


    def __str__(self):
        return self.title
class Ticket(models.Model):
    massage = models.TextField(verbose_name="متن پیام"  )
    email = models.EmailField(max_length=250 , verbose_name="ایمیل")
    phone = models.CharField(max_length=250 , verbose_name="شماره تماس")
    name = models.CharField(max_length=250 , verbose_name=" نام")
    subject = models.CharField(max_length=250 , verbose_name=" موضوع تیکت")


class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name="comments" , verbose_name="پست")
    name = models.CharField(max_length=250)
    massage = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return self.massage
