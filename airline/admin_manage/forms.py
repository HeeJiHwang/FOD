from django import forms
from .models import Inform

class BoardWriteForm(forms.ModelForm):
    class Meta:
        model = Inform
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

    def clean(self):
        cleaned_data = super(Inform,self).clean()

        title = cleaned_data.get('title','')
        content = cleaned_data.get('contents','')

        if title == '':
            self.add_error('title','제목 입력하세요')
        elif content == '':
            self.add_error('content','글 내용을 입력하세요')
        else:
            self.title = title
            self.content = content