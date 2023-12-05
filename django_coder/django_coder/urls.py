from django.contrib import admin
from django.urls import path, include
from django_coder.views import pag_principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pag_principal, name="principal"),
    # URLs de apps:
    path('stock/', include('stock.urls')),
    path('ventas/', include('ventas.urls'))
]
