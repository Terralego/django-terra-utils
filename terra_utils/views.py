from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from terra_utils.settings import STATES, TERRA_APPLIANCE_SETTINGS


class SettingsView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        terra_settings = {
            'states': {
                y: x
                for x, y in STATES.VALUE_TO_CONST.items()
            },
            'jwt_delta': settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
        }

        terra_settings.update(TERRA_APPLIANCE_SETTINGS)

        return Response(terra_settings)
