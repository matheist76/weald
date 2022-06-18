from django.urls import path
from . import views

app_name = 'ground'
urlpatterns = [
    path('', views.index),
    path('index.html', views.index, name='index'),
    path('gm.html', views.gm, name='gm'),
    path('player.html', views.player, name='player'),
    path('settings.html', views.settings, name='settings'),
    path('drives.html', views.drives, name='drives'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('drivesadd.html', views.add_drive, name='add_drive'),
    path('main.html', views.get_page, name='main'),
]
