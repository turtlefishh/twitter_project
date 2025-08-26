from django.apps import AppConfig

class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'history'

    def ready(self):
        # The IDE might flag this, but it is the correct way to handle signals.
        import history.signals  # noqa