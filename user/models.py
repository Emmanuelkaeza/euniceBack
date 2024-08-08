from __future__ import unicode_literals

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

type_user = (
   
    ('medecin_chef_de_zone','Medecin Chef de zone'),
    ('medecin_chef_de_division_provincial','Medecin chef de Division Provincial'),
    ('medecin_chef_de_division_nationale','Medecin chef de Division National'),
    ('ministre_provincial','Ministre Provincial'),
    ('ministre_national','Ministre National'),
    ('infirmier_titulaire','Infirmier Titulaire'),
    ('administrateur','Administrateur'),
    ('administrateur_etablissement','Administrateur établissement'),
    ('medecin','Medecin'),
    ('infirmier','Infirmier'),
    ('pharmacien',"Pharmacien"),
    ('laboratin','Laboratin'),

)






class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    poste=models.CharField(choices=type_user, max_length=50,default='administrateur_etablissement')
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self, full_name=None):
        nom_complet = '%s %s' % (self.first_name, self.last_name)
        return nom_complet.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)