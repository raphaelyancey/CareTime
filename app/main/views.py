from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime, date, timedelta, time
from numpy import mean
from django.contrib.auth.hashers import check_password


def about(request):
    return render(request, 'main/about.html', {})


def signup(request):
    return render(request, 'main/signup.html', {})


def index(request):

    # Only get top-level organizations
    organizations = Organization.objects.filter(parent_organization=None)

    context = {
        'organizations': organizations
    }

    return render(request, 'main/index.html', context)


def organization(request, org_slug):

    organization = Organization.objects.get(slug=org_slug)

    def get_all_host(organization):
        hosts = organization.host_set.all()
        print(hosts)
        for child_org in organization.organization_set.all():
            hosts = hosts | get_all_host(child_org)
            print("child: " + str(hosts))
        return hosts

    all_hosts = get_all_host(organization)

    context = {
        'organization': organization,
        'all_hosts': all_hosts.order_by('last_name'),
        'all_hosts_count': len(all_hosts)
    }

    return render(request, 'main/organization.html', context)


def host_admin(request, host_slug):

    if request.session.get('logged_user') is None:
        return redirect('host_login', host_slug=host_slug)

    pickup_form = PickupForm()
    host = Host.objects.get(slug=host_slug)
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    context = {
        'host': host,
        'all_day_appointments': host.appointment_set.filter(created_at__gte=today).order_by('-scheduled_time'),
        'pickup_form': pickup_form
    }

    if request.method == 'POST':
        form = PickupForm(request.POST)

        if form.is_valid():

            pickup_time = datetime.now().replace(microsecond=0).time()
            pickup_date = datetime.combine(date.min, pickup_time)
            scheduled_time = form.cleaned_data['scheduled_time']
            scheduled_date = datetime.combine(date.min, scheduled_time)

            appointment = Appointment(host=host, scheduled_time=scheduled_time, pickup_time=pickup_time)
            appointment.save()

            delay = pickup_date - scheduled_date

            context.update({
                'picked_up': True,
                'added_appointment': appointment,
                'delay': delay
            })

            return render(request, 'main/host_admin.html', context)

    return render(request, 'main/host_admin.html', context)


def host_login(request, host_slug):

    if request.session.get('logged_user') is not None:
        return redirect('host_admin', host_slug=host_slug)

    login_form = LoginForm()
    host = Host.objects.get(slug=host_slug)

    context = {
        'host': host,
        'login_form': login_form
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            typed_password = form.cleaned_data['password']
            stored_password = Host.objects.get(slug=host_slug).password
            if check_password(typed_password, stored_password) is True:
                request.session['logged_user'] = host_slug
                return redirect('host_admin', host_slug=host_slug)
            else:
                return render(request, 'main/host_login.html', context)    

    return render(request, 'main/host_login.html', context)


def host_front(request, host_slug):

    host = Host.objects.get(slug=host_slug)

    context = {'host': host}

    try:
        last_appointment = Appointment.objects.filter(host=host).latest(field_name='created_at')
        context.update({'updated_time': last_appointment.created_at})
    except Appointment.DoesNotExist:
        pass

    def compute_appointment_delay(Appointment):
        pickup_date = datetime.combine(date.min, Appointment.pickup_time)
        scheduled_date = datetime.combine(date.min, Appointment.scheduled_time)
        delay = pickup_date - scheduled_date
        return delay

    try:
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # Computing delay for the last appointment
        last_appointment_today = Appointment.objects.filter(host=host, created_at__gte=today).latest(field_name='pickup_time')
        delay = compute_appointment_delay(last_appointment_today)

        # Computing mean delay of the day

        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())

        all_day_appointments = Appointment.objects.filter(host=host, created_at__gte=today_start, created_at__lte=today_end).all()
        all_day_delays = list(map(compute_appointment_delay, all_day_appointments))
        mean_delay = mean(all_day_delays)
        print(mean_delay)

        context.update({
            'is_delayed': delay > timedelta(0, 10 * 60), # A delay is considered as it if it's over x minutes
            'delay_delta': delay,
            'delay_minutes': int(delay.total_seconds() / 60),
            'mean_delay_delta': mean_delay,
            'mean_delay_minutes': int(mean_delay.total_seconds() / 60),
            'last_appointment_time': last_appointment_today.scheduled_time,
            'today': today,
        })

    except Appointment.DoesNotExist:
        pass

    return render(request, 'main/host_front.html', context)