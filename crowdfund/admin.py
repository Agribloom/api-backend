from django.contrib import admin
from crowdfund.models import Farm, FarmManager, Category, Update


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(FarmManager)
class FarmManagerAdmin(admin.ModelAdmin):
    
    list_display = ['manager', 'role']
    raw_id_fields = ['manager',]



@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):

    list_display = [
        'name', 'manger', 'category', 'duration', 'location'
    ]
    search_fields = ['name', 'location', 'manger']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = [
        'insured', 'units', 'unit_in_stock', 'price_per_unit',
        'roi', 'start_date', 'end_date'
    ]
    raw_id_fields = ['manger']

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    
    list_display = ['activity']
    prepopulated_fields = {"slug": ("activity",)}

