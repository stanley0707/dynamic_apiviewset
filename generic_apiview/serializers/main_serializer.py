from rest_framework import serializers


class GenModelSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = None
        fields = '__all__' 
