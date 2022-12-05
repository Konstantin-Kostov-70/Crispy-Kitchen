from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic.edit import FormMixin

from Blog.crispy_blog.models import Post
from Blog.crispy_kitchen.forms import FoodCommentForm
from Blog.crispy_kitchen.models import FoodComment, Menu, SpecialMenu

UserModel = get_user_model()


class NewsDetailsView(FormMixin, views.DetailView):
    model = Post
    template_name = 'news-detail.html'
    form_class = FoodCommentForm

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FoodCommentForm()
        context['comments'] = FoodComment.objects.all()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        post = self.get_object()
        myform = form.save(commit=False)
        myform.post = post
        myform.user_id = self.request.user.pk
        form.save()
        return super(NewsDetailsView, self).form_valid(form)


class MenuDetailView(views.DetailView):
    model = Menu
    template_name = 'menu_detail.html'


class SpecialMenuDetailView(views.DetailView):
    model = SpecialMenu
    template_name = 'special_menu_detail.html'






