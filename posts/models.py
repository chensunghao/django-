from django.db import models
from django.utils import timezone

# 景點位置
class Location(models.Model):
    name = models.CharField(max_length=255)  #位置名稱

#景點貼文，於要建立「景點位置」及「景點貼文」一對多的關係，所以透過ForeignKey類別來進行設定，而on_delete=models.CASCADE的意思是，當「景點位置」資料表中的資料被刪除時，相對應的「景點貼文」資料也跟著刪除。
class Post(models.Model):
    subject = models.CharField(max_length=255)  #標題
    content = models.CharField(max_length=255)  #內容
    author = models.CharField(max_length=20)  #貼文者
    create_date = models.DateField(default=timezone.now)  #貼文時間
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #景點位置



