from rest_framework import serializers

from .models import Organization, OrganizationContact, OrganizationDemand, Team, TeamContact
from registration.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'phone', 'id']
        extra_kwargs = {
            'id': {'required': False},
            'url': {'required': False, 'read_only': True},
        }

class OrganizationContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationContact
        fields = ['url', 'id', 'organization', 'name', 'phone', 'add_time',]
        extra_kwargs = {
            'id': {'required': False},
            'url': {'required': False, 'read_only': True},
            'add_time': {'required': False, 'read_only': True},
            'organization': {'required': False},
        }

class OrganizationDemandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationDemand
        fields = ['url', 'id', 'organization', 'name', 'remark', 'amount', 'receive_amount', 'add_time',]
        extra_kwargs = {
            'id': {'required': False},
            'url': {'required': False, 'read_only': True},
            'add_time': {'required': False, 'read_only': True},
            'organization': {'required': False},
            'remark': {'required': False},
            'amount': {'required': False},
            'receive_amount': {'required': False},
        }

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    contacts = OrganizationContactSerializer(source='organizationcontact_set', many=True)
    demands = OrganizationDemandSerializer(source='organizationdemand_set', many=True)

    class Meta:
        model = Organization
        fields = ['url', 'id', 'contacts', 'demands', 'province', 'city', 'name', 'address', 'source', 'verified', 'add_time', 'is_manual', 'inspector', 'emergency']
        extra_kwargs = {
            'id': {'required': False},
            'url': {'required': False, 'read_only': True},
            'add_time': {'required': False, 'read_only': True},
            'inspector': {'required': False},
            'emergency': {'required': False},
            'address': {'required': False},
            'source': {'required': False},
            'verified': {'required': False, 'default': False},
            'is_manual': {'required': False, 'default': True},
        }

    def create(self, validated_data):
        contacts_data = validated_data.pop('organizationcontact_set', [])
        demands_data = validated_data.pop('organizationdemand_set', [])
        user = validated_data.pop('inspector', None)
        try:
            user = self.context['request'].user
        except Exception as e:
            pass

        instance = Organization.objects.create(inspector=user, **validated_data)
        
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
        validated_data.pop('inspector', None)

        instance = super(OrganizationSerializer, self).update(instance, validated_data)
        
        for contact_data in contacts_data:

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
        extra_kwargs = {
            'id': {'required': False},
            'url': {'required': False, 'read_only': True},
            'add_time': {'required': False, 'read_only': True},
            'team': {'required': False},
        }

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    contacts = TeamContactSerializer(source='teamcontact_set', many=True)

    class Meta:
        model = Team
        fields = ['url', 'id', 'contacts', 'name', 'address', 'verified', 'add_time',]
        extra_kwargs = {
            'id': {'required': False},
            'url': {'required': False, 'read_only': True},
            'add_time': {'required': False, 'read_only': True},
            'inspector': {'required': False},
        }

    def create(self, validated_data):
        contacts_data = validated_data.pop('teamcontact_set', [])
        user = validated_data.pop('inspector', None)
        try:
            user = self.context['request'].user
        except Exception as e:
            pass

        instance = Team.objects.create(inspector=user, **validated_data)
        
        for contact_data in contacts_data:
            contact_data.pop('team', None)
            contact, contact_created = TeamContact.objects.update_or_create(team=instance, **contact_data)

        return instance

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop('teamcontact_set', [])
        validated_data.pop('inspector', None)

        instance = super(TeamSerializer, self).update(instance, validated_data)
        
        for contact_data in contacts_data:
            contact_data.pop('team', None)
            contact, contact_created = TeamContact.objects.update_or_create(team=instance, **contact_data)

        return instance 
