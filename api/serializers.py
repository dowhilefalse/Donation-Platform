from rest_framework import serializers

from .models import Organization, OrganizationContact, OrganizationDemand, Team, TeamContact


class OrganizationContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationContact
        fields = ['url', 'id', 'organization', 'name', 'phone', 'add_time',]

class OrganizationDemandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationDemand
        fields = ['url', 'id', 'organization', 'name', 'remark', 'amount', 'receive_amount', 'add_time',]

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    contacts = OrganizationContactSerializer(source='organizationcontact_set', many=True)
    demands = OrganizationDemandSerializer(source='organizationdemand_set', many=True)

    class Meta:
        model = Organization
        fields = ['url', 'id', 'contacts', 'demands', 'province', 'city', 'name', 'address', 'source', 'verified', 'add_time',]

# -----------------------------------------------------------------------------------------------------

class TeamContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamContact
        fields = ['url', 'id', 'team', 'name', 'phone', 'add_time',]

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    contacts = TeamContactSerializer(source='teamcontact_set', many=True)

    class Meta:
        model = Team
        fields = ['url', 'id', 'contacts', 'name', 'address', 'verified', 'add_time',]
