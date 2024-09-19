from django.urls import path
from .views import AccountInfoListAPIView

urlpatterns = [
    path('me/', AccountInfoListAPIView.as_view(), name='account-info')
]
