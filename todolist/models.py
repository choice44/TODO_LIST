from django.db import models
from django.utils import timezone
from users.models import User


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_complete == True:
            self.completion_at = timezone.now()
        else:
            self.completion_at = None
        super().save(*args, **kwargs)
