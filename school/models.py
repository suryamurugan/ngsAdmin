from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import calendar

# Create your models here.

class Student(models.Model):
    s_no = models.IntegerField(primary_key=True,unique=True)
    student_name = models.CharField(max_length=41, blank=True, null=True)
    father_name = models.CharField(max_length=41, blank=True, null=True)
    mother_name = models.CharField(max_length=40, blank=True, null=True)
    contact_number = models.CharField(max_length =30,)

    CLASS_CHOICES = [
        ('LKG', 'LKG'),
        ('UKG', 'UKG'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('NC', 'NC'),
        ('PNC', 'PNC'),
        ('NR', 'NR'),
    ]
    class_std = models.CharField( max_length=10,
        choices=CLASS_CHOICES,
        )
    CATEGORY_CHOICES = [
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('GENERAL', 'GENERAL'),
    ]
    category = models.CharField( max_length=10,
        choices=CATEGORY_CHOICES,
        )
    BLOODGROUP_CHOICES = [
        ('A', 'A'),
        ('A+', 'A+'),
        ('B', 'B'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = models.CharField( max_length=10,
        choices=BLOODGROUP_CHOICES,
        )
    conveyance = models.BooleanField()
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.student_name)
    


class TutionAdmissionFee(models.Model):
    student =  models.ForeignKey(Student,on_delete=models.SET_NULL,null=True) 
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
    tution_fee = models.IntegerField('Tution Fee')
    admission_fee = models.IntegerField('Admission Fee')
    conveyance_fee =  models.IntegerField('IntegerField')
    def __str__(self):
        return "{}".format(self.student)
