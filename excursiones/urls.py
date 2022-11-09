from django.urls import path
from excursiones import views
from excursiones.views import excursionesList, excursionesCreacion ,excursionesDelete,excursionesUpdate,excursionesDetalle

urlpatterns = [
  
    path("Lista", excursionesList.as_view(), name="list-excursiones"),
    path("detail/<int:pk>/", excursionesDetalle.as_view(), name="detail-excursion"),
    path("create/", excursionesCreacion.as_view(), name="create-excursion"),
    path("update/<int:pk>/", excursionesUpdate.as_view(), name="update-excursion"),
    path("delete/<int:pk>", excursionesDelete.as_view(), name="delete-excursion"),
    
]