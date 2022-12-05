from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class ProfileLoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True, "placeholder": "Crispy_Kitchen",
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "placeholder": "Min 6 charaters long"}),
    )


class ProfileCreateForm(auth_forms.UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'type': 'password',
                   'align': 'center',
                   'placeholder': 'Min 8 charaters long'}),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'type': 'password',
                   'align': 'center',
                   'placeholder': 'Enter the same password'}),
    )

    photo = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Chose file'}),
    )

    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name',
                  'date_of_birth', 'email', 'phone',
                  'profession', 'photo')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Your Username",
                }
            ),

            'first_name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Your First Name",
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Your Last Name",
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Email",
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "10/10/2010",
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "123-456-7890",
                }
            ),

            'profession': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Your Profession",
                }
            ),
        }


class ProfileEditForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'type': 'password',
                   'align': 'center',
                   'placeholder': 'Min 8 charaters long'}),
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'type': 'password',
                   'align': 'center',
                   'placeholder': 'Enter the same password'}),
    )

    photo = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter the same password'}),
    )

    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name',
                  'date_of_birth', 'email', 'phone',
                  'profession', 'photo')

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Your Username",
                }
            ),

            'first_name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Your First Name",
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Your Last Name",
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Email",
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "10/10/2010",
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "123-456-7890",
                }
            ),

            'profession': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Your Profession",
                }
            ),
        }
