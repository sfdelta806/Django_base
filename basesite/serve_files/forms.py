from django import forms
from .models import FileTypes

class FileTypeForm(forms.ModelForm):
    """
    Form class to render fields in HTML
    """
    class Meta:
        model = FileTypes
        fields = ['folder_path', 'file_types']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folder_path'].widget.attrs.update({"class": "form-control"})
        # or iterate over field to add class for each field
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':"form-control"})
