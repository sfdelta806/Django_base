from django.db import models

file_type_choices = [
    ('images', 'images'),
    ('ideo', 'video'),
    ('audio', 'audio'),
    ('documents', 'documents'),
    ('misc', 'misc')
]

class FileTypes(models.Model):
    """
    Django model class to save data in sqlite and create base forms
    """
    folder_path = models.CharField(max_length=250)
    file_types = models.CharField(max_length=24, choices=file_type_choices, default='images')

    def __str__(self):
        return self.file_types