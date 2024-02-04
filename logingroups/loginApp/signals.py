from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

def addToStudentGroup(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='STUDENT')
        instance.groups.add(group)

post_save.connect(addToStudentGroup, sender=User)
