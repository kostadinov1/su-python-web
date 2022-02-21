import os
from django import forms
from exam_prep_1.main_app.models import Profile, Expenses


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image'
        }


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
        labels = {
            'budget': 'Budget',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image'
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        image_path = self.instance.image.path
        # delete and then remove just in case of exception
        # if you can't delete the profile you shouldn't delete the image, right?
        Expenses.objects.all().delete()
        self.instance.delete()
        os.remove(image_path)

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class DeleteExpenseForm(forms.ModelForm):

    # this is the way to disable all the fields in the model in one go
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is a dictionary bro
        for _, field in self.fields.items():
            # if the property is 'disabled' will not be sent to the form?
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expenses
        fields = '__all__'


