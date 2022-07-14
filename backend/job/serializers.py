from rest_framework import serializers
from .models import CandidateApplied, Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'

class CandidatesAppliedSerializer(serializers.ModelSerializer):

    job=JobSerializer()
    class Meta:
        model=CandidateApplied
        fields=('user','resume','appliedAt','job')
