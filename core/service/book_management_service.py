#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from core.model.book_management_model import Book
from core.response_code import TestResponseCode

from core.te import *
from settings import logs


class BookManagement(object):
    @staticmethod
    async def add_book(body_data):
        book_name = body_data.get("bookName")
        book_data = {
            "book_name": body_data.get("bookName"),
            "author": body_data.get("author"),
            "publish": body_data.get("publish"),
            "language": body_data.get("language"),
            "price": body_data.get("price"),
            "stock": body_data.get("stock"),
            "introduction": body_data.get("introduction"),
            "publish_time": body_data.get("publish_time"),
            "book_class_id": body_data.get("book_class_id")
        }
        await Book.create(**book_data)
        return book_data
