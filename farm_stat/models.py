from django.db import models


class Testimony(models.Model):

    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='images/testimonies')
    commet = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "testimony"
        verbose_name_plural = "testimonies"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("testimony_detail", kwargs={"pk": self.pk})


class Achievement(models.Model):

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "achievement"
        verbose_name_plural = "achievements"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("achievement_detail", kwargs={"pk": self.pk})


class Partner(models.Model):

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/partner')
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("partner_detail", kwargs={"pk": self.pk})
