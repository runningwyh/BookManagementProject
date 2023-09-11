#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field
from fastapi import Body


class AddProject(BaseModel):
    """ 创建项目接口数据校验 """
    projectname: str
    projectcode: int
