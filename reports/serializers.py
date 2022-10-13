from rest_framework import serializers

class ReportSerializer(serializers.Serializer):
    unitid = serializers.IntegerField(min_value=0)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()

class SpeedReportSerializer(serializers.Serializer):
    unitid = serializers.IntegerField(min_value=0)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()
    speed_limit = serializers.IntegerField()

class TripReportSerializer(serializers.Serializer):
    unitid = serializers.IntegerField(min_value=0)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()
    geofence_option = serializers.BooleanField()

class GeofenceReportSerializer(serializers.Serializer):
    unitid = serializers.IntegerField(min_value=0)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()
    geofences = serializers.ListField(
        child = serializers.IntegerField()
    )

class StopReportSerializer(serializers.Serializer):
    unitid = serializers.IntegerField(min_value=0)
    initial_datetime = serializers.DateTimeField()
    final_datetime = serializers.DateTimeField()
    geofence_option = serializers.BooleanField()
    discard_time = serializers.IntegerField(
        min_value=0,
        max_value=10,
    )