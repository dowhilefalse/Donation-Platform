from rest_framework import serializers

from .models import Organization, OrganizationContact, OrganizationDemand, Team, TeamContact
from registration.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'phone', 'id']

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
        fields = ['url', 'id', 'contacts', 'demands', 'province', 'city', 'name', 'address', 'source', 'verified', 'add_time', 'is_manual', 'inspector', 'emergency']

    def create(self, validated_data):
        contacts_data = validated_data.pop('organizationcontact_set', [])
        demands_data = validated_data.pop('organizationdemand_set', [])
        # import ipdb; ipdb.set_trace()
        instance = Organization.objects.create(**validated_data)
        
        for contact_data in contacts_data:
            contact_data.pop('organization', None)
            contact, contact_created = OrganizationContact.objects.update_or_create(organization=instance, **contact_data)
        
        for demand_data in demands_data:
            demand_data.pop('organization', None)
            demand, demand_created = OrganizationDemand.objects.update_or_create(organization=instance, **demand_data)
        
        return instance

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('organizationcontact_set', [])
        demands_data = validated_data.pop('organizationdemand_set', [])
        instance = super(OrganizationSerializer, self).update(instance, validated_data)
        
        for contact_data in contacts_data:
            # import ipdb; ipdb.set_trace()
            contact_data.pop('organization', None)
            contact, contact_created = OrganizationContact.objects.update_or_create(organization=instance, **contact_data)
        
        for demand_data in demands_data:
            demand_data.pop('organization', None)
            demand, demand_created = OrganizationDemand.objects.update_or_create(organization=instance, **demand_data)

        return instance 

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
