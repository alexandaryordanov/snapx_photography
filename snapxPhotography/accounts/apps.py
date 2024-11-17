from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'snapxPhotography.accounts'

    def ready(self):
        import snapxPhotography.accounts.signals

