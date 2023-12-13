from django.contrib import admin
from django.urls import path, include
from django_coder.views import pag_principal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pag_principal, name="principal"),
    # URLs de apps:
    path('stock/', include('stock.urls')),
    path('ventas/', include('ventas.urls')),
    path('usuarios/', include('usuarios.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
