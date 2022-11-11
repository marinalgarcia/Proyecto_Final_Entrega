"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', index, name="index-blog"),
    path('admin/', admin.site.urls),
    path('signup/', BlogSignUp.as_view(), name="blog-signup"),
    path('login/', BlogLogin.as_view(), name="blog-login"),
    path('list/', ListPost.as_view(), name="list-post"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    path('create/', CreatePost.as_view(), name="create-post"),
    path('update/<int:pk>/', UpdatePost.as_view(), name="update-post"),
    path('delete/<int:pk>', DeletePost.as_view(), name="delete-post"),
    path('detail/<int:pk>/', DetailPost.as_view(), name="detail-post"),    
    path('excursiones/', include('excursiones.urls')),
    path('about/', about),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
    path('search-by-name/', SearchPostByName.as_view(), name="search-by-name-post"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

