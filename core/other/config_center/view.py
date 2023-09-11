#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from fastapi import APIRouter, Request
from starlette import status

from core.config_center.schema import AddCaseConfig
from core.config_center.service import CaseConfigService

router = APIRouter()


@router.post("/case/config", status_code=status.HTTP_200_OK, summary="新增用例配置")
# @try_except
async def post_case_config(request: Request, request_data: AddCaseConfig):
    """创建用例配置项"""
    return await CaseConfigService.create_case_config(request_data.dict())
