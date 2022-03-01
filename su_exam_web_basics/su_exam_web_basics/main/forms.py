from django import forms

from su_exam_web_basics.main.models import Profile, Album

class BootstrapFieldMixin():
    fields = {}

    def _init_readonly_field(self):
        for _, field in self.fields.items():

            if hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})

                if 'readonly' not in field.widget.attrs:
                    field.widget.attrs['readonly'] = ''
                    field.widget.attrs['readonly'] += 'readonly'


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                },

            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age',
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):

        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        exclude = ('username_id',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },

            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'genre': forms.Select(
                choices=Album.CHOICES,
                attrs={
                    'placeholder': 'Genre',
                }
            )
            ,
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.URLInput(
            ),

            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price',
                }
            )
        }


class EditAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        exclude = ('username_id',)


class DeleteAlbumForm(forms.ModelForm, BootstrapFieldMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_readonly_field()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
        exclude = ('username_id',)
