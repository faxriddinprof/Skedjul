from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title=models.TextField()
    # author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text=models.TextField()
    # sana=models.DateField(auto_now_add=True)
    date=models.DateField()
    holati=models.BooleanField(default=False)

    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])
    
    def clean(self):
        super().clean()
        if self.date < timezone.now().date():
            raise ValidationError({'date': "Sana bugungi kundan oldin bo'lishi mumkin emas."})