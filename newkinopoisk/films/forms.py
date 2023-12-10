from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator

from films.models import Genres


#-----------------------------------работа со связкой с моделью -----------------
class SuggestGenreForm(forms.ModelForm):
    content = forms.CharField(
        max_length=200,
        required=False, widget=forms.Textarea(attrs={'cols': '40', 'rows': '10'}))
    class Meta:
        model = Genres
        fields = ['title', 'content', 'image']#'__all__'
        labels = {'title': 'Заголовок'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-text-area'})}

    def clean_content(self):  # clean_атрибут_формы, Django в момент валидации формы сам вызывает Form
        content = self.cleaned_data['content']
        if not ('А' in content) and content != '':
            raise ValidationError('А русская нет в строке')
        return content

    def clean_image(self):
        image = self.cleaned_data['image']
        if image.size > 50 * 1024:  #image.size - в байтах.  50 KB в байтах
            raise ValidationError("Размер файла слишком большой. Максимальный размер: 50KB.")
        return image

"""
#-----------------------------------работа без связки с моделью ---------------------------------
class alphaValidator:
    ALLOWED_CHARS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz "
    code = "russian"
    def __init__(self, message="Только буквы и пробел допустимы"):
        self.message = message

    def __call__(self, value):
        value = value.lower()
        if not(set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


# форма несвязанная с моделью
class SuggestGenreForm(forms.Form):
    # перечисляем поля формы
    title = forms.CharField(validators=[ MinLengthValidator(5, message="очень malo букв"), alphaValidator()] ,min_length=5, max_length=50) #error_messages={'min_length': 'nnnnnoooo!'})  #error_messages={'required': 'нельзя оставлять пустым',
                                           # 'min_length': 'очень malo букв'},  )# CharField поле для заполнения букв CharField(label="Заголовок")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': '40', 'rows': '10'}), max_length=300, required=False)
    # photo = forms.FileField(required=False)
    # checkbox = forms.BooleanField()
    # list_box = forms.ModelChoiceField(queryset=Films.objects.all())
    def clean_title(self): # clean_атрибут_формы, Django в момент валидации формы сам вызывает Form
        title = self.cleaned_data['title']
        if not('А' in title):
            raise ValidationError('А русская нет в строке')
        return title


"""

