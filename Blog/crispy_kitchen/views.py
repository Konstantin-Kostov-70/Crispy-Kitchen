from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from Blog.core.utils import apply_likes_count, apply_user_liked_food
from Blog.crispy_blog.models import Post
from Blog.crispy_kitchen.forms import ReservationForm, MessageForm, NewsLetterForm
from Blog.crispy_kitchen.models import Reservation, Message, SpecialMenu, Menu, FoodLike, NewsLetter
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



UserModel = get_user_model()


class IndexView(views.ListView):
    model = SpecialMenu
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()

        foods = SpecialMenu.objects.all()

        foods = [apply_likes_count(food) for food in foods]
        foods = [apply_user_liked_food(food) for food in foods]

        best_foods = [food for food in foods if food.best_offers]

        context['foods'] = foods
        context['best_foods'] = best_foods

        return context


class MenuView(views.ListView):
    context_object_name = 'menus'
    model = Menu
    template_name = 'menu.html'


class AboutView(views.CreateView):
    model = NewsLetter
    form_class = NewsLetterForm
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = UserModel.objects.all()
        return context

    def form_valid(self, form):
        myform = form.save(commit=False)
        myform.user_id = self.request.user.pk
        form.save()
        return super(AboutView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class ContactView(views.CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse_lazy('index')


class ReservationView(SuccessMessageMixin,views.CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation.html'
    success_message = 'Your reservation has been successfully submitted'

    def get_success_message(self, cleaned_data):
        return self.success_message

    def get_success_url(self):
        return reverse_lazy('reservation')


def get_user_liked_foods(food_id, request):
    return FoodLike.objects.filter(food_id=food_id, user=request.user)


def like_food(request, food_id):
    user_liked_food = get_user_liked_foods(food_id, request)

    if user_liked_food:
        user_liked_food.delete()
    else:
        FoodLike.objects.create(
            food_id=food_id,
            user=request.user

        )

    redirect_path = request.META['HTTP_REFERER'] + f'#food-{food_id}'
    return redirect(redirect_path)



