from django.urls import path
from . import views # 5 agregamos nuestro aca vamos a integrar nuestro pat

urlpatterns = [
    path('', views.index, name='index'), #4 aca temos nuestra ruta

]
