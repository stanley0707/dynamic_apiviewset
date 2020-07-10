from django.apps import apps


def get_model_from_any_apps(model_name):
	"""
	Забираем одну модель из приложения
	"""
	for app_label in apps.get_app_configs():
		try:
			return app_label.get_model(model_name)
		except LookupError:
			pass

def get_prams_construct(request):
	"""
	Здесь можно как-то валидировать
	входящии параметры и собирать новый массив
	параметров, что-б неотправлять невалидированный
	реквест в фильтр.
	"""
	return {k: v for k, v in request.GET.items()}