from django.urls import path
from .views import ListView 
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
	path('<str:model_name>', ListView.as_view({
			'get': 'list',
			'post': 'create'
		}), name='list-view'),
	
	path('<str:model_name>/<int:model_pk>', ListView.as_view({
			'get': 'retrieve',
			'put': 'update',
			'patch': 'partial_update',
			'delete': 'destroy'
		}), name='detail-view'),
])