from django.contrib import admin

from .models import Kurs, Rup, Subject
# Register your models here.
@admin.action(description="Greet")
def greeting(modeladmin,request,queryset):
    queryset.update(body="Hello")

class KursAdmin(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["title"]
    actions = [greeting]
class RupAdmin(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["title"]
    actions=[]
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["title"]
    ordering = ["title"]
    actions=[]
admin.site.register(Kurs,KursAdmin)
admin.site.register(Rup,RupAdmin)
#TODO: цвета поменять