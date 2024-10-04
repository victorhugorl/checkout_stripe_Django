from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('payment/', include('payment.urls')),
    path('admin/', admin.site.urls),
]
