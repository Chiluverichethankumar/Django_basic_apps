from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Myapp'

    def ready(self):
        import Myapp.signals  # Make sure to import signals here
