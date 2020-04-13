from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class Chairs(models.Model):
    name_of_chair = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    head_of_chair = models.ManyToManyField(User)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name_of_chair

class Specialisations(models.Model):
    code_of_specialisation = models.CharField(max_length=100)
    name_of_specialisation = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, unique=True)
    name_of_profile = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.code_of_specialisation



class Group(models.Model):
    code_group = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    specialisation = models.ForeignKey(Specialisations, on_delete=models.CASCADE)
    chair = models.ForeignKey(Chairs, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.code_group




class TableOfEducators(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=100)
    degree = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, unique=True)
    chair = models.ForeignKey(Chairs,on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.fio





class TableOfDisc(models.Model):
    STATUS_CHOICES = (
        ('new','Новое'),
        ('sent', 'Отправлено'),
        ('approved', 'Одобрено'),
        ('denied','На доработку')
    )
    name_of_disc = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    message = models.TextField()
    specialisation = models.ForeignKey(Specialisations, on_delete=models.CASCADE)
    content = models.FileField(upload_to='media/files')
    educator = models.ForeignKey(User, on_delete=models.CASCADE)
    chair = models.ForeignKey(Chairs,on_delete=models.CASCADE, )
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='new')
    educ_comment = models.TextField()
    admin_comment = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name_of_disc




