from django.db import models

class BookTable(models.Model):
    bookname = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)

class libUsers(models.Model):
    question = models.ForeignKey(BookTable, on_delete=models.CASCADE)
    u_name = models.CharField(max_length=200)
# this is for model
