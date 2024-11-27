from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'is_done', 'get_tags')
    list_filter = ('is_done', 'tags')
    search_fields = ('content',)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'

admin.site.register(Tag)
