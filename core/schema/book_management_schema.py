#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    """ 创建用户接口数据校验 """
    # default=..., 是指name字段为必填项, 不写default参数也是默认为必填, 这里加上只是为了更清晰
    bookName: str = Field(default=..., description="书籍名称")
    author: str = Field(..., description="作者")
    publish: str = Field(..., description="出版社")
    # Optional[str]可选项, default=None可以不填或者是填写None
    language: str
    price: float
    stock: int
    introduction: str
    className: str



class UserLogin(BaseModel):
    """ 用户登录数据格式化 """
    name: str
    password: str

