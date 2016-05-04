import clang.cindex
from ctypes import *

# The libclang bindings are fairly complete - but these two functions are
# omitted as of clang 3.8
#
# This code looks slightly different to the code in libclangs cindex.py
# wrappers - primarily because we're monkeypatching that functionality in
# rather than adding it directly, but ends up being equivalent

f = clang.cindex.conf.lib.clang_Type_getNumTemplateArguments
f.argtypes = [clang.cindex.Type]
f.restype = c_int
def _get_num_template_arguments(self):
    return f(self)

g = clang.cindex.conf.lib.clang_Type_getTemplateArgumentAsType
g.argtypes = [clang.cindex.Type, c_uint]
g.restype = clang.cindex.Type
def _get_template_argument_type(self, idx):
    return g(self, idx)

clang.cindex.Type.get_num_template_arguments = _get_num_template_arguments
clang.cindex.Type.get_template_argument_type = _get_template_argument_type

# This module intentionally exports nothing - it has side effects on the
# libclang (ie/ it monkey patches libclang in place to make the necessary
# changes)
__all__ = []
