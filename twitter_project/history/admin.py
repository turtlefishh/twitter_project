from django.contrib import admin
from .models import History

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'method', 'summary', 'date')
    list_filter = ('method', 'date')
    search_fields = ('summary', 'user__username')