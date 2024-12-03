from django.contrib import admin

from snapxPhotography.common.models import Vote


# Register your models here.
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user__account', 'photo', 'created_at')
    list_filter = ('created_at',)
