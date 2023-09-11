# -*- coding: utf-8 -*-
from core.view.book_management_view import router as book

"""
接口路由view层注册
"""


RESPONSES = {404: {"description": "Not found"}}
include = [
    {"router": book, "prefix": f"/book", "tags": ['user_center'], "responses": RESPONSES},
    # {"router": project, "prefix": f"/project", "tags": ['interface_center'], "responses": RESPONSES}
]
