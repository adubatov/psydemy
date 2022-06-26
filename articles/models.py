from django.db import models
from django.contrib.auth import get_user_model

from utilities.text_utilities import crop_text

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    published = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def body_crop(self):
        return crop_text(self.body, 500)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=1000)


# class Likes(models.Model):
#     article = models.ForeignKey(Article)
#     author = models.ForeignKey(get_user_model())