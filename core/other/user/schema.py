#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field
from fastapi import Body


class UserRequest(BaseModel):
    """ 创建用户接口数据校验 """
    # default=..., 是指name字段为必填项, 不写default参数也是默认为必填, 这里加上只是为了更清晰
    name: str = Body(default=..., description="用户名")
    password: str = Body(..., description="登录密码")
    # Optional[str]可选项, default=None可以不填或者是填写None
    email: Optional[str] = Body(default=None, description="邮箱")


class UserLogin(BaseModel):
    """ 用户登录数据格式化 """
    name: str
    password: str

