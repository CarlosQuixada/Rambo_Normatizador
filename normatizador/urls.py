from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^normatizar/$', views.NormatizadorList.as_view()),
]