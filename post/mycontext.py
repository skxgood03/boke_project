from .models import *
from django.db.models import *
def GetRight(request):
    # 1.获取分类信息,c是记录数
    right_post = Post.objects.values('category__cname','category').annotate(c = Count('*')).order_by('-c')
    # 2.近期文章'
    right_recp = Post.objects.all().order_by('-category')[:3]

    #3.跟据日期获取归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("set sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';")
    cursor.execute("select created,COUNT('*') c FROM t_post GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY c desc ")
    r_file= cursor.fetchall()
    return {'r_post':right_post,'r_recp':right_recp,'r_file':r_file}