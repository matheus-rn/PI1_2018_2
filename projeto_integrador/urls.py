from django.urls import path
from django.conf.urls import url
from projeto_integrador import views
from projeto_integrador.views import home

urlpatterns = [
    url(r'^medicamentos/',  views.MedicamentoViewSet.as_view()),
    url(r'^medicamentos/(?P<pk>[0-9]+)/$', views.MedicamentoDetailView.as_view()),
]
