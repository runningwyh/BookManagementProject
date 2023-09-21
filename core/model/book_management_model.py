#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tortoise import Model, fields
from tortoise.fields.relational import ForeignKeyField


class Book(Model):
    """ 创建user表 """
    # pk=True, 设置为主键
    id = fields.IntField(pk=True, unique=True, description="主键")
    book_name = fields.CharField(max_length=64, null=False, unique=True, description="书名")
    author = fields.CharField(max_length=32, description="作者")
    publish = fields.CharField(max_length=32, description="出版社")
    publish_time = fields.CharField(max_length=32, description="出版时间")
    language = fields.CharField(max_length=16, description="语言")
    price = fields.FloatField(description="价格")
    book_class_id = fields.IntField(description="图书分类")
    stock = fields.IntField(description="库存")
    introduction = fields.TextField(description="简介")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
    deleted = fields.IntField(default= 0, null=False, description="0：未删除，1：删除")

    class Meta:
        table = "book"
        table_description = "图书表"
        unique_together = []
        ordering = []
