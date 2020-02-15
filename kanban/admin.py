from django.contrib import admin
from .models import *

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CardAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(List, ListAdmin)
admin.site.register(Card, CardAdmin)


