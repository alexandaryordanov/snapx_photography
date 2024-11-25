from django.contrib import admin

from snapxPhotography.categories.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_by']
    search_fields = ['name', 'created_by']
    ordering = ['name']