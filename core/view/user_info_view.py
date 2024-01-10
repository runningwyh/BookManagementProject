#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fastapi import APIRouter, Request
from core.service.user_info_service import UserInfo
from core.schema.user_info_schema import UserRequest


router = APIRouter()


@router.post(path="/user/add", summary="添加用户信息")
async def regestuser(request_data: UserRequest):
    return await UserInfo().add_user(request_data.dict())


@router.get(path="/user/list", summary="查询用户")
async def api_get_user_list(request: Request, user_name: str = None,
                        phone: str = None, page: int = 1, size: int = 10):
    return await UserInfo().get_user_list(request, page, size, user_name, phone)
#
#
@router.delete(path="/user/delete/{user_id}", summary="删除用户")
async def api_delete_user(request: Request, user_id):
    return await UserInfo().delete_user(user_id)

#
# @router.put(path="/book/update", summary="更新书籍")
# async def api_updata_book(request: Request, book_obj: UpdateBookRequest):
#     return await BookManagement().update_book(book_obj.dict())
