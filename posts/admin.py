"""The register module for posrt"""

#Django
from django.contrib import admin

#Local modules
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin register"""

    list_display = ('user', 'title', 'created', 'modifie')
