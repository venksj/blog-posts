from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, verbose_name="Blog Title")
    text = models.TextField(max_length=2000, verbose_name="Body")
    created_date = models.DateField(default=timezone.now, verbose_name="Created On")
    published_date = models.DateField(blank=True, null=True, verbose_name="Published On")

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


