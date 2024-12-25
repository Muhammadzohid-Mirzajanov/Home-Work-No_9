from django import template
from app.models import Type  # Turlarni olish uchun modelingizni import qiling

register = template.Library()  # Teglarni ro'yxatdan o'tkazish uchun obyekt

@register.simple_tag
def get_all_types():
    return type.objects.all()
