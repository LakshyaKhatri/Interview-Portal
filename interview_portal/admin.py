from django.contrib import admin
from .models import (
    Technology,
    Status,
    Application,
    ApplicationDetail
)


class ApplicationInline(admin.StackedInline):
    model = ApplicationDetail


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    inlines = [ApplicationInline, ]


admin.site.register(Technology)
admin.site.register(Status)
