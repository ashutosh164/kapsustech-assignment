from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    # def __int__(self):
    #     return self.id


class Marks(models.Model):
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField()
    subj = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.std_id} -- {self.mark} -- {self.subj}'



