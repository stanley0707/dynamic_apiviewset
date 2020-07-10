from django.test import TestCase
from django.test import TestCase, Client
from book.models import Book, Author
from rest_framework import status
from .serializers import GenModelSerializer

client = Client()


class GetTest(TestCase):
	""" Test module for GET all puppies API """

	def setUp(self):
		b1 = Book.objects.create(
		  title='книга 1', description='описание 1', secret='123124u241y2u41u2y47')
		
		b2 = Book.objects.create(
		  title='книга 2', description='описание 2', secret='34728374ggg6sat62t64')
		
		b3 = Book.objects.create(
		  title='книга 3', description='описание 3', secret='65dst6tas8aey4g7d76d')
		
		b4 = Book.objects.create(
		  title='книга 4', description='описание 4', secret='8r2i37d7t2eu63rtu6rt')

		a1 = Author.objects.create(
			fullname='Васислий и Григорий Пупкины')
		
		a2 = Author.objects.create(
			fullname='Иван Задунайский')
		
		a3 = Author.objects.create(
			fullname='Зигмунд Поварёшкин')

		a1.author_books.add(b1, b2)
		a2.author_books.add(b3)
		a3.author_books.add(b4)

	
	def test_get_all_book(self):
		# get API response
		response = client.get('/api/book/')
		# get data from db
		GenModelSerializer.Meta.model, GenModelSerializer.Meta.fields \
			= Book, Book.serialize_fields

		serializer = GenModelSerializer(Book.objects.all().order_by('-id'), many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
	
	def post(self):
		request = client.post('/api/book/',
			{'title': 'книга 5', 'description': 'описание 5'},
			format='vnd.api+json'
		)
		print(request.data)

