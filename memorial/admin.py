from django.contrib import admin
from memorial.models import Memorias

# Register your models here.
class ListandoMemorias(admin.ModelAdmin):

    list_display = ("id", "nome")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")
    list_per_page = 30

admin.site.register(Memorias, ListandoMemorias)