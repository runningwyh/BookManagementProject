#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tortoise import Model, fields
from tortoise.fields.relational import ForeignKeyField


class Projecter(Model):
    """ 创建项目表 """
    # pk=True, 设置为主键
    id = fields.IntField(pk=True)
    project_name = fields.CharField(max_length=64, description="项目名")
    project_code = fields.IntField(max_length=64, description="项目code")
    create_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    modify_at = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = "project_table"
        table_description = "项目表"
        unique_together = []
        ordering = []
