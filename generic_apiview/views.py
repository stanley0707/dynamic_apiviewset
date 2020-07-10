from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import GenModelSerializer
from rest_framework import status
from .utils import get_model_from_any_apps, get_prams_construct
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


class ListView(viewsets.ViewSet):
	
	renderer_classes = [JSONRenderer]
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	
	@property
	def model(self):
		"""
		Принимает название модели в качестве
		URL параметра (REST)
		"""
		return get_model_from_any_apps(
			str(self.kwargs['model_name'])
			)
	
	def get_all_or_fliter(self, params):
		"""
		Фильтруем модели или забираем все
		в зависимости от полученного params
		"""
		params.setdefault('order_by', '-id')
		params.setdefault('limit', '50')
		order_by = params.pop('order_by')
		limit = params.pop('limit')
		return self.model.objects.all().filter(**params).order_by(order_by)[:int(limit)]           

	def get_model(self):
		"""
		Берём одну модель или возвращаем 404
		"""
		return get_object_or_404(
				self.model,
				pk=self.kwargs['model_pk']
			)
	
	def select_for_upd(self):
		return self.model.objects.select_for_update().filter(id=self.kwargs['model_pk'])
	
	def get_serialize_data(self, many=False):
		"""
		Инициализируем мета аттрибуты класса сериализации
		и поля модели из аттрибут класса модели serialize_fields.
		many  поумолчанию ложно
		"""
		GenModelSerializer.Meta.model, GenModelSerializer.Meta.fields = \
			self.model, self.model.serialize_fields
		return GenModelSerializer(
				self.data,
				many=many
			).data

	
	def list(self, request, **kwargs):
		"""
		Принимаем GET запрос на выборку множества
		объектов. Разбор параметров в фильтр осуществляем
		в методе get_all_or_fliter
		"""
		self.data = self.get_all_or_fliter(
			params=get_prams_construct(request)
			)
		return Response(self.get_serialize_data(many=True))
	
	def create(self, request, **kwargs):
		"""
		Создаём объект в базе. Принимаем
		множества разннообразных значений.
		Описание обязательных и необязателльных
		параметров описывается на уровне модели:
		ловим исключение ORM и возвращаем ошибку
		пользователю или производим запись на основе
		полученных аргументов.

		http POST
		"""
		try: 
			self.model.objects.create(**request.data)
			msg = 'success'
		
		except ValidationError as e:
			msg = str(e)

		except IntegrityError as e:
			msg = str(e)

		return Response(
				{'msg': msg},
				status=status.HTTP_200_OK
			)
	
	def retrieve(self, request, **kwargs):
		"""
		один объект по идентификатору http GET .../<params>/<id>
		"""
		self.data = self.get_model()
		return Response(
				self.get_serialize_data(),
				status=status.HTTP_200_OK
			)

	def update(self, request, **kwargs):
		"""
		обновление объекта http PUT
		"""
		try:
			self.select_for_upd().update(**request.data)
			msg = 'success'
		except ValidationError as e:
			msg = str(e)
		except IntegrityError as e:
			msg = str(e)
		return Response(
				{'msg': msg},
				status=status.HTTP_200_OK
			)

	def partial_update(self, request, **kwargs):
		"""
		Обновление выборки объектов
		http PATCH -d {"id__in":[1, 5, 66, 4]} .../<params>/
		"""
		pass

	def destroy(self, request, **kwargs):
		"""
		Удаление объекта http DELETE
		"""
		self.get_model().delete()
		msg = 'success'
		return Response(
				{'msg': msg},
				status=status.HTTP_200_OK
			)
