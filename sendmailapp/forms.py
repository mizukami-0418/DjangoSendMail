from django import forms
from .models import MailModel

class MailForm(forms.ModelForm):
    subject = forms.CharField(label='件名') # メールの件名
    message = forms.CharField(label='本文', widget=forms.Textarea) # メール本文
    from_email = forms.EmailField(label='送信元メールアドレス') # 送信元メールアドレス
    recipient_email = forms.EmailField(label='送信先メールアドレス', help_text='メールアドレスは１件のみです')
    recipient_list = forms.CharField(
        label='宛先メールアドレス', widget=forms.Textarea, help_text='メールアドレスはカンマで区切って入力してください'
        )
    
    class Meta:
        model = MailModel
        fields = ('subject', 'message', 'from_email', 'recipient_list')
    
