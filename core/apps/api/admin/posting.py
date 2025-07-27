from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import PostingModel


@admin.register(PostingModel)
class PostingAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
