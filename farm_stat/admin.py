from django.contrib import admin
from farm_stat.models import Testimony, Achievement, Partner


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):

    list_display = ['name', 'title']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = ['name', 'value']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = ['name']
