#-*- coding: utf-8 -*-
#自定义一个常量类
import sys

class _const ():
    class ConstError(Exception): pass
    class UpperCaseError(ConstError): pass
    def __setattr__(self, name: str, value):
        if name in self.__dict__.keys():
            raise self.ConstError("不能重复绑定常量值")
        if not name.isupper():
            raise self.UpperCaseError("'s%'不符合驼峰命名法规则，请重新编写")
        self.__dict__[name] = value

sys.modules[__name__] = _const()