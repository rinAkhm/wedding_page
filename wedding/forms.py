from django import forms


class WeddingForm(forms.Form):
    attendance = forms.ChoiceField(label='', required=True, choices=(
        (1, 'Я приду / Мы пиредем'),
        (2, 'Буду со своей парой'),
        (3, 'Не смогу прийти')
    ))
    name = forms.CharField(required=True, label='', min_length=2, max_length=30,
                           initial="Введите Имя", widget=forms.TextInput(attrs={"class": "input_filed"}))
    surname = forms.CharField(required=True, label='', min_length=2, max_length=50,
                              initial="Введите Фамилию", widget=forms.TextInput(attrs={"class": "input_filed"}))
    housing = forms.ChoiceField(required=True, label="Нужна ли помощь с размещением?", choices=(
        (1, 'Да'),
        (2, 'Нет')
    ))
    drinks = forms.MultipleChoiceField(label="Предпочтения по напиткам", choices=(
        (1, 'Вино'),
        (2, 'Шампанское'),
        (3, 'Водка'),
        (4, 'Коньяк'),
        (5, 'Виски')),
                                       widget=forms.CheckboxSelectMultiple(attrs={"class": "select_box"}), )
