#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from pydantic import BaseModel

class BookRequest(BaseModel):
    """ 创建用户接口数据校验 """
    bookName: str
    author: str
    publish: str
    language: str
    price: float
    stock: int
    introduction: str
    publish_time: str
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


class BookClassRequest(BaseModel):
    classname: str
    description: str


class UpdataClassRequest(BookClassRequest):
    id: int


class AccountRequest(BaseModel):
    account_number: str
    name: str
    status: str
    email: str
    phone: str
    sex: int
    description: str
    last_login_time: str
    role: int
