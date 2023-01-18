import uuid
from django.db import models
from django.utils import timezone

# テーブルの作成
# Meassgeのテーブルを作成
class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

# stressのテーブルを作成
class Stress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #stress = models.TextField()    # 文字列の場合
    stress = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)