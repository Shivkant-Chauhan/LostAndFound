from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('new-lost-item/', views.new_item, name="newitem"),
    path('category/<str:category>/', views.category_view, name = "category"),
    path('item/<int:item_id>/', views.item_view, name="item"),
    path('logout/', views.logout_view, name="logout"),
    path('found/', views.found, name="found"),
    path('my requests/', views.my_requests, name="my_requests"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
