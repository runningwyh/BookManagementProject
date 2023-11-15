#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from core.model.book_management_model import Book


class BookManagement(object):
    def __init__(self):
        pass

    async def add_book(self, body_data):
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
        try:
            await Book.create(**book_data)
            return "书籍添加成功！"
        except Exception as e:
            return e

    async def get_book_list(self, request, page, size, book_name, author, publish):
        dic = {"deleted": 0}
        book_name and dic.update(book_name=book_name)
        author and dic.update(author=author)
        publish and dic.update(publish=publish)
        book_result = await Book.filter(**dic)
        book_result = book_result if book_result else "查询结果为空"
        return book_result

    async def delete_book(self, book_id):
        book = await Book.filter(id = book_id).first()
        if book:
            await book.delete()

    async def update_book(self, book_obj):
        book_id = book_obj.get("id")
        update_data = {
            "book_name": book_obj.get("bookName"),
            "author": book_obj.get("author"),
            "publish": book_obj.get("publish"),
            "price": book_obj.get("price"),
            "stock": book_obj.get("stock"),
            "introduction": book_obj.get("introduction"),
            "publish_time": book_obj.get("publish_time")
        }
        try:
            await Book.filter(id=book_id).update(**update_data)
            return "书籍修改成功过"
        except:
            return "书籍修改失败"
