from django.urls import path
from . import views

urlpatterns = [
    path('report/retail', views.ecommerce_report_page, name='retail_report'),
]
