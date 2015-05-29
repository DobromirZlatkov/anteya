# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from anteya import roles


@receiver(post_save, User)
def my_callback(sender, **kwargs):
    roles.Client.assign_role_to_user(sender)
