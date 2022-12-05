from django.contrib import admin

from Blog.crispy_kitchen.models import Message, Reservation, Menu, SpecialMenu, FoodComment, NewsLetter


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class NormalMenuAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecialMenu)
class SpecialMenuAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodComment)
class FoodCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    pass


