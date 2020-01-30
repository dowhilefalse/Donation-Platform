from django.shortcuts import render

# Create your views here.
from django.db.models import Q
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
    # 默认查询集
    queryset = Organization.objects.all()

    def get_queryset(self):
        '''
        修改默认查询集
        '''
        queryset = self.queryset
        # 查询范围
        # - wuhan: 武汉(武汉市)
        # - hubei: 武汉周边(湖北省中除武汉外的城市)
        # - china: 全国各地(湖北省以外的行政区划的城市)
        scope = self.request.query_params.get('scope', None) # 默认范围为全部(即, 不筛选)
        # import ipdb; ipdb.set_trace()
        if scope is not None and scope in ('wuhan', 'hubei', 'china',):
            # 注意: 以下功能要求 province 和 city 为下拉选择，而不能是人工输入
            if scope == 'wuhan':
                queryset = queryset.filter(province='湖北省', city='武汉市')
            elif scope == 'hubei':
                queryset = queryset.filter(Q(province='湖北省') & ~Q(city='武汉市'))
            else:
                queryset = queryset.filter(~Q(province='湖北省'))
        # 按时间倒序
        return queryset.order_by('-add_time')

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
