from django.db import models

# Create your models here.

class Employee(models.Model):
    """
    Represents an employee in the HRMS system.

    Stores personal and organizational details required
    for employee management and reporting.
    """

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"


class Attendance(models.Model):
    """
    Represents daily attendance for an employee.

    Ensures that an employee can have only one
    attendance record per date.
    """

    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="attendances")
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()

    class Meta:
        unique_together = ("employee", "date")
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"{self.employee.name} - {self.date}"