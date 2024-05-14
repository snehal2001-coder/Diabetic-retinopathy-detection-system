from django.db import models

# Create your models here.

class newuser(models.Model):
    Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)


# class Predict(models.Model):
#     dname=models.CharField(max_length=120)


class Prediction(models.Model):
    class_choices = (
        ('no_dir', 'No Diabetic Retinopathy'),
        ('mild', 'Mild Diabetic Retinopathy'),
        ('moderate', 'Moderate Diabetic Retinopathy'),
        ('sever', 'Severe Diabetic Retinopathy'),
        ('proliferative', 'Proliferative Diabetic Retinopathy'),
    )
    result = models.CharField(choices=class_choices, max_length=20)
    accuracy = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)