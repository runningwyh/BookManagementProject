#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from core.config_center.schema import AddCaseConfig


class CaseConfigService(object):

    @staticmethod
    async def create_case_config(request_data):
        request_data = AddCaseConfig(**request_data).dict()
        request_data.update({"config_code": CodeCreator.rule_code()})
        create_result = await CaseConfig.create(**request_data)
        data = create_result.__dict__
        return Msg(MsgEnum.SUCCESS).body(data=data)
