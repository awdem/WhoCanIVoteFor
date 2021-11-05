from django.urls import path, include

from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(
    r"candidates_for_postcode",
    views.CandidatesAndElectionsForPostcodeViewSet,
    basename="candidates-for-postcode",
)
router.register(
    r"candidates_for_ballots",
    views.CandidatesAndElectionsForBallots,
    basename="candidates-for-ballots",
)


urlpatterns = [
    path(r"", include(router.urls)),
    path(
        "last-updated-timestamps/",
        views.LastUpdatedView.as_view(),
        name="last-updated-timestamps",
    ),
]
