from datetime import date

from rest_framework import serializers

from .models import Employee, Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for Attendance model.

    Handles validation to prevent invalid
    or logically incorrect attendance entries.
    """

    class Meta:
        model = Attendance
        fields = (
            "id",
            "date",
            "check_in_time",
            "check_out_time",
        )

    def validate(self, attrs):
        """
        Ensure check-out time is after check-in time.
        """
        check_in = attrs.get("check_in_time")
        check_out = attrs.get("check_out_time")

        if check_in >= check_out:
            raise serializers.ValidationError(
                "Check-out time must be after check-in time."
            )

        return attrs


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee creation and listing.
    """

    class Meta:
        model = Employee
        fields = (
            "id",
            "name",
            "email",
            "address",
            "department",
            "designation",
            "date_of_joining",
            "created_at",
        )
        read_only_fields = ("id", "created_at")

    def validate_date_of_joining(self, value):
        """
        Prevent future joining dates.
        """
        if value > date.today():
            raise serializers.ValidationError(
                "Date of joining cannot be in the future."
            )
        return value


class EmployeeDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for employee detail view.

    Includes nested attendance records.
    """

    attendances = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = (
            "id",
            "name",
            "email",
            "address",
            "department",
            "designation",
            "date_of_joining",
            "created_at",
            "attendances",
        )
