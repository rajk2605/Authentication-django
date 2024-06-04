from django.contrib import admin
from django.urls import path
from auapp.views import ulogin, usignup, uhome, ulogout,ucpass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uhome,name="uhome"),
    path("ulogin",ulogin,name="ulogin"),
    path("usignup",usignup,name="usignup"),
    path("ulogout",ulogout,name="ulogout"),
    path("ucpass",ucpass,name="ucpass")
]
