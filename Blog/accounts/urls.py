from django.urls import path, include

from Blog.accounts.views import SignInView, SignOutView, \
    SignUpView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
    ])),
]