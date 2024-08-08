from django.db import models
from clinical.models import Clinical
from django.core.exceptions import ValidationError

# Create your models here.


class CategorieMedicament(models.Model):
    nom = models.CharField(max_length=200)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom


class Medicament(models.Model):
    nom = models.CharField(max_length=200)
    categorie = models.ForeignKey(CategorieMedicament, on_delete=models.CASCADE)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.nom
    

class GestionStock(models.Model):
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)
    date_entree = models.DateField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.medicament)

class Vente(models.Model):
    medicament = models.ForeignKey(GestionStock, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_vente = models.DateField(auto_now_add=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.medicament)

    def save(self, *args, **kwargs):
        stock, created = GestionStock.objects.get_or_create(
            medicament=self.medicament.medicament,
            defaults={
                'quantite': self.medicament.quantite + self.quantite,
                'date_entree': self.medicament.date_entree,
                'prix_unitaire': self.medicament.prix_unitaire,
                'clinical': self.medicament.clinical,
            }
        )

        # Vérifier si la quantité en stock est suffisante pour la vente
        if self.quantite > stock.quantite:
            raise ValidationError({"quantite": "Quantité insuffisante en stock."})

        # Mettre à jour la quantité en stock
        stock.quantite -= self.quantite
        stock.save()

        # Calculer le montant total de la vente
        self.montant_total = self.quantite * stock.prix_unitaire

        super().save(*args, **kwargs)