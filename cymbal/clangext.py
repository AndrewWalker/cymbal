import clang.cindex
from ctypes import *

__all__ = ['monkeypatch_type', 'monkeypatch_cursor', 'CymbalException']

def find_libclang_function(function):
    return getattr(clang.cindex.conf.lib, function)

class CymbalException(Exception):
    def __init__(self, msg):
        super(CymbalException, self).__init__(msg)

def monkeypatch_helper(classtype, library_function, name):
    if hasattr(classtype, name):
        raise CymbalException('failed to add method, %s is already available' % name) 
    f = find_libclang_function(library_function)
    def impl(*args):
        return f(*args)
    setattr(classtype, name, impl)
    return f

def monkeypatch_type(library_function, name):
    return monkeypatch_helper(clang.cindex.Type, library_function, name)

def monkeypatch_cursor(library_function, name):
    return monkeypatch_helper(clang.cindex.Cursor, library_function, name)

