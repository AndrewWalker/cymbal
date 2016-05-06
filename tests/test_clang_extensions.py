import unittest
from ctypes import *
import clang
import clang.cindex
import cymbal

class TestClangExtension(unittest.TestCase):

    def parse(self, contents):
        idx = clang.cindex.Index.create()
        name = 'tmp.cpp'
        tu = idx.parse(name, unsaved_files=[(name, contents)], args=['-x','c++','-std=c++11'])
        return tu

    def test_fails_to_add(self):
        with self.assertRaises(cymbal.CymbalException):
            f = cymbal.monkeypatch_type('ignored',
                                        'get_declaration')
        
    def test_class_template_args(self):

        f = cymbal.monkeypatch_type('clang_Type_getTemplateArgumentAsType',
                                    'get_template_argument_type')
        f.argtypes = [clang.cindex.Type, c_uint]
        f.restype = clang.cindex.Type

        g = cymbal.monkeypatch_type('clang_Type_getNumTemplateArguments',
                                    'get_num_template_arguments')
        g.argtypes = [clang.cindex.Type]
        g.restype = c_int

        s = '''
        template<class T, class U>
        class foo {};

        foo<int,char> f();
        '''

        tu = self.parse(s)
        for c in tu.cursor.walk_preorder():
            if c.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                rt = c.result_type
                self.assertEquals( 2, rt.get_num_template_arguments())
                self.assertEquals( 'int', rt.get_template_argument_type(0).spelling )
                self.assertEquals( 'char', rt.get_template_argument_type(1).spelling )
         

if __name__ == '__main__':
    unittest.main()
