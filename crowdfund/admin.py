from django.contrib import admin
from crowdfund.models import Farm, Project, PManager, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']


@admin.register(PManager)
class PManagerAdmin(admin.ModelAdmin):
    
    list_display = ['manager', 'role']
    raw_id_fields = ['manager',]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'project_manger', 'category', 'duration', 'location'
    ]
    search_fields = ['name', 'location', 'project_manger']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = [
        'insured', 'units', 'unit_in_stock', 'price_per_unit',
        'roi', 'start_date', 'end_date'
    ]


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'project_manger', 'category', 'duration', 'location'
    ]
    search_fields = ['name', 'location', 'project_manger']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = [
        'insured', 'units', 'unit_in_stock', 'price_per_unit',
        'roi', 'start_date', 'end_date'
    ]
