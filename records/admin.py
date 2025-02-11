from django.contrib import admin
from .models import Patient, MedicalRecords, Gender, BloodGroup, Genotype, PatientType

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_id', 'phone_no', 'email', 'date_of_birth', 'gender', 'blood_group', 'genotype', 'patient_type', 'height', 'weight', 'hospital', 'emg_name', 'emg_relationship', 'emg_phone_no')
    search_fields = ('first_name', 'last_name', 'national_id', 'email')
    list_filter = ('gender', 'blood_group', 'genotype', 'patient_type')
    ordering = ('last_name', 'first_name')

class MedicalRecordsAdmin(admin.ModelAdmin):
    list_display = ('patient', 'pdf_records')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__national_id')
    list_filter = ('patient',)
    ordering = ('patient__last_name', 'patient__first_name')

class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)
    search_fields = ('gender',)

class BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('blood_group',)
    search_fields = ('blood_group',)

class GenotypeAdmin(admin.ModelAdmin):
    list_display = ('genotype',)
    search_fields = ('genotype',)

class PatientTypeAdmin(admin.ModelAdmin):
    list_display = ('patient_type',)
    search_fields = ('patient_type',)

# Register the models with the admin site
admin.site.register(Patient, PatientAdmin)
admin.site.register(MedicalRecords, MedicalRecordsAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(BloodGroup, BloodGroupAdmin)
admin.site.register(Genotype, GenotypeAdmin)
admin.site.register(PatientType, PatientTypeAdmin)
