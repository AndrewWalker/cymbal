import cymbal
import unittest


class TestPaths(unittest.TestCase):

    def parse(self, contents):
        idx = clang.cindex.Index.create()
        names = 'tmp.cpp'
        tu = idx.parse(name, unsaved_files=[(name, contents)], args=['-std=c++11'])
        return tu

    def test_class_template_args(self):
        s = '''
        template<typename U, typename V>
        class foo { };

        foo<int, char> f();
        '''
        tu = self.parse(s)
        for cursor in tu.cursor.walk_preorder():
            if cursor.kind == clang.cindex.CursorKind.CLASS_TEMPLATE:
                class_type = cursor.type
                cnt = class_type.get_num_template_arguments()
                for i in xrange(cnt):
                    class_type.get_template_argument_type(i) 


