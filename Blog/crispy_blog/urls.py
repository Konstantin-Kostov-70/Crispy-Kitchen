from django.urls import path

from Blog.crispy_blog.views import NewsDetailsView, MenuDetailView, SpecialMenuDetailView

urlpatterns = [
    path('news-detail/<int:pk>/', NewsDetailsView.as_view(), name='news detail'),
    path('menu-detail/<int:pk>', MenuDetailView.as_view(), name='menu detail'),
    path('special-menu-detail/<int:pk>', SpecialMenuDetailView.as_view(), name='special menu detail'),

]