from django.contrib import admin
from iot.models import IoTData


class IoTDataAdmin(admin.ModelAdmin):
    list_display = ['device_tag', 'random_number', 'timestamp', 'created_at', 'data']
    search_fields = ['device_tag']
    list_filter = ['created_at']

admin.site.register(IoTData, IoTDataAdmin)
