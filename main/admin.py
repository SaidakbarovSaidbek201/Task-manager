from django.contrib import admin
from .models import Books
from .models import Vazifa


admin.site.register(Vazifa)


class CustomKitob(admin.ModelAdmin):
    list_display = ('name', 'mualif', 'year', 'janri')
    list_filter = ('year', 'janri')
    search_fields = ('name', 'mualif', 'janri')
    date_hierarchy = 'year'

admin.site.register(Books, CustomKitob)

