from django.apps import AppConfig

class TurnosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'turnos'

    def ready(self):
        # Importar el módulo de señales para que se ejecute cuando se inicien las migraciones
        import turnos.signals