#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fastapi import APIRouter, Body

from core.service.book_management_service import BookManagement
from core.schema.book_management_schema import BookRequest
from settings import logs

router = APIRouter()


@router.post(path="/book/add", summary="新增图书")
async def regestuser(request_data: BookRequest):
    return await BookManagement.add_book(request_data.dict())


