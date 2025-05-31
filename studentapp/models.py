from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    maths_score = models.IntegerField()
    physics_score = models.IntegerField()
    computer_score = models.IntegerField()
    total_score = models.IntegerField(editable=False)

    def save(self, *args, **kwargs ):
        self.total_score = self.maths_score+self.physics_score+self.computer_score
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name