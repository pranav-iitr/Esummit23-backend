from rest_framework import serializers
from .models.otp import OTP
from .models.role.startup import StartupUser
from .models.role.student import StudentUser
from .models.role.proff import ProffUser
from .models.role.ca import CAUser
from .models.querry import Querry


class otpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        exclude = ["id","date_created" ,"date_expired"]


class QuerrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Querry
        fields = ["name", "email", "phone_number", "message"]


class EventStartpuUser(serializers.ModelSerializer):
    class Meta:
        model = StartupUser
        fields = ["startup_name", "email", "phone_number", "esummit_id"]


class EventStudentUser(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ["name", "email", "phone_number", "esummit_id"]


class EventProffUser(serializers.ModelSerializer):
    class Meta:
        model = ProffUser
        fields = ["name", "email", "phone_number", "esummit_id"]


class CAUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAUser
        exclude=['payment','taskAssigned','taskCompleted','esummit_id','created','updated','authToken','points']

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        exclude=['payment','esummit_id','created','updated','authToken']

class ProffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProffUser
        exclude=['payment','esummit_id','created','updated','authToken']

class StartupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupUser
        exclude=['payment','esummit_id','created','updated','authToken']
