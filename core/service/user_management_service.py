#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from core.model.user_management_model import Book
from core.response_code import TestResponseCode

from core.te import *


class BookManagement(object):

    @staticmethod
    async def add_book(body_data):
        book_name = body_data.get("book_name")

        return body_data


