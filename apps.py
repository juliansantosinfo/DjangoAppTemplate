from django.apps import AppConfig
from django.utils.translation import gettext, gettext_lazy as _


class {{ camel_case_app_name }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ app_name }}'
