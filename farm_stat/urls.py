from django.urls import path
from farm_stat.views import TestimonyList, AchievementList, PartnerList
urlpatterns = [
    path('testimonials', TestimonyList.as_view(), name='testimonials_list'),
    path('partners', PartnerList.as_view(), name='partner_list'),
    path('achievements', AchievementList.as_view(), name='achievement_list'),
]
