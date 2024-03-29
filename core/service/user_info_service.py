#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
from core.model.user_info_model import User
from starlette.responses import FileResponse

from utils.handle_yaml import Handleyaml


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
    async def get_user_list(self, request, page, size, user_name, phone):
        dic = {}
        user_name and dic.update(user_name__icontains=user_name)
        phone and dic.update(phone__icontains=phone)
        user_result = await User.filter(**dic)
        user_result = user_result if user_result else "查询结果为空"
        user_result = user_result[(page - 1) * size:page * size]
        return user_result
    #
    async def delete_user(self, user_id):
        user = await User.filter(id = user_id).first()
        if user:
            await user.delete()
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


class Other(object):
    def __init__(self):
        self.do_yaml = Handleyaml('config.yaml')

    async def upload_image(self, image):
        if not image.content_type.startswith("image/"):
            return {"message": "只能上传图片文件"}
        # 保存文件到指定路径
        save_path = "/data/images"
        file_path = os.path.join(save_path, image.filename)
        with open(file_path, "wb") as f:
            try:
                f.write(await image.read())
                return "保存成功"
            except Exception as e:
                return e

    async def get_image(self, filename):
        file_path =self.do_yaml.read_yaml('path', 'images_file')
        file_path = f"{file_path}/{filename}"
        try:
            return FileResponse(file_path, media_type="image/png")
        except Exception as e:
            return e
