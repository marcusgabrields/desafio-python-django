from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("first name"), max_length=255)


class Phone(TimeStampedModel):
    profile = models.ForeignKey(
        "profiles.Profile",
        on_delete=models.CASCADE,
        verbose_name=_("profile"),
        related_name="phones",
        related_query_name="phone",
    )
    number = models.PositiveIntegerField(_("number"))
    area_code = models.PositiveSmallIntegerField(_("area code"))
    country_code = models.CharField(_("country code"), max_length=7)
