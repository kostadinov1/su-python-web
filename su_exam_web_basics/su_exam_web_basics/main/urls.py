from django.urls import path

from su_exam_web_basics.main.views import show_home, show_add_album, show_edit_album, show_delete_album, \
    show_album_details, show_profile_details, show_profile_delete, show_create_profile

urlpatterns = [
    path('', show_home, name='show home with profile'),
    path('album/add/', show_add_album, name='show add album'),
    path('album/edit/<int:pk>', show_edit_album, name='show edit album'),
    path('album/delete/<int:pk>', show_delete_album, name='show delete album'),
    path('album/details/<int:pk>', show_album_details, name='show album details'),
    path('profile/create/', show_create_profile, name='show home no profile'),
    path('profile/details/', show_profile_details, name='show profile'),
    path('profile/delete/', show_profile_delete, name='show delete profile'),
]