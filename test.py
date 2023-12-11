from typing import NamedTuple, Optional


class MsgData(NamedTuple):
    """ 响应信息 """
    code: int
    message: str = "服务器异常"

a = MsgData(500000, "未查询环境信息")

# print(a.code)
# print(a.message)

from typing import Optional

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person(name: Optional[Person]) -> Optional[str]:
    if name is None:
        return None
    else:
        return name.name

person = Person("Alice")
print(get_person(person))   # 输出: Alice
print(get_person(None))     # 输出: None