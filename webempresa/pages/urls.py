from django.urls import path
from . import views

urlpatterns = [
    # path del blog

    path('<int:page_id>/', views.page, name="page"),

]
