import clang.cindex
from ctypes import *

__all__ = ['monkeypatch_type', 'monkeypatch_cursor', 'CymbalException']

def find_libclang_function(function):
    return getattr(clang.cindex.conf.lib, function)

class CymbalException(Exception):
    def __init__(self, msg):
        super(CymbalException, self).__init__(msg)

def monkeypatch_helper(classtype, name, library_function, args, result):
    if hasattr(classtype, name):
        raise CymbalException('failed to add method, %s is already available' % name) 
    f = find_libclang_function(library_function)
    f.argtypes = args
    f.restype = result
    def impl(*args):
        return f(*args)
    setattr(classtype, name, impl)

def monkeypatch_type(method_name, library_function, args, result):
    monkeypatch_helper(clang.cindex.Type, method_name, library_function, args, result)

def monkeypatch_cursor(method_name, library_function, args, result):
    monkeypatch_helper(clang.cindex.Cursor, method_name, library_function, args, result)

