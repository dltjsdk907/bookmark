# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 아래 행 한 줄은 수정된 행
    path('', include('bookmark.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]