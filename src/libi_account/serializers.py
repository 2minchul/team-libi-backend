from rest_framework import serializers

from libi_account.models import Account
from libi_common.serializers import StatelessSerializer


class AccountCreateRequestSerializer(StatelessSerializer):
    phone = serializers.CharField(required=True, max_length=16, help_text='휴대전화번호')
    password = serializers.CharField(required=True, trim_whitespace=False, help_text='비밀번호')
    name = serializers.CharField(required=True, max_length=64, help_text='이름')

    def validate_phone(self, value: str):
        value = value.strip().replace('-', '')
        if not value.isdigit():
            raise serializers.ValidationError("올바르지 않은 휴대전화번호입니다")
        return value


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'phone', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'phone', 'created_at', 'updated_at',)


class TokenCreateRequestSerializer(StatelessSerializer):
    phone = serializers.CharField(required=True, max_length=16, help_text='휴대전화번호')
    password = serializers.CharField(required=True, trim_whitespace=False, help_text='비밀번호')

    def validate_phone(self, value: str):
        value = value.strip().replace('-', '')
        if not value.isdigit():
            raise serializers.ValidationError("올바르지 않은 휴대전화번호입니다")
        return value


class TokenResponseSerializer(StatelessSerializer):
    access_token = serializers.CharField(required=True, help_text='AccessToken')
