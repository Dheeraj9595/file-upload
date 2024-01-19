from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    PDF = models.FileField(upload_to='books/pdfs')  # File_Upload_Class\media
    coverpage = models.ImageField(upload_to='cover', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'

