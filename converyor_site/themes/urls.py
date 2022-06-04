from django.urls import path

from . import views

app_name = 'themes'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'themes/',
        views.themes,
        name='themes'
    ),
    path(
        'create/',
        views.theme_create,
        name='theme_create'
    ),
    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),
    path(
        'themes/<int:theme_id>/',
        views.theme_detail,
        name='theme_detail'
    ),
    path(
        'themes/<int:theme_id>/edit/',
        views.theme_edit,
        name='theme_edit'
    ),
    path(
        'themes/<int:theme_id>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'themes/<int:theme_id>/delete/',
        views.delete_theme,
        name='theme_delete'
    ),
]
