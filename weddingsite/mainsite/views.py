from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from mainsite.models import Guest
from datetime import datetime, timedelta
from mainsite.forms import GuestForm, ConfirmationForm

# Create your views here.
# def save_the_date():
#     # Save the date
#     save_the_date = datetime(2019,10,26)
#     date_now = datetime.now()
#     remaining_days = abs((save_the_date - date_now).days)

#     return (save_the_date, remaining_days)

def index(request):
    """View function for home page of site."""

    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = ConfirmationForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            guest = form.cleaned_data['password']

            return HttpResponseRedirect(guest.get_absolute_url())
        else:
            context = {
                'form': form,
                'save_the_date': save_the_date.strftime("%d.%m.%Y"),
                'remaining_days': remaining_days,
            }
            # Render the HTML template index.html with the data in the context variable
            return render(request, 'index.html', context=context)
    else:
        form = ConfirmationForm(initial={'name': 'Adam Sandler'})

        context = {
            'form': form,
            'save_the_date': save_the_date.strftime("%d.%m.%Y"),
            'remaining_days': remaining_days,
        }

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'index.html', context=context)

def bride_and_groom(request):
    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    context = {
        'save_the_date': save_the_date.strftime("%d.%m.%Y"),
        'remaining_days': remaining_days,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'bride_and_groom.html', context=context)

def save_the_date(request):
    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    context = {
        'save_the_date': save_the_date.strftime("%d.%m.%Y"),
        'remaining_days': remaining_days,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'save_the_date.html', context=context)

def gifts(request):
    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    context = {
        'save_the_date': save_the_date.strftime("%d.%m.%Y"),
        'remaining_days': remaining_days,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'gifts.html', context=context)

def e_gifts(request):
    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    context = {
        'save_the_date': save_the_date.strftime("%d.%m.%Y"),
        'remaining_days': remaining_days,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'e_gifts.html', context=context)

def cerimony_and_reception(request):
    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    context = {
        'save_the_date': save_the_date.strftime("%d.%m.%Y"),
        'remaining_days': remaining_days,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'cerimony_and_reception.html', context=context)

def tips(request):
    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    context = {
        'save_the_date': save_the_date.strftime("%d.%m.%Y"),
        'remaining_days': remaining_days,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tips.html', context=context)

def confirmation(request):
    # Save the date
    save_the_date = datetime(2019,10,26)
    date_now = datetime.now()
    remaining_days = abs((save_the_date - date_now).days)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = ConfirmationForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            guest = form.cleaned_data['password']

            # form = GuestForm(initial={
            #     'full_name': full_name,
            #     'family_quantity' : guest.family_quantity,
            #     'num_of_babies': guest.num_of_babies,
            #     'num_of_children': guest.num_of_children,
            #     'has_presence': guest.has_presence,
            #     # 'has_presence': 'n', # se for utilizar como um select box
            #     })

            # context = {
            #     # 'num_guests': num_guests,
            #     # 'num_of_guests_confirmed': num_of_guests_confirmed,
            #     'form': form,
            #     'guest': guest,
            #     'valid_guest': 'True',
            #     'save_the_date': save_the_date.strftime("%d.%m.%Y"),
            #     'remaining_days': remaining_days,
            # }

            # Render the HTML template index.html with the data in the context variable
            # return render(request, 'guest.html', context=context) # se fizer assim continua na mesma url! não serve!

            # redirect to a new URL:
            # print(guest.get_absolute_url())
            # HttpResponseRedirect retonar um 302 desejado pela view, e o guest.get_absolute_url() fornece a
            # url desejada para o guest em detalhes!

            return HttpResponseRedirect(guest.get_absolute_url())
        else:
            context = {
                'form': form,
                'save_the_date': save_the_date.strftime("%d.%m.%Y"),
                'remaining_days': remaining_days,
            }

            # Render the HTML template index.html with the data in the context variable
            return render(request, 'confirmation.html', context=context)
    else:
        form = ConfirmationForm(initial={'name': 'Adam Sandler'})

        # Render the HTML template index.html with the data in the context variable
        context = {
            'form': form,
            'valid_guest': 'False',
            'save_the_date': save_the_date.strftime("%d.%m.%Y"),
            'remaining_days': remaining_days,
        }

        return render(request, 'confirmation.html', context=context)

def guest(request, uuid):
    # exemplo:
    # http://127.0.0.1:8000/confirmation/guest/0e0ff50f-2495-454e-bec6-b68b31bdf314/
    try:
        guest = Guest.objects.get(id=uuid)

        # Save the date
        save_the_date = datetime(2019,10,26)
        date_now = datetime.now()
        remaining_days = abs((save_the_date - date_now).days)

        if request.method == 'POST':
            # Create a form instance and populate it with data from the request (binding):
            form = GuestForm(request.POST)
            form.id = uuid

            # Check if the form is valid:
            if form.is_valid():
                # atualizando banco de dados
                # print(form.cleaned_data['has_presence'])
                guest.has_presence = form.cleaned_data['has_presence']
                guest.family_quantity = form.cleaned_data['family_quantity']
                guest.num_of_babies = form.cleaned_data['num_of_babies']
                guest.num_of_children = form.cleaned_data['num_of_children']
                guest.message = form.cleaned_data['message']
                guest.last_update = datetime.today()
                guest.save()

                context = {
                    'guest': guest,
                    'save_the_date': save_the_date.strftime("%d.%m.%Y"),
                    'remaining_days': remaining_days,
                }

                return render(request, 'thanks.html', context=context)

                # redirect to a new URL:
                # return HttpResponseRedirect(reverse('thanks'))

            else:
                context = {
                    'form': form,
                    'guest': guest,
                    'save_the_date': save_the_date.strftime("%d.%m.%Y"),
                    'remaining_days': remaining_days,
                }

                # Render the HTML template index.html with the data in the context variable
                return render(request, 'guest.html', context=context)                
        
        # parte da view GET:
        else:
            # print('template get!')
            form = GuestForm(initial={
                'id' : uuid,
                # 'full_name': f'{guest.name} {guest.lastname}',
                'family_quantity' : guest.family_quantity,
                'num_of_babies': guest.num_of_babies,
                'num_of_children': guest.num_of_children,
                'has_presence': guest.has_presence,
                # 'has_presence': 'n', # se for utilizar como um select box
                })
            
            #     num_guests = Guest.objects.all().count()
            #     num_of_guests_confirmed = Guest.objects.filter(has_presence__exact='True').count()

            context = {
                # 'num_guests': num_guests,
                # 'num_of_guests_confirmed': num_of_guests_confirmed,
                'form': form,
                'guest': guest,
                'save_the_date': save_the_date.strftime("%d.%m.%Y"),
                'remaining_days': remaining_days,
            }

            # Render the HTML template index.html with the data in the context variable
            return render(request, 'guest.html', context=context)

    except Guest.DoesNotExist:
        raise Http404('Book does not exist')

# def thanks(request):
#      # Save the date
#     save_the_date = datetime(2019,10,26)
#     date_now = datetime.now()
#     remaining_days = abs((save_the_date - date_now).days)
    
#     request.session['my_car'] = 'mini'

#     context = {
#         # 'num_guests': num_guests,
#         # 'num_of_guests_confirmed': num_of_guests_confirmed,
#         # 'guest': guest,
#         'save_the_date': save_the_date.strftime("%d.%m.%Y"),
#         'remaining_days': remaining_days,
#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'thanks.html', context=context)

