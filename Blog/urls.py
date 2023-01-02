
from django.urls import path
from Blog import views

urlpatterns = [
    path("", views.inicio,name='Inicio'),
    path("Familiares/", views.FamiliaresList.as_view(),name='Familiares'),
    path("FamiliaresApi/", views.familiaresapi),
    path("Amigos/", views.AmigosList.as_view(),name='Amigos'),
    path("AmigosApi/", views.amigosapi),
    path("Referidos/", views.ReferidosList.as_view(),name='Referidos'),
    path("ReferidosApi/", views.referidosapi),
    path("busquedaFamiliares/", views.buscarfamiliar),
    path("buscar/", views.buscar),
    path("familiares/list/", views.FamiliaresList.as_view(),name='List'),
    path("familiares/create/", views.FamiliaresCreate.as_view(),name='New'),
    path("familiares/edit/<pk>", views.FamiliaresEdit.as_view(),name='Edit'),
    path("familiares/detail/<pk>", views.FamiliaresDetail.as_view(),name='Detail'),
    path("familiares/delete/<pk>", views.FamiliaresDelete.as_view(),name='Delete'),
    path("amigos/list/", views.AmigosList.as_view(),name='List2'),
    path("amigos/create/", views.AmigosCreate.as_view(),name='New2'),
    path("amigos/edit/<pk>", views.AmigosEdit.as_view(),name='Edit2'),
    path("amigos/detail/<pk>", views.AmigosDetail.as_view(),name='Detail2'),
    path("amigos/delete/<pk>", views.AmigosDelete.as_view(),name='Delete2'),
    path("referidos/list/", views.ReferidosList.as_view(),name='List3'),
    path("referidos/create/", views.ReferidosCreate.as_view(),name='New3'),
    path("referidos/edit/<pk>", views.ReferidosEdit.as_view(),name='Edit3'),
    path("referidos/detail/<pk>", views.ReferidosDetail.as_view(),name='Detail3'),
    path("referidos/delete/<pk>", views.ReferidosDelete.as_view(),name='Delete3'),
    path("busquedaAmigos/", views.buscaramigo),
    path("otrabusqueda/", views.otrabusqueda),
    path("busquedaReferidos/", views.buscarreferido),
    path("otrabusqueda_2/", views.otrabusqueda_2),
    



]