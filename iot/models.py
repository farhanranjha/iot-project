from django.db import models


class IoTData(models.Model):
    device_tag = models.CharField(max_length=255)
    random_number = models.IntegerField()
    data = models.JSONField(default=dict)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_tag

    class Meta:
        verbose_name = "IoT Data"
        verbose_name_plural = "IoT Data"
        ordering = ["-created_at"]
