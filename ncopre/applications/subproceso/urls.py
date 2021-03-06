from django.conf.urls import url, include

# local
from . import views

urlpatterns = [

    #url para gregar sub proceso
    url(
        r'^sub-proceso/agregar/(?P<pk>\d+)/$',
        views.SubProcessAddView.as_view(),
        name='subproceso_add'
    ),


    #url para agregar factura
    url(
        r'^factura/agregar/(?P<pk>\d+)/$',
        views.SubProcessVoucherFactura.as_view(),
        name='factura_add'
    ),
    #servicio para unidad de negocio
    url(
        r'^',
        include(
            'applications.subproceso.services_urls',
            namespace="subproceso_services_url"
        )
    ),
]
