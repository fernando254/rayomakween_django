from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    url(r'^api/mecanicos/$', views.MecanicoViewSet.as_view()),
    url(r'^api/categorias/$', views.CategoriaViewSet.as_view()),
    url(r'^api/buscar_mecanico/(?P<nombre>.+)/$', views.MecanicoBuscarViewSet.as_view()),
    
]


urlpatterns=format_suffix_patterns(urlpatterns)
