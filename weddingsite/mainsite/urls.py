from django.urls import path
from . import views
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('save_the_date/', views.save_the_date, name='save_the_date'),
    path('bride_and_groom/', views.bride_and_groom, name='bride_and_groom'),
    path('cerimony_and_reception/', views.cerimony_and_reception, name='cerimony_and_reception'),
    path('tips/', views.tips, name='tips'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('e_gifts/', views.e_gifts, name='e_gifts'),
    path('gifts/', views.gifts, name='gifts'),
    path('confirmation/guest/<uuid:uuid>/', views.guest, name='guest'),
    # path('confirmation/thanks/', views.thanks, name='thanks'),
    #Add URL maps to redirect the base URL to our application
    path('', RedirectView.as_view(url='/index/', permanent=True)),
]