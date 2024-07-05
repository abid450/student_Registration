"""
URL configuration for two project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from yellow.views import Y_llow
from yellow.views import yellow_re
from yellow.views import registration
from yellow.views import Register_re
from yellow.views import softTect_L
from yellow.views import change_password
from yellow.views import Change_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('softTech',Y_llow),
    path('yellow_re',yellow_re),
    path('registration',registration, name='register'),
    path('Register_r_re',Register_re),
    path('softTect_L',softTect_L,name='login'),
    path('Change_pass',change_password,name='change_p'),
    path('Change__userp',Change_user,name='change_u'),

]
