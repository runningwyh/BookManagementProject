#!/usr/bin/python3
# -*- coding: UTF-8 -*-


class TestResponseCode(object):
    SUCCESS = {"message": "成功", "code": 200000, "data": ""}
    Test1CreateError = {"message": "test1数据已存在", "code": 100001, "data": ""}
    Test2CreateError = {"message": "test2和test3数据已存在", "code": 100002, "data": ""}
    Test1UpdateError = {"message": "test1数据不存在", "code": 100003, "data": ""}
