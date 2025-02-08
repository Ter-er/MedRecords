from django.db import models

from django.contrib.auth.models import AbstractUser
from records.models import Gender

# Create your models here.
class MedUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField()
    specialty = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    med_license = models.FileField(upload_to='MedRecords/media/MedLicense', blank=True, null=True)
    hospital = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.email} - {self.specialization}'
    
class MedRole(models.Model):
    user = models.OneToOneField(MedUser, on_delete=models.CASCADE, related_name='role_profile')

    # Define the choices for the role field

    DOCTOR = 'Doctor'
    LAB_SCIENTIST = 'Lab Scientist'
    RECORDS_OFFICER = 'Records Officer'

    ROLE_CHOICES = [
        (DOCTOR, 'Doctor'),
        (LAB_SCIENTIST, 'Lab Scientist'),
        (RECORDS_OFFICER, 'Records Officer'),
    ]

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default=DOCTOR,
    )

    def __str__(self):
        return f'{self.user.email} - {self.role}'