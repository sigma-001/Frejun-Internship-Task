from django.db import models


class CallRecord(models.Model):
    
    from_number = models.CharField(max_length = 16)
    to_number = models.CharField(max_length = 16)
    start_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
    # Indexing the fields in order to optimize the filtering
        indexes = [models.Index(fields=['from_number']),
                   models.Index(fields=['to_number'])]
        
        verbose_name = "Call Record"
        verbose_name_plural = "Call Records"
    
    def __str__(self) -> str:
        return f"{self.from_number} --> {self.to_number}"