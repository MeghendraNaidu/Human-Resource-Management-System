from django.contrib import admin
from .models import Employee, Attendance

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin configuration for Employee model.
    """

    list_display = (
        "name",
        "email",
        "department",
        "designation",
        "date_of_joining",
        "created_at",
    )
    list_filter = ("department", "designation")
    search_fields = ("name", "email")
    ordering = ("name",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Attendance model.
    """

    list_display = (
        "employee",
        "date",
        "check_in_time",
        "check_out_time",
    )
    list_filter = ("date",)
    search_fields = ("employee__name",)
    ordering = ("-date",)