
from django.db import models


class Mypage(models.Model):
    post = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_done = models.BooleanField(default=False)
