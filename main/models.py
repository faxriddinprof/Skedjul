from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title=models.TextField()
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateField(auto_now_add=True)
    holati=models.BooleanField(default=False)



    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])