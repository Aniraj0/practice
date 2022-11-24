"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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


#practice/practice/urls.py: Main urls.py


from django.contrib import admin
from django.urls import path, include
from practice_api import urls as practice_urls
from api import urls as api
from modelView import urls as modelView
from readModelView import urls as readView
from genericView import urls as genericView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('practice/', include(practice_urls)),
    path('api/', include(api)),
    path('modelView/', include(modelView)),
    path('readModelView/',include(readView)),
    path('genericView/',include(genericView)),

]
