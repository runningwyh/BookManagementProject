#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fastapi import APIRouter, Request
from core.service.book_management_service import BookManagement, BookClassManagement
from core.schema.book_management_schema import BookRequest, UpdateBookRequest, BookClassRequest, UpdataClassRequest


router = APIRouter()

# 图书管理
@router.post(path="/book/add", summary="新增图书")
async def regestuser(request_data: BookRequest):
    return await BookManagement().add_book(request_data.dict())

@router.get(path="/book/list", summary="查询书籍")
async def api_get_book_list(request: Request, page: int = 1, size: int = 10, book_name: str = None,
                        author: str = None, publish: str = None):
    return await BookManagement().get_book_list(request, page, size, book_name, author, publish)

@router.delete(path="/book/delete/{book_id}", summary="删除书籍")
async def api_delete_book(request: Request, book_id):
    return await BookManagement().delete_book(book_id)

@router.put(path="/book/update", summary="更新书籍")
async def api_updata_book(request: Request, book_obj: UpdateBookRequest):
    return await BookManagement().update_book(book_obj.dict())

# 图书分类管理
@router.post(path="/bookclass/add", summary="新增图书分类")
async def add_book_class(request_data: BookClassRequest):
    return await BookClassManagement().book_class_manage(request_data.dict())

@router.get(path="/bookclass/list", summary="查询书籍分类")
async def get_book_class(request: Request, name: str = None, page: int = 1, size: int = 10):
    return await BookClassManagement().book_class_list(name, page, size)

@router.put(path="/bookclass/update", summary="修改书籍分类")
async def update_class_name(request: Request, change_info: UpdataClassRequest):
    return await BookClassManagement().update_class(change_info.dict())

@router.delete(path="/bookclass/delete/{id}", summary="删除分类")
async def delete_book_class(request: Request, id):
    return await BookClassManagement().delete_class(id)


# 借阅管理
