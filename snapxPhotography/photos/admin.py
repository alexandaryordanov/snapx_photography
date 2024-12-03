from django.contrib import admin

from snapxPhotography.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'contest', 'uploaded_at', 'uploaded_by__account', 'vote')
    list_filter = ('uploaded_at', )
