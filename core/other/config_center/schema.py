#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from enum import Enum
from typing import Any, Optional, List
from pydantic import BaseModel, Field
from fastapi import Body


class AddCaseConfig(BaseModel):
    config_name: str
    project_code: str = None
    setup_data: List[dict] = list()
    teardown_data: List[dict] = list()
    remark: str = None
