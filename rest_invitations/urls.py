from django.urls import include, re_path
from rest_framework import routers

from .app_settings import ACCEPT_INVITE_URL, API_BASE_URL
from .views import InvitationViewSet, accept_invitation

router = routers.SimpleRouter()
router.register(r'{0}'.format(API_BASE_URL), InvitationViewSet)

invitations_patterns = (
    [
        re_path(
            r'^{0}/{1}/(?P<key>\w+)/?$'.format(
                API_BASE_URL, ACCEPT_INVITE_URL
            ),
            accept_invitation,
            name='accept-invite'
        ),
    ],
    'invitations'
)

urlpatterns = router.urls + [
    re_path(r'^', include(invitations_patterns)),
]
