from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

from user.models import User


User = get_user_model()


type_affectation = (
    ('medecin_directeur','Medecin Directeur'),
    ('infirmier_titulaire','Infirmier Titulaire'),
    ('medecin','Médecin' ),
    ('infirmier','Infirmier' ),
    ('receptioniste','Réceptioniste'),
    ('pharmacien','Pharmacien'),
    ('laboratin','Laboratin'),
    ('stagiaire','Stagiaire'),
    ('medecin_visiteur','Médecin Visiteur')
)

membership_choice = (
    ('public', 'Publique'),
    ('private', 'Privé'),
    ('religious_confession', 'Confession réligieuse'),
    ('religious_confession_conventione', 'Confession réligieuse conventionée '),
    ('private_asbl','Privé Asbl'),
)
category_choice = (
    ('hopital_general_de_reference', 'Hopital général de reference'),
    ('hopital_general', 'Hopital général'),
    ('hopital', 'Hopital'),
    ('centre_hospitalier','Centre hospitalier'),
    ('clinique_universitaire', 'Clinique_universitaire'),
    ('clinique', 'Clinique'),
    ('polyclinique', 'Polyclinique'),
    ('centre_medical', 'Centre medical'),
    ('centre_de_sante', 'Centre de santé'),
    ('centre_de_sante_de_reference', 'Centre de santé de reference'),
    ('centre_de_sante_universitaire', 'Centre de santé universitaire'),
    ('dispensaire', 'Dispensaire')

)

class Service(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nom du service')

    class Meta:
        verbose_name = "Service"

    def __str__(self):
        return self.name


class ZoneDeSante(models.Model):
    name = models.CharField(max_length=128, verbose_name='nom',unique=True)
    code_zone=models.CharField(max_length=50,unique=True,blank=False)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='date de création')

    class Meta:
        verbose_name = "Zone de santé"

    def __str__(self):
        return self.name




class AireDeSante(models.Model):
    health_zone = models.ForeignKey(ZoneDeSante, on_delete=models.CASCADE, verbose_name='zone de santé')
    name = models.CharField(max_length=128, verbose_name='nom')
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='date de création')

    class Meta:
        verbose_name = "Aire de santé"

    def __str__(self):
        return self.name

    

    







class Clinical(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    name = models.CharField(max_length=128, verbose_name='Nom')
    membership = models.CharField(max_length=128, choices=membership_choice, verbose_name='Appartenance')
    category = models.CharField(max_length=128, choices=category_choice, verbose_name='Catégorie')
    aire_de_sante = models.ForeignKey(AireDeSante, on_delete=models.CASCADE)
    zip_cod = models.CharField(max_length=16, unique=True, verbose_name='Code postal')
    matricul = models.PositiveIntegerField(unique=True, verbose_name='matricule')
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='date de création')

    class Meta:
        verbose_name = "Structure de santé"

    def __str__(self):
        return self.name


class Affectation(models.Model):
    clinical = models.ForeignKey(Clinical,on_delete=models.CASCADE)
    email = models.ForeignKey(User,on_delete=models.CASCADE)
    poste = models.CharField( max_length=50,choices= type_affectation)
    date_register = models.DateField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    is_approuve = models.BooleanField(default=True)


    def __str__(self):
        return str(self.email) + '   ' + str(self.clinical)


