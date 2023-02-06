from django.contrib import admin
from django.urls import path

from todo.views import TodosAPIView, TodoAPIView, DoneTodosAPIView, DoneTodoAPIView
from todo.views import CreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo', TodosAPIView.as_view()),
    path('todo/<int:pk>', TodoAPIView.as_view()),
    path('done', DoneTodosAPIView.as_view()),
    path('done/<int:pk>', DoneTodoAPIView.as_view()),
    path('api/books/', CreateView.as_view())
]

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Swagger Study API",
        default_version="v1",
        description="Swagger Study를 위한 API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="test", email="dhkep03@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    schema_view.without_ui(cache_timeout=0), name="schema-json"),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
    name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
    name='schema-redoc'), ]