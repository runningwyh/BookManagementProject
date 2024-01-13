from typing import NamedTuple, Optional


class MsgData(NamedTuple):
    """ 响应信息 """
    code: int
    message: str = "服务器异常"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MsgData):
            raise NotImplemented
        return self.code == other.code

a = MsgData(500000, "未查询环境信息")

print(MsgData(500000, "未查询环境信息"))
print(a.message)

from typing import Optional

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person(name: Optional[Person]) -> Optional[str]:
    if name is None:
        return None
    else:
        return name.name

