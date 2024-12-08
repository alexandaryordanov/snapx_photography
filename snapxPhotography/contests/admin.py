from django.contrib import admin
from snapxPhotography.contests.models import Contest


# Register your models here.
@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('name', 'requirements', 'award', 'deadline', 'category', 'created_by__account')
    list_filter = ('award', 'deadline', 'category')