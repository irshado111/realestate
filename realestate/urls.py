"""
URL configuration for realestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from myapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log',views.log,name='log'),
    path('',views.mainview,name='main'),
    path('catagory',views.catagory,name='cata'),
    path('register',views.register,name='reg'),
    path('sell',views.sell,name='sell'),
    path('property/<int:id>',views.property,name='property'),
    path('logout',views.logoutpg,name='lgout'),
    path('profileview',views.profileview,name='profv'),
    path('deletesell/<int:id>',views.deletesell,name='deletesell'),
    path('udateprof/<int:id>',views.edit,name='updateprof'),
    path('update/<int:id>',views.updatepro,name='updatesave'),
    path('viewpropdetailes/<int:id>',views.viewpropertydetailes,name='viewpropertydeatai'),
    path('land',views.land,name='land'),
    path('building',views.building,name='building'),
    path('flat',views.flat,name='flat'),
    path('search1',views.search,name='search1'),
    # path('chat<int:id>',views.chat,name='chat'),
    # path('chatview',views.chatview,name='chatview')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

