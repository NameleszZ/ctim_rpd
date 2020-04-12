from django.contrib import admin
from .models import TableOfEducators, Chairs, Specialisations, Group, TableOfDisc


@admin.register(TableOfEducators)
class TableOfEducatorsAdmin(admin.ModelAdmin):
    list_display = ['fio', 'slug']
    prepopulated_fields = {'slug': ('fio',)}
    search_fields = ['fio']


@admin.register(Chairs)
class ChairsAdmin(admin.ModelAdmin):
    list_display = ['name_of_chair', 'slug']
    prepopulated_fields = {'slug': ('name_of_chair',)}
    search_fields = ['name_of_chair']


@admin.register(Specialisations)
class SpecialisationsAdmin(admin.ModelAdmin):
    list_display = ['name_of_specialisation', 'slug']
    prepopulated_fields = {'slug': ('name_of_specialisation',)}
    search_fields = ['specialisation']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['code_group', 'slug']
    prepopulated_fields = {'slug': ('code_group',)}
    search_fields = ['code_group']


@admin.register(TableOfDisc)
class TableOfDiscAdmin(admin.ModelAdmin):
    list_display = ['name_of_disc', 'slug']
    prepopulated_fields = {'slug': ('name_of_disc',)}
    search_fields = ['name_of_disc']