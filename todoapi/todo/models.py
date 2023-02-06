from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    # 디버깅을 위해서 사용 - print로 인스턴스를 출력하면 호출되는 메서드
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)