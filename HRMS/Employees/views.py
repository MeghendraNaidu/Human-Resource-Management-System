from django.shortcuts import render

from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Employee, Attendance
from .serializers import (EmployeeSerializer, EmployeeDetailSerializer, AttendanceSerializer,)

from django.views import View
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.db.models import Count


# Create your views here.

class EmployeeListCreateAPIView(APIView):
    """
    Handles listing all employees and creating new employees.
    """

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "Employee created successfully", "data": serializer.data})

        return Response({"status": "error", "errors": serializer.errors})


class EmployeeDetailAPIView(APIView):
    """
    Retrieves detailed information of a single employee,
    including attendance records.
    """

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeDetailSerializer(employee)

        return Response({"status": "success","data": serializer.data})


class AttendanceMarkAPIView(APIView):
    """
    Marks attendance for an employee.

    Prevents duplicate attendance entries
    for the same employee and date.
    """

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"status": "error", "errors": serializer.errors})

        employee_id = request.data.get("employee")
        attendance_date = request.data.get("date")

        employee = get_object_or_404(Employee, pk=employee_id)

        if Attendance.objects.filter(
            employee=employee,
            date=attendance_date
        ).exists():
            return Response({"status": "error", "message": "Attendance already marked for this employee on this date"})

        Attendance.objects.create(
            employee=employee,
            date=serializer.validated_data["date"],
            check_in_time=serializer.validated_data["check_in_time"],
            check_out_time=serializer.validated_data["check_out_time"],
        )

        return Response({"status": "success", "message": "Attendance marked successfully"})


class AttendanceListAPIView(APIView):
    """
    Lists attendance records for a specific employee.
    """

    def get(self, request, employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        attendance_qs = Attendance.objects.filter(employee=employee)

        serializer = AttendanceSerializer(attendance_qs, many=True)

        return Response({"status": "success", "employee": employee.name, "data": serializer.data})


class DepartmentReportAPIView(APIView):
    """
    Provides department-wise employee count
    using ORM aggregation.
    """

    def get(self, request):
        report = (
            Employee.objects
            .values("department")
            .annotate(employee_count=Count("id"))
            .order_by("department")
        )

        return Response({"status": "success", "data": list(report)})

# TEMPLATE VIEWS ONLY

class DashboardView(TemplateView):
    """
    Renders the HRMS dashboard homepage.
    """
    template_name = "dashboard.html"


class EmployeeListView(ListView):
    """
    Displays a list of all employees.
    """
    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"
    ordering = ["name"]


class EmployeeDetailView(View):
    """
    Displays employee details along with attendance records.
    """

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        attendances = employee.attendances.all()

        context = {
            "employee": employee,
            "attendances": attendances,
        }

        return TemplateView.as_view(
            template_name="employees/employee_detail.html",
            extra_context=context
        )(request)


class AttendanceMarkView(View):
    """
    Handles attendance marking via HTML form.
    """

    template_name = "attendance/attendance_mark.html"

    def get(self, request):
        employees = Employee.objects.all()

        return TemplateView.as_view(
            template_name=self.template_name,
            extra_context={"employees": employees}
        )(request)

    def post(self, request):
        employee_id = request.POST.get("employee")
        date = request.POST.get("date")
        check_in_time = request.POST.get("check_in_time")
        check_out_time = request.POST.get("check_out_time")

        employee = get_object_or_404(Employee, pk=employee_id)

        if Attendance.objects.filter(employee=employee, date=date).exists():
            messages.error(
                request,
                "Attendance already marked for this employee on this date."
            )
            return redirect("/attendance/mark/")

        Attendance.objects.create(
            employee=employee,
            date=date,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
        )

        messages.success(request, "Attendance marked successfully.")
        return redirect("/attendance/mark/")


class DepartmentReportView(View):
    """
    Displays department-wise employee count report.
    """

    def get(self, request):
        report = (
            Employee.objects
            .values("department")
            .annotate(employee_count=Count("id"))
            .order_by("department")
        )

        return TemplateView.as_view(
            template_name="reports/department_report.html",
            extra_context={"report": report}
        )(request)
