#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from fastapi import APIRouter
from core.project.schema import AddProject
from core.project.service import AddProjectService


router = APIRouter()


@router.post(path="/project/add", summary="创建项目")
async def add_project(request_data: AddProject):
    return await AddProjectService.add_project(request_data.dict())


# @router.post(path="/project/check", summary="查询项目")
# async def check_project(request_data: CheckProject):
#     return
