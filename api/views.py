from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.utils.decorators import classonlymethod
from rest_framework import viewsets
from rest_framework.reverse import reverse

from registration.models import User
from .models import Organization, OrganizationContact, OrganizationDemand, Team, TeamContact
from .serializers import (
    UserSerializer,
    OrganizationContactSerializer,
    OrganizationDemandSerializer,
    OrganizationSerializer,
    TeamContactSerializer,
    TeamSerializer
)


class PatchedViewSet(viewsets.ModelViewSet):
    rewrite_app_name = None

    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        if 'app_name' in initkwargs:
            cls.rewrite_app_name = initkwargs['app_name']
            initkwargs.pop('app_name')
        return super(PatchedViewSet, cls).as_view(actions=actions, **initkwargs)

    def initialize_request(self, request, *args, **kwargs):
        if self.rewrite_app_name is not None:
            request.resolver_match.app_name = self.rewrite_app_name
            request.resolver_match.namespace = self.rewrite_app_name
        return super(PatchedViewSet, self).initialize_request(request, *args, **kwargs)

class UserViewSet(PatchedViewSet):
    """
    API endpoint that allows User to be viewed or edited.
    """
    queryset = User.objects.all().order_by('phone')
    serializer_class = UserSerializer

class OrganizationContactViewSet(PatchedViewSet):
    """
    API endpoint that allows OrganizationContact to be viewed or edited.
    """
    # queryset = OrganizationContact.objects.all()
    queryset = OrganizationContact.objects.all().order_by('-add_time')
    serializer_class = OrganizationContactSerializer

class OrganizationDemandViewSet(PatchedViewSet):
    """
    API endpoint that allows OrganizationDemand to be viewed or edited.
    """
    # queryset = OrganizationDemand.objects.all()
    queryset = OrganizationDemand.objects.all().order_by('-add_time')
    serializer_class = OrganizationDemandSerializer

class OrganizationViewSet(PatchedViewSet):
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
        # 按紧急程度正序, 时间倒序
        return queryset.order_by('emergency', '-add_time')

    serializer_class = OrganizationSerializer

# ----------------------------------------------------------------

class TeamContactViewSet(PatchedViewSet):
    """
    API endpoint that allows TeamContact to be viewed or edited.
    """
    # queryset = TeamContact.objects.all()
    queryset = TeamContact.objects.all().order_by('-add_time')
    serializer_class = TeamContactSerializer

class TeamViewSet(PatchedViewSet):
    """
    API endpoint that allows Team to be viewed or edited.
    """
    # queryset = Team.objects.all()
    queryset = Team.objects.all().order_by('-add_time')
    serializer_class = TeamSerializer
