from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["inserted_at", "updated_at"]
    list_display = ["summary", "author", "inserted_at", "updated_at"]

    def summary(self, obj: models.Post):
        return str(obj.content)[:10] + "..."
