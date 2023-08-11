from django.apps import AppConfig


class RestobotApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restobot_api'

    # Bot autorun:
    # def ready(self):
    #     from django.core.management import call_command
    #     call_command('bot')
