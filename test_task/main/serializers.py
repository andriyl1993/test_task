from rest_framework import serializers
from models import Domain

class DomainSerializer(serializers.ModelSerializer):

	class Meta:
		model = Domain
		fields = ('name', 'is_private', 'id')

	def valid(self):
		if self.is_valid() and self.data.get('is_private') != None:
			return True
		else:
			return False

	def create(self):
		domain = Domain(
			name = self.data.get('name'),
			is_private = self.data.get('is_private')
		)
		
		if domain.is_https() and domain.is_valid_address(): 
			domain.save()
			return True
		else:
			return False

