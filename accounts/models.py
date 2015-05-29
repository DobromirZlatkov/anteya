from django.db import models
from django.contrib.auth.models import User


# class Role(models.Model):
#     """
#     The Employee can be either an admin or receptionist.
#     The admin's function is to manage the Clubs's different
#     parts: play fields, price models, other employees, etc.
#     """

#     TYPES = [
#         ['admin', 'Admin'],  # access to everything
#         ['firm', 'Firm'],  # access to schedule only
#         ['casual', 'Casual'],  # deactivate user.
#     ]

#     user = models.ForeignKey(User, related_name='employees')
#    # firm = models.ForeignKey('clubs.Club')
#     type_of = models.CharField(
#         max_length=250,
#         choices=TYPES
#     )
#     disabled = models.BooleanField(default=False)

#     def __unicode__(self):
#         return u'{type}: {f_name} {l_name}'.format(
#             type=self.type_of,
#             f_name=self.user.first_name,
#             l_name=self.user.last_name
#         )

#     def is_admin(self):
#         return self.type_of == 'manager' or self.type_of == 'owner'

#     def is_owner(self):
#         return self.type_of == 'owner'

#     def is_reception(self):
#         return self.type_of == 'reception'
