from django.db import models

# Create your models here.
class Users(models.model): 

    class sexType(models .IntegerField):
        male = (1, "male")
        female = (2, "female")
        other = (3, "other")

    username = models.CharField(max_length=100, null=False)
    email = models .EmailField(max_length=80)
    birth_day = models .DateField(null=False)
    password = models  .CharField(max_length=10, blank=False, 
                                  null=False)
    sex = models .IntegerField(choises=sexType.choices,
                               default=sexType.other)
    phone = models.IntegerField()