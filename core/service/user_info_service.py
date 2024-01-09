#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from core.model.user_info_model import User


class UserInfo(object):
    def __init__(self):
        pass

    async def add_user(self, body_data):
        user_name = body_data.get("userName")
        user_date = {
            "user_name": body_data.get("userName"),
            "sex": body_data.get("sex"),
            "age": body_data.get("age"),
            "phone": body_data.get("phone")
        }
        try:
            await User.create(**user_date)
            return "新增客户信息成功！"
        except Exception as e:
            return e
    #
    # async def get_book_list(self, request, page, size, book_name, author, publish):
    #     dic = {"deleted": 0}
    #     book_name and dic.update(book_name__icontains=book_name)
    #     author and dic.update(author__icontains=author)
    #     publish and dic.update(publish__icontains=publish)
    #     book_result = await Book.filter(**dic)
    #     book_result = book_result if book_result else "查询结果为空"
    #     book_result = book_result[(page - 1) * size:page * size]
    #     return book_result
    #
    # async def delete_book(self, book_id):
    #     book = await Book.filter(id = book_id).first()
    #     if book:
    #         await book.delete()
    #
    # async def update_book(self, book_obj):
    #     book_id = book_obj.get("id")
    #     update_data = {
    #         "book_name": book_obj.get("bookName"),
    #         "author": book_obj.get("author"),
    #         "publish": book_obj.get("publish"),
    #         "price": book_obj.get("price"),
    #         "stock": book_obj.get("stock"),
    #         "introduction": book_obj.get("introduction"),
    #         "publish_time": book_obj.get("publish_time")
    #     }
    #     book_data = await Book.filter(id=book_id).first()
    #     if book_data:
    #         try:
    #             await Book.filter(id=book_id).update(**update_data)
    #             return "书籍修改成功！"
    #         except:
    #             return "书籍修改失败！"
    #     else:
    #         return "书籍不存在或书籍已被删除！"
