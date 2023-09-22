#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    """ 创建用户接口数据校验 """
    bookName: str
    author: str
    publish: str
    language: str
    price: float
    stock: int
    introduction: str
    publish_time:str
    book_class_id: str


class UpdateBookRequest(BaseModel):
    id: int
    bookName: str
    author: str
    publish: str
    price: float
    stock: int
    introduction: str
    publish_time: str

