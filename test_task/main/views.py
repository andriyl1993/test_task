# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from models import Domain
from serializers import DomainSerializer


@api_view(['POST', 'GET'])
@permission_classes((AllowAny,))
def list_or_add_domains(request):
	if request.method == "GET":
		if request.user.is_anonymous():
			domains = Domain.objects.filter(is_private = False)
		else:
			domains = Domain.objects.all()

		content = {
			'domains': DomainSerializer(domains, many=True).data
		}
		return Response(content)
	elif request.method == "POST":
		serializer = DomainSerializer(data = request.POST)
		if request.user.username == "manager":
			if serializer.valid():
				response = serializer.create()
				if response:
					content = {
						'error': False,
						'error_text': ''
					}
				else:
					content = {
						'error': True,
						'error_text': 'Invalid data'
					}
			else:
				content = {
					'error': True,
					'error_text': 'Invalid data'
				}
		else:
			content = {
				'error': True,
				'error_text': 'Permission denied'
			}
		return Response(content)


@api_view(['GET'])
@permission_classes((AllowAny,))
def detail_domain(request, pk):
	try:
		domain = Domain.objects.get(pk = pk)
		if domain.is_private and request.user.is_anonymous():
			error = True
			error_text = 'You have not permissions'
			domain = None
		else:
			error = False
			error_text = ''
			domain = DomainSerializer(domain, many=False).data
		content = {
			'domain': domain,
			'error': error,
			'error_text': error_text
		}
	except:
		content = {
			'domain': None,
			'error': True,
			'error_text': 'no current domain'
		}
	return Response(content)


def add_domain(request):

	print request.POST
	return render(request, 'domain.html')