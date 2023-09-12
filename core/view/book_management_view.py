#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fastapi import APIRouter, Request

from core.service.book_management_service import BookManagement
from core.schema.book_management_schema import BookRequest


router = APIRouter()


@router.post(path="/book/add", summary="新增图书")
async def regestuser(request_data: BookRequest):
    return await BookManagement().add_book(request_data.dict())


@router.get(path="/book/list", summary="查询书籍")
async def get_book_list(request: Request):
    return await BookManagement().select_book(request)