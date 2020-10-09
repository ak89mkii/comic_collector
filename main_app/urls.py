from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comics/', views.comics_index, name='index'),
    path('comics/<int:comic_id>/', views.comics_detail, name='detail'),
    path('comics/create/', views.ComicCreate.as_view(), name='comics_create'),
    path('comics/<int:pk>/update/', views.ComicUpdate.as_view(),name='comics_update'),
    path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comics_delete'),
    path('comics/<int:comic_id>/add_reading/', views.add_reading, name='add_reading'),

    # NEW
    path('collectables/', views.CollectableList.as_view(), name='collectables_index'),
    path('collectables/<int:pk>/', views.CollectableDetail.as_view(), name='collectables_detail'),
    path('collectables/create/', views.CollectableCreate.as_view(), name='collectables_create'),
    path('collectables/<int:pk>/update/', views.CollectableUpdate.as_view(), name='collectables_update'),
    path('collectables/<int:pk>/delete/', views.CollectableDelete.as_view(), name='collectables_delete'),
    path('comics/<int:comic_id>/assoc_collectable/<int:collectable_id>/', views.assoc_collectable, name='assoc_collectable'),
    path('accounts/signup/', views.signup, name='signup'),
    
]