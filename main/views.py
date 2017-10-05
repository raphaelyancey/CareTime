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


def host(request, host_slug):

    pickup_form = PickupForm()
    host = Host.objects.get(slug=host_slug)

    context = {
        'host': host,
        'pickup_form': pickup_form
    }

    if request.method == 'POST':
        form = PickupForm(request.POST)

        if form.is_valid():

            appointment = Appointment(host=host, scheduled_time=form.cleaned_data['pickup_time'])
            appointment.save()

            now = datetime.combine(date.min, datetime.now().time())
            scheduled = datetime.combine(date.min, appointment.scheduled_time)
            delay = now - scheduled

            print(now)
            print(scheduled)
            print(delay)

            context.update({
            'picked_up': True,
            'appointment': appointment,
            'delay': delay
            })

            return render(request, 'main/host.html', context)

    return render(request, 'main/host.html', context)
