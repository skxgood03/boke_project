import math

from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator  #分页
# Create your views here.
from django.db import connection
import datetime
from django.utils.timezone import utc
utcnow = datetime.datetime.utcnow().replace(tzinfo=utc)
#渲染主页面
def all(request,num=1):

    # num = int(num)
    #获取所有帖子信息
    postlist = Post.objects.all().order_by('-created')
    # postlists = Post.objects.values('created')
    # print(postlists)
    #创建分页器对象
    pageObj = Paginator(postlist,2)
    #获取当前页数据
    perPagelist = pageObj.page(num)

    #生成页码数列表
    #每页开始页码
    begin = (num - int(math.ceil(10.0/2)))
    if begin < 1:
        begin = 1

    #每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <=10:
        begin = 1
    else:
        begin = end - 9

    PageList = range(begin, end+1)


    return render(request,'index.html',{'postlist':perPagelist,'pagelist':PageList,'currentnum':num})

#查看全部
def allpost(request,num):
    #根据num查询贴子的详情
    post = Post.objects.filter(id=num)
    return render(request,'details.html',{'posts':post})

#根据id查询所有贴子
def postid(request,cid):
    # postList = Post.objects.filter(category_id=cid)
    # print(postList)
    cursor = connection.cursor()

    sql = "select id,title,created FROM t_post WHERE category_id={} ".format(cid)
    cursor.execute(sql)
    postList= cursor.fetchall()
    return render(request,'article.html',{'postList':postList})


def PostCreated(request,year,month):
    print(year,month)

    cursor = connection.cursor()

    sql = "select id,title,created FROM t_post WHERE DATE_FORMAT(created,'%Y') ={} AND DATE_FORMAT(created,'%m')={}".format(month,year)
    cursor.execute(sql)
    postList= cursor.fetchall()
    print(postList)
    return render(request,'article.html',{'postList':postList})

