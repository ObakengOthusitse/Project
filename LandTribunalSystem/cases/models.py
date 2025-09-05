from django.db import models


class Case(models.Model):
    case_number = models.CharField(max_length=50, unique=True)
    date_receipt = models.DateField()
    appellant_name = models.CharField(max_length=100)
    respondent_name = models.CharField(max_length=100)
    subject = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.case_number
