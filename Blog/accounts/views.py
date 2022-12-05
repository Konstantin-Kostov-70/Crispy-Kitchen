from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from Blog.accounts.forms import ProfileLoginForm, ProfileCreateForm, ProfileEditForm
from Blog.crispy_kitchen.models import FoodLike

UserModel = get_user_model()


class SignUpView(views.CreateView):
    form_class = ProfileCreateForm
    template_name = 'user_sign_up.html'
    success_url = reverse_lazy('index')


class SignInView(auth_views.LoginView):
    form_class = ProfileLoginForm
    template_name = 'user_sign_in.html'
    next_page = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class ProfileDetailsView(views.DetailView):
    model = UserModel
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = FoodLike.objects.all()
        return context


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'user_edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.object.pk,
        })


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'user_delete_profile.html'
    success_url = reverse_lazy('index')




