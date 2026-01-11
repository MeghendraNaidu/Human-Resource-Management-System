from django.urls import path

from .views import (EmployeeListCreateAPIView, EmployeeDetailAPIView, AttendanceMarkAPIView, AttendanceListAPIView, DepartmentReportAPIView,        EmployeeListView, EmployeeDetailView, AttendanceMarkView, DepartmentReportView,)

urlpatterns = [
    # =====================
    # API ROUTES
    # =====================

    # Employee APIs
    path("api/employees/", EmployeeListCreateAPIView.as_view(), name="api_employee_list_create",),
    path("api/employees/<int:pk>/", EmployeeDetailAPIView.as_view(),name="api_employee_detail",),

    # Attendance APIs
    path("api/attendance/mark/", AttendanceMarkAPIView.as_view(), name="api_attendance_mark",),
    path("api/attendance/<int:employee_id>/", AttendanceListAPIView.as_view(), name="api_attendance_list",),

    # Reports API
    path("api/reports/department-count/", DepartmentReportAPIView.as_view(), name="api_department_report",),

    # =====================
    # TEMPLATE ROUTES
    # =====================

    # path("employees/", EmployeeListCreateAPIView.as_view(), name="employee_list_page",),
    # path("employees/<int:pk>/", EmployeeDetailAPIView.as_view(), name="employee_detail_page",),
    # path("attendance/mark/", AttendanceMarkAPIView.as_view(), name="attendance_mark_page",),
    # path("reports/departments/", DepartmentReportAPIView.as_view(), name="department_report_page",),
    
    path("employees/", EmployeeListView.as_view(), name="employee_list"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),
    path("attendance/mark/", AttendanceMarkView.as_view(), name="attendance_mark"),
    path("reports/departments/", DepartmentReportView.as_view(), name="department_report",),
]
