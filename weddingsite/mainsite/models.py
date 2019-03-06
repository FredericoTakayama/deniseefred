from django.db import models
from django.urls import reverse
import uuid # Required for unique book instances

# import datetime

# Obs.: se precisar apagar o banco (limpar tudo, inclusive superuser):
# https://stackoverflow.com/questions/6485106/what-is-the-easiest-way-to-clear-a-database-from-the-cli-with-manage-py-in-djang
# issue com uuid:
# https://stackoverflow.com/questions/32445546/django-uuidfield-modelfield-causes-error-in-django-admin-badly-formed-hexadecim

# Create your models here.
class Guest(models.Model):
    """tabela convidado (metadata)"""

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular guest', editable=False)
    name = models.CharField(max_length=50, null=False, help_text='Nome', verbose_name='Nome')
    # for some reason last_name is named as lastname in postgree, so I'm renaming it from last_name to lastname
    lastname = models.CharField(max_length=100, null=False, help_text='Sobrenome', verbose_name='Sobrenome')
    genders = (
        ('m', 'Homem'),
        ('f', 'Mulher')
    )
    gender = models.CharField(max_length=2, choices=genders, null=False, help_text='Gênero', verbose_name='Gênero')
    address =  models.TextField(max_length=2000, null=True, blank=True)
    is_vip = models.BooleanField(default=False, null=False) # se eh padrinho/madrinha
    inviters = (
        ('m','noivo'),
        ('f','noiva')
    )
    invited_by = models.CharField(max_length=2, choices=inviters, null=False, verbose_name='Convidado pelo(a)')
    main_inviter = models.BooleanField(default=False, null=False)
    has_presence = models.BooleanField(default=False, null=False, help_text='Confirmar Presença', verbose_name='Confirmar Presença')
    # last_update = models.DateField(default=datetime.datetime.today, null=False)
    # lista de opções aqui com base no max_family
    max_family_quantity = models.IntegerField(default=1, null=False)
    num_of_people = [(i,i) for i in range(0,11)]
    family_quantity = models.IntegerField(default=1, choices=num_of_people, null=False, help_text='Total de pessoas que irão junto incluindo você', verbose_name='Número de pessoas')
    # babies_list = [i for i in range(0,self.max_family_quantity-1)]
    num_of_babies = models.IntegerField(default=0, choices=num_of_people, null=False, help_text='Número de crianças até 5 anos', verbose_name='Número de bebes')
    # children_list = [i for i in range(0,self.family_quantity-1-self.num_of_babies)]
    num_of_children = models.IntegerField(default=0, choices=num_of_people, null=False, help_text='Número de crianças entre 6 e 10 anos', verbose_name='Número de crianças')

    # Metadata
    class Meta: 
        ordering = ['id','has_presence', 'name'] # ordenado pela presença e pelo nome de A-Z (se quiser inverter colocar '-name')
    
    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Guest."""
        # return "/confirmation/guest/%i/" % self.id
        return reverse('guest', args=[self.id])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.id} ({self.name})'
        # return self.name
