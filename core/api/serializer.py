from rest_framework import serializers
from core.models import Member



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name' , 'surname', 'phone' , 'photo' ]



class MemberSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name']
