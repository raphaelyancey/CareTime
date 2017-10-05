from django.shortcuts import render
from .models import *
from .forms import *
from datetime import datetime, date


def index(request):

    # Only get top-level organizations
    organizations = Organization.objects.filter(parent_organization=None)

    context = {
        'organizations': organizations
    }

    return render(request, 'main/index.html', context)


def organization(request, org_slug):

    organization = Organization.objects.get(slug=org_slug)

    context = {
        'organization': organization
    }

    return render(request, 'main/organization.html', context)


def host_admin(request, host_slug):

    pickup_form = PickupForm()
    host = Host.objects.get(slug=host_slug)

    context = {
        'host': host,
        'pickup_form': pickup_form
    }

    if request.method == 'POST':
        form = PickupForm(request.POST)

        if form.is_valid():

            pickup_time = datetime.now().replace(microsecond=0).time()
            pickup_date = datetime.combine(date.min, pickup_time)
            scheduled_time = form.cleaned_data['pickup_time']
            scheduled_date = datetime.combine(date.min, scheduled_time)

            appointment = Appointment(host=host, scheduled_time=scheduled_time, pickup_time=pickup_time)
            appointment.save()

            delay = pickup_date - scheduled_date

            context.update({
                'picked_up': True,
                'appointment': appointment,
                'delay': delay
            })

            return render(request, 'main/host_admin.html', context)

    return render(request, 'main/host_admin.html', context)


def host_front(request, host_slug):

    host = Host.objects.get(slug=host_slug)

    last_appointment = Appointment.objects.filter(host=host).latest(field_name='pickup_time')

    pickup_date = datetime.combine(date.min, last_appointment.pickup_time)
    scheduled_date = datetime.combine(date.min, last_appointment.scheduled_time)
    delay = pickup_date - scheduled_date

    context = {
        'host': host,
        'delay': delay
    }

    return render(request, 'main/host_front.html', context)