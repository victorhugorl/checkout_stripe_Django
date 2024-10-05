from payment import views
from django.urls import path

urlpatterns = [
    path('', views.product_page, name='product_page' ),
    path('payment_successfull/',views.success_buy, name='payment_successful'),
    path('payment_cancelled/', views.cancelled_buy, name='payment_cancelled'),
    path('stripe_webhooks/', views.stripe_webhook, name='stripe_webhook'),
]
 
