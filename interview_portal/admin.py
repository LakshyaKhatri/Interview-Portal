from django.contrib import admin
from .models import (
    Technology,
    Status,
    Application,
    ApplicationDetail
)


class ApplicationDetailInline(admin.StackedInline):
    model = ApplicationDetail


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    inlines = [ApplicationDetailInline, ]


admin.site.register(Technology)
admin.site.register(Status)
