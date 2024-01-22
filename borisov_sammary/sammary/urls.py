from django.urls import path

from sammary.views import *

urlpatterns = [
    path('', base, name='home'),
    # path('portfolio/', portfolio, name='portfolio'),
    # path('portfolio_details/', portfolio_details, name='portfolio_details'),
]