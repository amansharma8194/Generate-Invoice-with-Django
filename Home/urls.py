from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard_page'),
    path('logout/', logout_page, name='logout_page'),
    path('add_invoice/', add_invoice, name='add_invoice_page'),
    path('service_provider/', service_provider_page, name='service_provider_page'),
    path('update_service_provider/<int:id>', update_service_provider, name='update_service_provider_page'),
    path('delete_service_provider/<int:id>', delete_service, name='delete_service'),
    path('review/', review_invoices, name="review_invoices"),
    path('update_client/<int:id>/', update_client, name='update_client_page'),
    path('delete_client/<int:id>/', delete_client, name='delete_client'),
    path('review/<int:id>/', review_invoice, name='review_invoice_page'),
    path('update_service/<int:id>/', update_service, name='update_service_page'),
    path('delete_service/<int:id>/', delete_service, name='delete_service'),
    path('all_invoice/', all_invoice, name='all_invoice_page'),
    path('invoice_page/<int:id>', invoice_report, name='invoice_page')
]
