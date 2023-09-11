#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from core.user.model import User
from core.response_code import TestResponseCode

from core.te import *


class TestObject(object):

    @staticmethod
    async def regest_user(param_data):
        name = param_data.get("name")
        password = param_data.get("password")
        if len(name) < 1 or len(name) > 16:
            return "用户名长度应该是8-16位"
        db_user = await User.filter(name=name).first()
        if db_user:
            return "用户名已存在"
        try:
            hash_password = await get_password_hash(password)
        except Exception as e:
            return "密码加密失败"
        data = {
            "name": name,
            "password": hash_password,
            "email": param_data.get("email")
        }
        try:
            await User.create(**data)
            return TestResponseCode.SUCCESS
        except Exception as e:
            return "注册失败"

    @staticmethod
    async def user_login(param_data):
        name = param_data.get("name")
        password = param_data.get("password")
        db_user = await User.filter(name=name).first()
        if not db_user:
            return "用户不存在"
        if await verify_password(password, db_user.password):
            return "登录成功"
        else:
            return "密码不正确"
