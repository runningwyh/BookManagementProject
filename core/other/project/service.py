#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from core.project.model import Projecter
from core.response_code import TestResponseCode


class AddProjectService(object):

    @staticmethod
    async def add_project(param_data):
        project_name = param_data.get("projectname")
        project_code = param_data.get("projectcode")
        db_project_name = await Projecter.filter(project_name=project_name).first()
        if db_project_name:
            return "项目已存在"
        data = {
            "project_name": project_name,
            "project_code": project_code
        }
        try:
            a = await Projecter.create(**data)
            print(a.__dict__)
            return TestResponseCode.SUCCESS
        except Exception as e:
            return "项目创建失败"
