from django.contrib import admin
from models import Diseases, Symptoms

# Register your models here.
class SymptomsInLine(admin.TabularInline):
    model = Symptoms
    extra = 3
    
class DiseasesAdmin(admin.ModelAdmin):
    list_display = ('diseases',)
    search_fields = ['question_text']

    inlines = [SymptomsInLine]
    
admin.site.register(Diseases, DiseasesAdmin)
admin.site.register(Symptoms)