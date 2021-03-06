from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from degvabank.apps.card.serializers import UserDebitCardSerializer
from degvabank.apps.petitions.models import Petition

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class UserAccountSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    cards = UserDebitCardSerializer(
        source="get_active_cards", many=True, read_only=True
    )

    def get_id(self, obj):
        return obj.pretty_account_number

    def validate(self, attrs):
        if Petition.objects.filter(
            user=attrs["user"],
            reason=Petition.ReasonType.OPEN_ACCOUNT,
            status=Petition.PetitionStatus.PENDING,
        ).exists():
            raise ValidationError(
                _("you cannot have 2 pending accounts"),
                code="petition already exist",
            )
        return attrs

    def create(self, validated_data):
        return self.Meta.model.objects.request_account(**validated_data)

    class Meta:
        model = Account
        fields = [
            "id",
            "type",
            "balance",
            "date_created",
            "cards",
            "user",
        ]
