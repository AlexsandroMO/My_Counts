from django.contrib import admin
from .models import Task, TypeTask

class ListaTask(admin.ModelAdmin):
    list_display = ('type_task','name','description','varcont','done','create_at','update_at')

admin.site.register(TypeTask)
admin.site.register(Task, ListaTask)


