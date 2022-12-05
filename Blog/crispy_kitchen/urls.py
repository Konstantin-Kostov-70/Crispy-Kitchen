from django.urls import path

from Blog.crispy_kitchen.views import ReservationView, ContactView, IndexView, MenuView, like_food, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('like/<int:food_id>/', like_food, name='like food'),

]