from django.db import models

# Create your models here.
PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))
# models.Modelは定型
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices= PRIORITY
    )
    duedate = models.DateField()
    # オブジェクトを文字列として表示するときにどう見せるかを決めるメソッド
    def __str__(self):
        return self.title