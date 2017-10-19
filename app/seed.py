from main.models import *
from django.template.defaultfilters import slugify

# Organizations

org1 = {
    'name': "Institut Hospitalier Franco-Britannique"
}

org1_m = Organization(name=org1['name'], slug=slugify(org1['name']))
org1_m.save()

#--

org2 = {
    'name': "Service de Radiologie"
}

org2_m = Organization(name=org2['name'], slug=slugify(org2['name']), parent_organization=org1_m)
org2_m.save()

#--

org3 = {
    'name': "Service de Chirurgie"
}

org3_m = Organization(name=org3['name'], slug=slugify(org3['name']), parent_organization=org1_m)
org3_m.save()

#--

org4 = {
    'name': "Sous-service de Radiologie"
}

org4_m = Organization(name=org4['name'], slug=slugify(org4['name']), parent_organization=org2_m)
org4_m.save()

#--

org5 = {
    'name': "Cabinet du Dr. Mormon"
}

org5_m = Organization(name=org5['name'], slug=slugify(org5['name']))
org5_m.save()

# Hosts

host1 = {
    'title': 'Dr',
    'first_name': 'Jean',
    'last_name': 'Perrerin'
}

host1_m = Host(
    title=host1['title'],
    first_name=host1['first_name'],
    last_name=host1['last_name'],
    slug=slugify(host1['last_name']),
    organization=org2_m
)

host1_m.save()

#--

host2 = {
    'title': 'Dr',
    'first_name': 'Martine',
    'last_name': 'Lavoisier'
}

host2_m = Host(
    title=host2['title'],
    first_name=host2['first_name'],
    last_name=host2['last_name'],
    slug=slugify(host2['last_name']),
    organization=org2_m
)

host2_m.save()