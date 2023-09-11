#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tortoise import Model, fields
from tortoise.fields.relational import ForeignKeyField


class CaseConfig(Model):  # 用例配置
    id = fields.IntField(pk=True)
    config_code = fields.CharField(35, null=False, description="项目Code:唯一标签", unique=True)
    config_name = fields.CharField(100, null=False, description="配置名称")
    project_code = fields.CharField(35, null=True, description="项目Code:唯一标签")
    setup_data = fields.JSONField(null=True, description="前置配置数据")
    teardown_data = fields.JSONField(null=True, description="后置配置数据")
    tag = fields.CharField(50, null=True, description="标签")
    remark = fields.CharField(80, null=True, description="备注")
    created_time = fields.DatetimeField(null=True, auto_now_add=True, description="创建时间")
    modified_time = fields.DatetimeField(null=True, auto_now=True, description="修改时间")
    status = fields.CharField(3, null=False, default="1", description="状态(0：禁用，1：启用)")
    deleted = fields.IntField(null=False, default="0", description="是否删除(0：未删除，1：已删除")

    class Meta:  # 添加索引和表注释
        app = "zt_auto_test"
        table = "case_config"
        table_description = "用例配置表"
        ordering = ["-modified_time"]

    class PydanticMeta:
        exclude = ["created_time", "modified_time", "id"]
