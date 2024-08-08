from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient, SSI,VisitePatient
from .serializers import PatientSerializer, SSISerializer,VisitePatientSerializer
from django.http import JsonResponse,HttpResponse
from consultation.models import Consultation, MedicamentPrescrit, ExamenDemande
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.conf import settings
from cryptography.fernet import Fernet
import base64
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nom', 'post_nom', 'prenom', 'adresse', 'genre', 'clinical', 'date_register']
    search_fields = ['nom', 'post_nom', 'prenom', 'adresse']
    ordering_fields = ['nom', 'post_nom', 'prenom', 'date_register']

    @action(detail=False, methods=['post'], url_path='scan-qr')
    def scan_qr(self, request):
        qr_code_data = request.data.get('qr_code_data')
        if not qr_code_data:
            return Response({"detail": "Les données du QR code sont requises"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            secret_key = settings.FERNET_KEY
            decrypted_data = self.decrypt(qr_code_data, secret_key)
            patient_info = decrypted_data.split(';')
            code = patient_info[-1]
            
            patient = get_object_or_404(Patient, code=code)
            
            clinical_id = request.user.clinical.id
            if SSI.objects.filter(patient=patient, clinical_id=clinical_id).exists():
                return Response({"detail": "Le patient est déjà enregistré dans cet établissement."}, status=status.HTTP_200_OK)
            
            ssi = SSI.objects.create(patient=patient, clinical_id=clinical_id)
            return Response(SSISerializer(ssi).data, status=status.HTTP_201_CREATED)

        except Patient.DoesNotExist:
            return Response({"detail": "Patient non trouvé. Veuillez créer un nouveau dossier patient."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def decrypt(self, encrypted_text, key):
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_text.encode())
        return decrypted.decode()

    @action(detail=True, methods=['get'], url_path='generate-pdf')
    def generate_pdf(self, request, pk=None):
        patient = get_object_or_404(Patient, pk=pk)
        consultations = Consultation.objects.filter(patient=patient)
        ssi = SSI.objects.get(patient=patient)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="dossier_medical_{patient.nom}.pdf"'

        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        p.drawString(100, height - 100, f"Dossier Médical de {patient.nom} {patient.prenom}")
        p.drawString(100, height - 120, f"Adresse: {patient.adresse}")
        p.drawString(100, height - 140, f"Date de Naissance: {patient.date_birth}")
        p.drawString(100, height - 160, f"Genre: {patient.get_genre_display()}")

        y_position = height - 180

        p.drawString(100, y_position, "Consultations:")
        y_position -= 20

        for consultation in consultations:
            p.drawString(100, y_position, f"Date: {consultation.date_consultation}")
            y_position -= 20
            p.drawString(100, y_position, f"Symptômes: {consultation.symptomes}")
            y_position -= 20
            p.drawString(100, y_position, f"Diagnostic: {consultation.diagnostic}")
            y_position -= 20
            p.drawString(100, y_position, f"Recommandations: {consultation.recommandations}")
            y_position -= 20
            p.drawString(100, y_position, f"Clinique: {consultation.clinical.name}")
            y_position -= 20

            medicaments = MedicamentPrescrit.objects.filter(consultation=consultation)
            examens = ExamenDemande.objects.filter(consultation=consultation)

            p.drawString(100, y_position, "Médicaments Prescrits:")
            y_position -= 20
            for medicament in medicaments:
                p.drawString(120, y_position, f"{medicament.nom}, Dosage: {medicament.dosage}, Fréquence: {medicament.frequence}")
                y_position -= 20

            p.drawString(100, y_position, "Examens Demandés:")
            y_position -= 20
            for examen in examens:
                p.drawString(120, y_position, f"Type: {examen.type_examen}, Description: {examen.description}")
                y_position -= 20

            y_position -= 20

        p.drawString(100, y_position, "SSI:")
        y_position -= 20
        p.drawString(100, y_position, f"Température: {ssi.temperature}")
        y_position -= 20
        p.drawString(100, y_position, f"Tension: {ssi.tension}")
        y_position -= 20
        p.drawString(100, y_position, f"Poids: {ssi.poids}")
        y_position -= 20
        p.drawString(100, y_position, f"Clinique: {ssi.clinical.name}")

        p.showPage()
        p.save()
        return response


class SSIViewSet(viewsets.ModelViewSet):
    queryset = SSI.objects.all()
    serializer_class = SSISerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient', 'temperature', 'tension', 'poids', 'clinical']
    search_fields = ['patient__nom', 'patient__post_nom', 'patient__prenom']
    ordering_fields = ['date_register','temperature', 'tension', 'poids']



class VisitePatientViewSet(viewsets.ModelViewSet):
    queryset = VisitePatient.objects.all()
    serializer_class = VisitePatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient', 'clinical', 'date_visite']
    search_fields = ['patient__nom', 'patient__post_nom', 'patient__prenom', 'clinical__name']
    ordering_fields = ['date_visite', 'patient__nom', 'patient__post_nom', 'clinical__name']