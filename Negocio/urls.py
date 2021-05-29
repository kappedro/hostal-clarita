from django.urls import path
from .views import registro_cliente, listar_ordenes_compra, registro_orden_compra

urlpatterns = [
    path('registro/', registro_cliente, name='registro_cliente'),
    path('ordenes_compra/', listar_ordenes_compra, name='listar_ordenes_compra'),
    path('ordenes_compra/ingresar/', registro_orden_compra, name='registro_orden_compra'),
]
