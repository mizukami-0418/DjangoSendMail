from django.db import models

class MailModel(models.Model):
    subject = models.CharField(max_length=50) # メールの件名
    message = models.TextField() # メール本文
    from_email = models.EmailField(max_length=254) # 送信元メールアドレス
    recipient_email = models.EmailField(max_length=255) # 宛先メールアドレス　
    recipient_list = models.TextField() # 宛先メールアドレス(複数の場合)