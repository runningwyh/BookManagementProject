# -*- coding: utf-8 -*-
from core.view.book_management_view import router as book
from core.view.user_info_view import router as user

"""
接口路由view层注册
"""


RESPONSES = {404: {"description": "Not found"}}
include = [
    {"router": book, "prefix": f"", "tags": ['图书接口'], "responses": RESPONSES},
    {"router": user, "prefix": f"/userinfo", "tags": ['用户管理'], "responses": RESPONSES}
]
