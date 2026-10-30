from django.db import models

# Create your models here.
class Kurs(models.Model): #yaml
    title = models.CharField(max_length=100, verbose_name="название",
                             help_text="Внутренне название предмета")
    name = models.JSONField(default=list, verbose_name="ключевые слова",
                            help_text="Ключевые слова для поиска дисциплины в РУП")
    authors = models.JSONField(default=list)
    year = models.IntegerField()
    objective = models.CharField(max_length=100)
    knowledge = models.CharField(max_length=100)
    ability = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    link = models.JSONField(default=list)
    themes = models.JSONField(default=dict)
    controll = models.JSONField(default=dict)
    books = models.JSONField(default=dict)
    additional_books = models.JSONField(default=dict)
    resources = models.JSONField(default=dict)
    software = models.JSONField(default=dict)
    libraries = models.JSONField(default=dict)

    def __str__(self):
        return self.title
    


class Rup(models.Model): #plx

    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to="documents")

    def save(self, *args, **kwargs):
        res = super().save(*args, **kwargs)
        #TODO  прочитать руп и создать новый subject 
        return res
    #TODO печать subject'ов
class Subject(models.Model):
    #rup = models.ForeignKey("Rup")
    title = models.CharField(max_length=100)
    semesters = models.CharField()
    competencies = models.CharField()
    hours = models.IntegerField()
    controls = models.JSONField()
    credits = models.IntegerField()
    credits = models.IntegerField()
#TODO создать таблицу для дисциплин учебного плана