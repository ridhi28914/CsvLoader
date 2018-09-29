from rest_framework import serializers
from models import *
class itemSerializer(serializers.ModelSerializer):
	class Meta:
		model=item
		fields='__all__'#optional, name of fields to return as a list