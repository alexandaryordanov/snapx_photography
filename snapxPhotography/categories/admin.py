from django.contrib import admin

from snapxPhotography.categories.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_by', 'created_by__account']
    search_fields = ['name', 'created_by__account']
    ordering = ['name']
    list_filter = ['created_by']