from django.test.client import Client
from django.test import TestCase

class ListDomainsTestCase(TestCase):

	def get_domain_anonymous(self):
		client = Client()
		response = client.get(' /api/')
		self.assertEqual(response.status_code, 200)

	def get_domain_authorized(self):
		client = Client()
		
		res1 = client.post('/api-auth/login/', {'username': 'admin', 'password': 'admin'})
		response = client.get('/api/')
		self.assertEqual(response.status_code, 200)


class GetDomainByPK(TestCase):

	def test(self):
		client = Client()
		pk = 1

		response = client.post('/api-auth/login/', {'username': 'manager', 'password': '12121212'})
		response = client.post('/api/', {'is_private': 0, 'name': 'https://test.com'})

		res1 = client.get('/api/1/')
		self.assertEqual(response.status_code, 200)


class CreateDomains(TestCase):

	def set_domain(self):
		self.domains = []
		client = Client()
		response = client.post('/api-auth/login/', {'username': 'manager', 'password': '12121212'})

		for i in range(10):
			if i < 5:
				response = client.post('/api/', {'is_private': 0, 'name': 'https://test' + i + '.com'})
			else:
				response = client.post('/api/', {'is_private': 1, 'name': 'https://test' + i + '.com'})
			self.assertEqual(response.status_code, 200)




if __name__ == "__main__":
	# settings.configure()
	unittest2.main()
