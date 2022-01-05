from django.contrib import admin
from .models import Location, Post 

admin.site.register(Location)  #註冊至Administration(管理員後台)
admin.site.register(Post)  #註冊至Administration(管理員後台)

#引用應用程式(APP) models.py中的Location及Posts資料模型
# Register your models here.如果想要把Django專案中的應用程式(APP)資料模型(Model)，加入到Django Administration(管理員後台)，就可以透過應用程式(APP)底下的admin.py檔案來達成
