#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fastapi import APIRouter, Request
from core.service.user_info_service import UserInfo
from core.schema.user_info_schema import UserRequest


router = APIRouter()


@router.post(path="/user/add", summary="添加用户信息")
async def regestuser(request_data: UserRequest):
    return await UserInfo().add_user(request_data.dict())


# @router.get(path="/book/list", summary="查询书籍")
# async def api_get_book_list(request: Request, page: int = 1, size: int = 10, book_name: str = None,
#                         author: str = None, publish: str = None):
#     return await BookManagement().get_book_list(request, page, size, book_name, author, publish)
#
#
# @router.delete(path="/book/delete/{book_id}", summary="删除书籍")
# async def api_delete_book(request: Request, book_id):
#     return await BookManagement().delete_book(book_id)
#
#
# @router.put(path="/book/update", summary="更新书籍")
# async def api_updata_book(request: Request, book_obj: UpdateBookRequest):
#     return await BookManagement().update_book(book_obj.dict())
