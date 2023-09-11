#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fastapi import APIRouter

from core.user.schema import UserRequest, UserLogin
from core.user.service import TestObject
router = APIRouter()


@router.post(path="/regester", summary="用户注册")
async def regestuser(request_data: UserRequest):
    return await TestObject.regest_user(request_data.dict())


@router.post(path="/login", summary="用户登录")
async def login(request_data: UserLogin):
    return await TestObject.user_login(request_data.dict())

