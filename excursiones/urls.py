from django.urls import path
from excursiones import views
from excursiones.views import ExcursionesList, ExcursionesCreacion ,ExcursionesDelete,ExcursionesUpdate,ExcursionesDetalle

urlpatterns = [
  
    path("lista", ExcursionesList.as_view(), name="list-excursiones"),
    path("detail/<int:pk>/", ExcursionesDetalle.as_view(), name="detail-excursion"),
    path("create/", ExcursionesCreacion.as_view(), name="create-excursion"),
    path("update/<int:pk>/", ExcursionesUpdate.as_view(), name="update-excursion"),
    path("delete/<int:pk>", ExcursionesDelete.as_view(), name="delete-excursion"),
    
]