#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True, unique=True, description='主键')
    user_name = fields.CharField(max_length=32, description='姓名')
    sex = fields.IntField(default=0, description="性别(0：男，1：女")
    age = fields.IntField(description='年龄')
    phone= fields.CharField(max_length=32, description='电话')

    class Meta:
        table = "userinfo"
        table_description = "用户表"
        unique_together = []
        ordering = []