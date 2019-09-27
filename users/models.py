from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)

    def __str__(self):
        res = "{} ".format(self.user.username)
        if self.name or self.surname:
            fullname = ' '.join([self.name, self.surname]).strip()
            res += " - {}".format(fullname)
        return res

    # def save(self):
    #     super().save()