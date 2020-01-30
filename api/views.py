from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Organization, OrganizationContact, OrganizationDemand, Team, TeamContact
from .serializers import (
    OrganizationContactSerializer,
    OrganizationDemandSerializer,
    OrganizationSerializer,
    TeamContactSerializer,
    TeamSerializer
)

class OrganizationContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrganizationContact to be viewed or edited.
    """
    # queryset = OrganizationContact.objects.all()
    queryset = OrganizationContact.objects.all().order_by('-add_time')
    serializer_class = OrganizationContactSerializer

class OrganizationDemandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrganizationDemand to be viewed or edited.
    """
    # queryset = OrganizationDemand.objects.all()
    queryset = OrganizationDemand.objects.all().order_by('-add_time')
    serializer_class = OrganizationDemandSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Organization to be viewed or edited.
    """
    # queryset = Organization.objects.all()
    queryset = Organization.objects.all().order_by('-add_time')
    serializer_class = OrganizationSerializer

# ----------------------------------------------------------------

class TeamContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TeamContact to be viewed or edited.
    """
    # queryset = TeamContact.objects.all()
    queryset = TeamContact.objects.all().order_by('-add_time')
    serializer_class = TeamContactSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    # queryset = Team.objects.all()
    queryset = Team.objects.all().order_by('-add_time')
    serializer_class = TeamSerializer
