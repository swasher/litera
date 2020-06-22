from django.contrib import admin
from .models import Font
from .models import Family

admin.site.site_header = 'Font DB'


class FontAdmin(admin.ModelAdmin):
    list_display = ['fullName']


admin.site.register(Family)
admin.site.register(Font, FontAdmin)

