from django import forms
from Blog.crispy_kitchen.models import Reservation, Message, FoodComment, NewsLetter


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Your Name",
                },
            ),

            'email': forms.EmailInput(
                attrs={
                    'pattern': "[^ @]*@[^ @]*",
                    'class': "form-control",
                    'placeholder': "your@email.com"
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'pattern': "[0-9]*",
                    'class': "form-control",
                    'placeholder': "123-456-7890",
                }
            ),

            'number_of_person': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "12 person",
                }
            ),

            'date': forms.DateInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "10/10/2010",
                }
            ),

            'time': forms.Select(
                attrs={
                    'class': "form-control",
                    'placeholder': "5:00 PM",
                }
            ),
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Name',
                }
            ),

            'email': forms.EmailInput(
                attrs={

                    'class': "form-control",
                    'placeholder': "your@email.com"
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "123-456-7890",
                }
            ),

            'message': forms.Textarea(
                attrs={

                    'class': "form-control",
                    'placeholder': "Your Message",
                }
            ),
        }


class FoodCommentForm(forms.ModelForm):
    class Meta:
        model = FoodComment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write a comment'
                }
            ),
        }


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Your email address',
                    'class': 'form-control'
                }
            )
        }