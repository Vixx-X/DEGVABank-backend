"""degvabank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import user_passes_test

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

def apidocs_view_permission(user):
    "User can read or se the api documentation if it is staff"
    return user.is_staff

docs_urls = [
    # documentation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # optional ui:
    path(
        "",
        user_passes_test(apidocs_view_permission)(
            SpectacularSwaggerView.as_view(url_name="schema")
        ),
        name="default-docs",
    ),
    path(
        "swagger-ui/",
        user_passes_test(apidocs_view_permission)(
            SpectacularSwaggerView.as_view(url_name="schema")
        ),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        user_passes_test(apidocs_view_permission)(
            SpectacularRedocView.as_view(url_name="schema")
        ),
        name="redoc",
    ),
]


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # user
    path('', include(('degvabank.apps.user.urls', "degvabank.apps.user"), namespace="user")),

    # account
    path('', include(('degvabank.apps.account.urls', "degvabank.apps.account"), namespace="account")),

    # card
    path('', include(('degvabank.apps.card.urls', "degvabank.apps.card"), namespace="card")),

    # transaction
    # path('', include(('degvabank.apps.transaction.urls', "degvabank.apps.transaction"), namespace="transaction")),

    # docs
    path('docs/', include(docs_urls)),
]
