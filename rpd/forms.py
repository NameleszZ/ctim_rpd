from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory
from .models import User, TableOfDisc, TableOfEducators, Group, Chairs


class MessageSendForm(forms.ModelForm):


    class Meta:
        model = TableOfDisc
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super(MessageSendForm, self).__init__(*args, **kwargs)
        self.fields['message'].label = 'Поле для сообщения'


class AssignRpdForm(forms.ModelForm):
    educ_comment = forms.CharField(required=False)

    class Meta:
        model = TableOfDisc
        fields = ['educator','status',
                  'educ_comment']

    def __init__(self, *args, **kwargs):
        super(AssignRpdForm, self).__init__(*args, **kwargs)
        self.fields['educator'].label = 'Укажите кому отправить'
        self.fields['educ_comment'].label = 'Комментарий:'
        self.fields['status'].label = 'Статус'


class FileRpdForm(forms.ModelForm):

    class Meta:
        model = TableOfDisc
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(FileRpdForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = 'Прикрепите файл'



