from django import forms

from  MoveFiles.models import Documents

class DocumentsForm(forms.ModelForm):
    class Meta:
        model= Documents
        fields= "__all__"