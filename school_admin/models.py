from django.db import models

# Create your models here.


class Teachers(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email =  models.CharField(max_length=50, unique=True)
    phone = models.BigIntegerField()
    roomNo = models.IntegerField()
    image = models.ImageField(upload_to='images')
    password = models.CharField(max_length=20)
    permission = models.BooleanField(default=False)


class Subject(models.Model):
    subject = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("subject", "teacher")


