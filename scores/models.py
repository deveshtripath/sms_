from django.db import models
from twilio.rest import Client
import os
# Create your models here.


class Score(models.Model):
    result=models.PositiveIntegerField()

    # def __str__(self):
    #     return self.result
    def __str__(self):
       return str(self.result)

    def save(self,*args,**kwargs):
        if self.result < 70:
            account_sid = 'ACafa4090ee82d544af83ed2b1a6f83653'
            auth_token = '49df6c41ba825468c21a820666504093'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'the current result is bad -{self.result}',
                                        from_='+12142204554',
                                        to='+919305958149'
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)