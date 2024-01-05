from django.urls import path
from . import views

app_name='baseapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('baseapp/about/',views.about, name='about'),
    path('baseapp/portfolio_1/',views.portfolio_1, name='portfolio_1'),
    path('baseapp/portfolio_2/',views.portfolio_2, name='portfolio_2'),
    path('baseapp/portfolio_3/',views.portfolio_3, name='portfolio_3'),
    path('baseapp/portfolio_4/',views.portfolio_4, name='portfolio_4'),
    path('baseapp/portfolio_0/',views.portfolio_0, name='portfolio_0'),
    path('baseapp/faq/',views.faq, name='faq'),

]


