#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    """ 创建用户接口数据校验 """
    userName: str
    sex: int
    age: int
    phone: str


