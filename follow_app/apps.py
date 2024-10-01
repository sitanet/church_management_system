from django.apps import AppConfig

class FollowAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'follow_app'


    # def ready(self):
    #     import follow_app.signals

