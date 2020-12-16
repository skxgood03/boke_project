#全文搜索
from haystack import indexes
from post.models import *

#格式（模型名+Index）
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)  #固定字段

    #给title，content设置索引
    title = indexes.NgramField(model_attr='title')  #必须和model的字段对应（用于搜索的字段）
    content = indexes.NgramField(model_attr='content')  #必须和model的字段对应（用于搜索的字段）

    def get_model(self):  #重写父类方法
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')