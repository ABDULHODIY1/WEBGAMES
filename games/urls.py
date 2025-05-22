# gamehub/urls.py
from django.contrib import admin
from django.urls import path
from games import views as game_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_views.game_list, name='game_list'),
    path('game/<int:game_id>/', game_views.game_detail, name='game_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
