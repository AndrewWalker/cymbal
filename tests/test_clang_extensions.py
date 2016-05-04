import os
import unittest
import clang
import clang.cindex
clang.cindex.conf.set_library_path('.')
import cymbal
cymbal.monkey_patch()

class TestClangExtension(unittest.TestCase):

    def parse(self, contents):
        idx = clang.cindex.Index.create()
        name = 'tmp.cpp'
        tu = idx.parse(name, unsaved_files=[(name, contents)], args=['-x','c++','-std=c++11'])
        return tu

    def test_class_template_args(self):
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
