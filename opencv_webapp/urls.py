from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #어떤 글자든지 (^$) view파일의 first_view로 가라
    url(r'^$',views.first_view, name='first_view'),

    #uimage라는 주소를 넣으면 uimage 함수로 name을 uimage로 전달
    url(r'^uimage/$',views.uimage, name = 'uimage'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)