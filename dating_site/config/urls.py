from config import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients/', include('register_user.urls')),
    path('api/clients/', include('match_users.urls')),
    path('api/', include('list_users.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]


urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
