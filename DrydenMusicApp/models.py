from django.db import models
from storages.backends.s3boto import S3BotoStorage
import pdb
import uuid

def data_file_path(instance, filename):
    result = '_'.join(['%06d' % uuid.uuid4(), filename]).replace(" ","-")
    return result

# Create your models here.
class music(models.Model):
    def __str__(self):
        return self.title
        
    FILE_TYPE_CHOICES = [(1,'Single Song Sheet'),
                            (2,'Songbook'),
                            ]    
    
    music_file = models.FileField(null=True, upload_to=data_file_path, 
                    storage=S3BotoStorage(location='music_files'),
                    help_text='')
    file_type = models.IntegerField(null=False, choices=FILE_TYPE_CHOICES, default=1)               
    title = models.CharField(blank=True, max_length=200)
    first_line = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
