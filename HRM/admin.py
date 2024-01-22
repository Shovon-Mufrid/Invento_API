from django.contrib import admin
from .models import *
# from software_settings.models import *
# Register your models here.


# class DesignationAdmin(admin.ModelAdmin):
#     list_display = ['name', 'Department', 'rank', 'responsibility']


# class EmployeeAdmin(admin.ModelAdmin):
#     # list_display = [field.name for field in EmployeeProfile._meta.get_fields()]
#     list_display = [
#         'employee', 'Office', 'Designation', 'defaultShift',
#         'defaultEntryTime', 'defaultExitTime'
#     ]


# class OfficeAdmin(admin.ModelAdmin):
#     list_display = [
#         'name', 'Office_parent', 'Company', 'OfficeType', 'OfficeLocation',
#     ]


# class PermissionAdmin(admin.ModelAdmin):
#     list_display = [
#         'Designation', 'module', 'sub_module', 'is_create', 'is_read', 'is_update', 'is_delete'
#     ]
#     search_fields = ('Designation__name','sub_module__name', 'module__name' )


admin.site.register(GroupOfCompany)
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(OfficeType)
admin.site.register(OfficeLocation)
admin.site.register(Office)
admin.site.register(OfficeAccountParent)
admin.site.register(OfficeAccount)
admin.site.register(Employee)
admin.site.register(EmployeeDocument)
admin.site.register(IncreamentPolicy)
admin.site.register(LeaveType)
admin.site.register(EmployeeLeave)
admin.site.register(Attendance)
# admin.site.register(Salary)
# admin.site.register(SalaryPayment)
# admin.site.register(Loan)
# admin.site.register(LoanPayment)
# admin.site.register(PaySlip)
admin.site.register(Permission)