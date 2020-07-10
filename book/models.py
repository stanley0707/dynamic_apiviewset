from django.db import models
from django.core.exceptions import ValidationError

def validate_not_empty(value):
	if value == '':
		raise ValidationError('%(value)s is empty!', params={'value':value})

class Book(models.Model):
	authors = models.ManyToManyField(
			'Author',
			related_name='author_books',
		)
	
	title = models.CharField(
			validators=[validate_not_empty],
			max_length=120,
			unique=True,
		)
	
	description = models.TextField()

	secret = models.CharField(
			max_length=50,
			blank=True
		)

	# Указываем поля сериализации DRF
	# для инкапсуляции скрытых значений прим. (secret)
	# Перечисленные поля данных будут ожидаться
	# расширением generic_apiview в качестве аргументов
	# для всех методов REST.
	serialize_fields = [
		'id', 'title', 'description', 'authors'
	]
	
	def __str__(self):
		return '{}, {}'.format(self.id, self.title)

	def save(self, *args, **kwargs):
		if self.title == '':
			raise ValidationError('title не можеьт быть пустым')
		super().save(*args, **kwargs)

class Author(models.Model):
	fullname = models.CharField(
			max_length=200,
			unique=True,
			validators=[validate_not_empty]
		)
	
	born_date = models.DateTimeField(
			blank=True,
			null=True
		)

	rip_date = models.DateTimeField(
			blank=True,
			null=True
		)

	secret = models.CharField(
			max_length=50,
			blank=True
		)
	
	serialize_fields = [
		'id', 'fullname', 'born_date', 'rip_date', 'author_books'
	]