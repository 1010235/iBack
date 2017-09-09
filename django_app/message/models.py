from django.db import models


# Create your models here.

class Number(models.Model):
    number = models.IntegerField()


class Message(models.Model):
    number = models.ForeignKey(Number, on_delete=models.CASCADE)
    msg = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_date',)
