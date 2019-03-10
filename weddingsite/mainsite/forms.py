from django import forms
from mainsite.models import Guest
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ConfirmationForm(forms.Form):
    # full_name = forms.CharField(label='Nome Completo')
    password = forms.CharField(label='Entre com a senha fornecida no convite')

    # # para validar algum campo, o nome da função de validação precisa começar com clean_<nome do campo>
    # def clean_full_name(self):
    #     # fetch guest
    #     full_name = self.cleaned_data['full_name']
    #     # print(full_name)
    #     guests = Guest.objects.all()
    #     for guest in guests:
    #         guest_full_name  = guest.name + ' ' + guest.lastname
    #         # print(guest_full_name)
    #         if (guest_full_name == full_name):
    #             return guest
    #     raise ValidationError(_('Nome inválido - nome não consta na lista de presença (está escrito idêntico ao convite?)'))

    def clean_password(self):
        password = self.cleaned_data['password']
        try:
            guest = Guest.objects.get(password=password)
        except:
            raise ValidationError(_('Senha inválida - por favor, se atente com as letras maiúsculas e minusculas'))
        return guest

class GuestForm(forms.Form):
    # full_name = forms.CharField(label='Nome Completo')
    id = forms.UUIDField(required=False)
    family_quantity = forms.IntegerField(label='Total de pessoas que irão junto incluindo você:')
    num_of_babies = forms.IntegerField(label='Destas, quantas são menores que cinco anos de idade:')
    num_of_children = forms.IntegerField(label='E quantas estão entre 5 e 10 anos de idade:')
    has_presence = forms.BooleanField(label='Confirmar presença', required=False)
    message = forms.CharField(widget=forms.Textarea, label='Deixe aqui sua mensagem aos noivos', required=False)

    # também da pra fazer por lista de opções. Para trazer o valor do banco é necessário declarar
    # as condições inicias na instancia desta classe no views.py:
    # segue exemplo:
    # form = GuestForm(initial={
    #     'family_quantity' : guest.family_quantity,
    #     'num_of_babies': guest.num_of_babies,
    #     'num_of_children': guest.num_of_children,
    #     # 'has_presence': guest.has_presence,
    #     'has_presence': 'n',
    # })
    # e aqui no forms.py:
    # presence_choices = (
    #     ('y', 'Confirmado'),
    #     ('n', 'Não Confirmado'),
    # )
    # has_presence = forms.ChoiceField(label='Confirmar Presença', choices=presence_choices)

    # validação:
    def fetch_guest(self):
        guest = Guest.objects.filter(id__exact=self.id).first()
        # print(guest)
        # print(type(guest))
        return guest

    def clean_num_of_babies(self):
        num_of_babies = self.cleaned_data['num_of_babies']
        if num_of_babies >= 0:
            return num_of_babies
        else:
            raise ValidationError(_('Número inválido - deve ser maior ou igual a 0'))
    
    def clean_num_of_children(self):
        num_of_children = self.cleaned_data['num_of_children']
        if num_of_children >= 0:
            return num_of_children
        else:
            raise ValidationError(_('Número inválido - deve ser maior ou igual a 0'))

    def clean_family_quantity(self):
        # print(self.id)
        # id = self.cleaned_data['id']
        guest = self.fetch_guest()

        family_quantity = self.cleaned_data['family_quantity']
        # como resgatar dados dos outros campos para fazer uma validação multipla?
        # data = self.get_initial()
        # print(data)
        # num_of_children = self.clean_num_of_children()
        # num_of_babies = self.clean_num_of_babies()

        # guest = Guest.objects.get(max_family_quantity)
        max_family_quantity = getattr(guest, 'max_family_quantity')
        # print(max_family_quantity)
        if family_quantity <= 0:
            raise ValidationError(_('Numero inválido - deve ser no mínimo maior que 0'))
        elif family_quantity > max_family_quantity:
            raise ValidationError(_('Numero inválido - deve ser no mínimo maior que 0 e menor ou igual a ' + str(max_family_quantity)))
        # elif (num_of_children + num_of_babies) >= family_quantity:
        #     raise ValidationError(_('Numero inválido - total de pessoas deve ser maior que o número de crianças'))
        else:
            return family_quantity

    def clean_has_presence(self):
        return self.cleaned_data['has_presence']
    
    def clean_id(self):
        id = self.cleaned_data['id']
        return id

    def clean_message(self):
        return self.cleaned_data['message']
