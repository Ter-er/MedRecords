from django.contrib import admin
from .models import MedUser
from django.contrib.auth.admin import UserAdmin

# Define custom admin form for MedUser to display fields in a more readable way
class MedUserAdmin(UserAdmin):
    model = MedUser
    # Specify which fields to display
    list_display = ('email', 'phone_no', 'gender', 'date_of_birth', 'specialty', 'employee_id', 'hospital', 'department', 'is_staff')
    list_filter = ('gender', 'specialty', 'hospital', 'department', 'is_staff')
    search_fields = ('email', 'employee_id', 'specialty')
    ordering = ('email',)
    
    # Fields to be displayed in the user detail page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_no', 'gender', 'date_of_birth', 'specialty', 'employee_id', 'med_license', 'hospital', 'department')}),
    )
    # Fields to be displayed in the user creation page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_no', 'gender', 'date_of_birth', 'specialty', 'employee_id', 'med_license', 'hospital', 'department')}),
    )

# Register MedUser with the custom admin
admin.site.register(MedUser, MedUserAdmin)

# # Register MedRole model with admin interface
# @admin.register(MedRole)
# class MedRoleAdmin(admin.ModelAdmin):
#     list_display = ('user', 'role')
#     list_filter = ('role',)
#     search_fields = ('user__email', 'role')
#     ordering = ('role',)

