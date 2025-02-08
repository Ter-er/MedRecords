from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name =    models.CharField(max_length=100)
    last_name =     models.CharField(max_length=100)
    national_id =   models.CharField(max_length=100)
    phone_no =      models.CharField(max_length=100)
    email =         models.EmailField()
    date_of_birth = models.DateField()
    gender =        models.ForeignKey('Gender', on_delete=models.CASCADE, null=True, blank=True)
    allergies =     models.TextField()
    address =       models.TextField()
    blood_group =   models.ForeignKey('BloodGroup', on_delete=models.CASCADE, null=True, blank=True)
    genotype =      models.ForeignKey('Genotype', on_delete=models.CASCADE, null=True, blank=True)
    patient_type =  models.ForeignKey('PatientType', on_delete=models.CASCADE, null=True, blank=True)
    height =        models.FloatField()
    weight =        models.FloatField()
    condition =     models.TextField()
    pdf_records =   models.ForeignKey('MedicalRecords',related_name='patient_pdf_records', on_delete=models.CASCADE, null=True, blank=True)
    hospital =      models.CharField(max_length=100)
    emg_name =      models.CharField(max_length=100)
    emg_relationship = models.CharField(max_length=100)
    emg_phone_no =  models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + " " + self.last_name


class MedicalRecords(models.Model):
    patient = models.ForeignKey(Patient,related_name='medical_records_patient', on_delete=models.CASCADE)
    pdf_records = models.FileField(upload_to='MedRecords/media/PatientReports', blank=True, null=True)

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name + " - " + self.patient.national_id
    

class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class BloodGroup(models.Model):
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return self.blood_group
    
    
class Genotype(models.Model):
    genotype = models.CharField(max_length=10)

    def __str__(self):
        return self.genotype
    


class PatientType(models.Model):
    patient_type = models.CharField(max_length=50)

    def __str__(self):
        return self.patient_type


    
