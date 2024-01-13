#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tortoise import Model, fields


class Book(Model):
    id = fields.IntField(pk=True, unique=True, description="主键")
    book_name = fields.CharField(max_length=64, null=False, unique=True, description="书名")
    author = fields.CharField(max_length=32, description="作者")
    publish = fields.CharField(max_length=32, description="出版社")
    publish_time = fields.CharField(max_length=32, description="出版时间")
    language = fields.CharField(max_length=16, description="语言")
    price = fields.DecimalField(max_digits=8, decimal_places=2, description="价格")
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


class BookClass(Model):
    id = fields.IntField(pk=True, unique=True, description="主键")
    name = fields.CharField(max_length=32, null=False, description="分类名称")
    description = fields.CharField(max_length=256, default=None, description="备注")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
    deleted = fields.IntField(default=0, null=False, description="0：未删除，1：删除")

    class Meta:
        table = "book_class"
        table_description = "图书分类表"
        unique_together = []
        ordering = []


class BorrowRecord(Model):
    id = fields.IntField(pk=True, unique=False, description="主键")
    book_id = fields.IntField(null=False, description="图书id")
    passport = fields.CharField(max_length=32, null=False, description="账号")
    borrow_time = fields.DatetimeField(auto_now_add=True, description="借书时间")
    expected_back_time = fields.CharField(max_length=20, null=False,default=None, description="计划还书时间")
    back_time = fields.CharField(max_length=20, default=None, description="还书时间")

    class Meta:
        table = "borroe_info"
        table_description = "借阅信息表"
        unique_together = []
        ordering = []


class Account(Model):
    """账号表"""
    id = fields.IntField(pk=True, unique=True, description="主键")
    passport = fields.CharField(max_length=16, null=False, description="账号", )
    name = fields.CharField(max_length=6, null=False, description="名称")
    password = fields.CharField(max_length=64, null=False, description="密码")
    status = fields.CharField(max_length=64, null=False, description="用户状态")
    role_id = fields.IntField(null=False, description="角色")
    email = fields.CharField(max_length=16, null=False, description="邮箱")
    phone = fields.CharField(max_length=16, null=False, description="手机号")
    address = fields.CharField(max_length=64, default=None, description="地址")
    sex = fields.IntField(default=0, description="性别 0：女；1：男")
    description = fields.CharField(max_length=128, default=None, description="备注")
    last_login_time = fields.CharField(max_length=32, default=0, description="最近登录时间")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now_add=True, description="更新时间")

    class Meta:
        table = "account"
        table_description = "账号表"
        unique_together = []
        ordering = []

# """
# CREATE TABLE `account` (
#
#   UNIQUE KEY `passport_UNIQUE` (`passport`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='账号表'
# """
#
#
class Role(Model):
    id = fields.IntField(pk=True, unique=False, description="主键")
    name = fields.CharField(max_length=32, null=False, description="角色名称")
    description = fields.CharField(max_length=128, default=None, description="角色名称")
    authorities = fields.CharField(max_length=1024, null=False, description="权限列表")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now_add=True, description="更新时间")

    class Meta:
        table = "role"
        table_description = "角色表"
        unique_together = []
        ordering = []