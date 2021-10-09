from django.contrib import admin
from django.urls import path
from phyApp.views import home , about , hardware , detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('simulations/' , home ,  name='home' ),
    path('about/' , about , name='about'),
    path('video/' , hardware , name='hardware'),
    path('detail/<int:id>' , detail , name='detail'),

]
