#使っていません。
from django.core.exceptions import ValidationError


def validate_admin(value):
    if 'admin' in value:
        raise ValidationError('空白文字のみは使用できません。')