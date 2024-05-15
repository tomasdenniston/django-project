from django.contrib import admin

from polls.models import Awnser, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Awnser)