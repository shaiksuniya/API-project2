from django.db import models

# Create your models here.
class product_category(models.Model):
    pcname=models.CharField(max_length=100)
    pcid=models.PositiveIntegerField()


    def __str__(self):
        return self.pcname



class product(models.Model):
    pcname=models.ForeignKey(product_category,on_delete=models.CASCADE)
    pid=models.PositiveIntegerField()
    pname=models.CharField(max_length=100)
    pprice=models.DecimalField(max_digits=8,decimal_places=2)
    Pdate=models.DateField()
    


    def __str__(self):
        return self.pname