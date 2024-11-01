from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin class for CollaborateRequest model.
    Customizes the admin interface for CollaborateRequest objects by
    displaying the 'message' and 'read' status in the admin list view.
    """
    list_display = ('message', 'read',)
