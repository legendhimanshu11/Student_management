from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"