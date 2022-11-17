from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class TextConverter(models.Model):
    body=RichTextField(blank=True,null=True)