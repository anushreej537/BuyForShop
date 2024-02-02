from tortoise.models import Model
from tortoise import fields

id:int pk=True
name email password is_active=models.BooleanField(_(""),default=True)

last_login  created=models.DateTimeField(_(""), auto_now=False, auto_now_add=False)



