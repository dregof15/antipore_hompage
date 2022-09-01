import email
from django.db import models


class Customer(models.Model):
    name = models.TextField()
    mail = models.TextField()

    def __str__(self):
        return self.name
# Customer object (1)... 같은 내용 대신 name의 내용이 출력되게 변경.
