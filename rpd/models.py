from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


def image_folder(instance, filename):
    filename = instance.slug +'.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class Chairs(models.Model):
    name_of_chair = models.CharField(max_length=100, verbose_name="Название кафедры")
    slug = models.SlugField(max_length=200, unique=True)
    head_of_chair = models.ManyToManyField(User, verbose_name="Заведущий кафедрой")


    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица кафедр'
        verbose_name_plural = 'Таблица кафедр'

    def __str__(self):
        return self.name_of_chair

class Specialisations(models.Model):
    code_of_specialisation = models.CharField(max_length=100, verbose_name="Код специализации")
    name_of_specialisation = models.CharField(max_length=1000, verbose_name="Наименование специализации")
    slug = models.SlugField(max_length=200, unique=True)
    name_of_profile = models.CharField(max_length=100, verbose_name="Наименование профиля")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица специализаций'
        verbose_name_plural = 'Таблица специализаций'

    def __str__(self):
        return self.code_of_specialisation



class Group(models.Model):
    code_group = models.CharField(max_length=50, verbose_name="Код группы")
    slug = models.SlugField(max_length=200, unique=True)
    specialisation = models.ForeignKey(Specialisations, on_delete=models.CASCADE, verbose_name="Специализация")
    chair = models.ForeignKey(Chairs, on_delete=models.CASCADE, verbose_name="Кафедра")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица групп'
        verbose_name_plural = 'Таблица групп'

    def __str__(self):
        return self.code_group




class TableOfEducators(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Логин")
    image = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Фотография преподователя")
    fio = models.CharField(max_length=100, verbose_name="ФИО")
    degree = models.CharField(max_length=1000, verbose_name="Достижения")
    slug = models.SlugField(max_length=200, unique=True)
    chair = models.ForeignKey(Chairs,on_delete=models.CASCADE, verbose_name="Кафедра")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица преподавателей'
        verbose_name_plural = 'Таблица преподавателей'

    def __str__(self):
        return self.fio





class TableOfDisc(models.Model):
    STATUS_CHOICES = (
        ('Новое','Новое'),
        ('Отправлено', 'Отправлено'),
        ('Одобрено', 'Одобрено'),
        ('На доработку','На доработку')
    )
    name_of_disc = models.CharField(max_length=100, verbose_name="Наименование дисциплины")
    slug = models.SlugField(max_length=200, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    message = models.TextField(null=True,blank=True, verbose_name="Сообщение")
    specialisation = models.ForeignKey(Specialisations, on_delete=models.CASCADE, verbose_name="Специализация")
    content = models.FileField(upload_to='files',null=True,blank=True, verbose_name="Файл с РПД")
    educator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Логин преподавателя")
    chair = models.ForeignKey(Chairs,on_delete=models.CASCADE, verbose_name="Кафедра" )
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Новое', verbose_name="статус")
    educ_comment = models.TextField(null=True,blank=True, verbose_name="Комментарий преподавателя")
    admin_comment = models.TextField(null=True,blank=True, verbose_name="Комментарий администратора")

    class Meta:
        ordering = ['id']
        verbose_name = 'Таблица дисциплин'
        verbose_name_plural = 'Таблица дисциплин'

    def __str__(self):
        return self.name_of_disc




