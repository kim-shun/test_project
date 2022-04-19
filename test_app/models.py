from django.db import models


class Test(models.Model):
    """テストモデル"""
    name = models.CharField(verbose_name='名前', max_length=40)
    age = models.PositiveIntegerField(verbose_name='年齢')
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Test'

    def __str__(self):
        return self.title
