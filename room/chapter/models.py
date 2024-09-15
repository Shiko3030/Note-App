from django.db import models



class Techers(models.Model):
    status=(
        ('Male','Male'),
        ('Female','Female'),
    )
    Specialization_choices=(
        ('Science','Science'),
        ('Mathematics','Mathematics'),
        ('Arabic','Arabic'),
        ('English','English'),
        ('history','history'),
        ('sport','sport'),
        ('Programming','Programming'),
    )
    name = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50,null=True)
    adress = models.CharField(max_length=50)
    type = models.CharField(max_length=50,choices=status)
    specialization = models.CharField(max_length=50,choices=Specialization_choices, null=True)
    email= models.EmailField()
    phone = models.CharField(max_length=50 ,null=True)
    salary=models.FloatField(null=True)

    def __str__(self):
        
        return self.name
            

# Create your models here.

class Students(models.Model):
    status=(
        ('Male','Male'),
        ('Female','Female'),
    )
    STAGE=(
        ('Primary','Primary'),
        ('Middle ','Middle '),
        ('Secondary','Secondary'),
    )
    payment_status=(
        ('Paid','Paid'),
        ('Not Paid','Not Paid'),
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50,choices=status)
    adress = models.CharField(max_length=50)
    stage = models.CharField(max_length=50,choices=STAGE)
    class_Room = models.CharField(max_length=50,null=True)
    amount = models.FloatField(null=True)
    payment_status=models.CharField(max_length=50,choices=payment_status,null=True)
    birthday = models.CharField(max_length=50,null=True)
    def __str__(self):
        
        return self.name
    






