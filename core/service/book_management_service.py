#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from core.model.book_management_model import Book, BookClass


class BookManagement(object):
    def __init__(self):
        pass

    async def add_book(self, body_data):
        # book_name = body_data.get("bookName")
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
        book_name and dic.update(book_name__icontains=book_name)
        author and dic.update(author__icontains=author)
        publish and dic.update(publish__icontains=publish)
        book_result = await Book.filter(**dic)
        book_result = book_result if book_result else "查询结果为空"
        book_result = book_result[(page - 1) * size:page * size]
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
        book_data = await Book.filter(id=book_id).first()
        if book_data:
            try:
                await Book.filter(id=book_id).update(**update_data)
                return "书籍修改成功！"
            except:
                return "书籍修改失败！"
        else:
            return "书籍不存在或书籍已被删除！"


class BookClassManagement(object):
    def __init__(self):
        pass

    async def book_class_manage(self, body_data):
        book_class_data = {
            "name": body_data.get("classname"),
            "description": body_data.get("description")
        }
        try:
            await BookClass.create(**book_class_data)
            return "书籍分类添加成功！"
        except Exception as e:
            return "书籍分类添加失败！"

    async def book_class_list(self, name, page, size):
        dic = {"deleted": 0}
        name and dic.update(name__icontains=name)
        class_list = await BookClass.filter(**dic)
        class_list = class_list if class_list else "查询结果为空！"
        class_list = class_list[(page - 1) * size:page * size]
        return class_list

    async def update_class(self, change_data):
        id = change_data.get("id")
        updata_data = {
            "name": change_data.get("classname"),
            "description": change_data.get("description")
        }
        book_data = await BookClass.filter(id=id).first()
        if book_data:
            try:
                await BookClass.filter(id=id).update(**updata_data)
                return "书籍分类修改成功！"
            except:
                return "书籍分类修改失败！"
        else:
            return "书籍分类不存在或书籍分类已被删除！"

    async def delete_class(self, id):
        book_class = await BookClass.filter(id=id).first()
        if book_class:
            try:
                await book_class.delete()
                return "书籍分类删除成功！"
            except Exception as e:
                return e
        else:
            return "书籍分类不存在或已被删除！"


class BookBorrowManagement(object):
    def __init__(self):
        pass

    async def borrow_book(self, id, name, name_class, return_time):
        borrow_data = {
            "id": id,
            "name": name,
            "name_class": name_class,
            "expected_back_time": return_time   # 计划还书时间
        }
        bookinfo = await Book.filter(id = id).first().values()
        if bookinfo.get("stock"):
            stock = bookinfo.get("stock") - 1
            await Book.filter(id=id).update(stock=stock)
            return "借书成功！"
        else:
            return "库存不足，请联系图书管理员！"

    async def return_book(self, id):
        pass




