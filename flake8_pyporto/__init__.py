import ast
import os

from flake8.formatting import base

# import tokenize
# import collections
# import token as mod_token

# try:
#     import pycodestyle
# except ImportError:
#     import pep8 as pycodestyle

# try:
#     from flake8.engine import pep8 as stdin_utils
# except ImportError:
#     from flake8 import utils as stdin_utils


# def get_tokens(filename):
#     if filename == 'stdin':
#         file_contents = stdin_utils.stdin_get_value().splitlines(True)
#     else:
#         file_contents = pycodestyle.readlines(filename)
#     file_contents_iter = iter(file_contents)

#     def file_contents_next():
#         return next(file_contents_iter)

#     for t in tokenize.generate_tokens(file_contents_next):
#         yield Token(t)





# class PyPorto(base.BaseFormatter):
class PyPorto:
    """Flake8's PyPorto formatter."""

    name = __name__
    version = '2.0'

    # def format(self, error):
    #     print(2)
    #     return 'Example formatter: {0!r}'.format(error)


    # def run(self, error):
    #     print(1)
    #     return 'asdsad'

    def get_filename_wrapper(self, filename):
        return filename

    def __init__(self, tree, filename='(none)', file_tokens=None):
        print("__init__")
        
        filename = self.get_filename_wrapper(filename)

        fn = 'stdin' if filename in ('stdin', '-', None) else filename
        self.filename = fn
        self.tokens = file_tokens
        # print(tree)
        
        self.errors = []
<<<<<<< HEAD

        print("self.filename", self.filename)

        # print("__init__")

        # print(self.tokens)

=======
        
        print("self.filename", self.filename)
        
        # print("__init__")
        
        # print(self.tokens)
        
>>>>>>> 90a79c52c47b074f2bd4bc390a617e750417f477
        a = os.path.split(self.filename)
        
        print("a", a)
        
        b = a[-1].split('_')
        
        # print('b', b)
        if len(b) >= 2:
            # print(11, b[-1], b[-2])
            
            if b[-1] == 'task.py':
                print(self.filename)

                class_instance_as_three = tree
                # print(ast.dump(tree, indent=4))

                # print(class_instance_as_three.body)
                for i in class_instance_as_three.body:
                    print(i)
                    print(type(i))
                    if isinstance(i, ast.ClassDef):
                        # print(ast.dump(i, indent=4))
                        
                        print("i.name", i.name)
                        
                        
                        # comparison = node.operand
                        # left = astor.to_source(comparison.left).strip()
                        # right = astor.to_source(comparison.comparators[0]).strip()
                        # errors.append((node.lineno, node.col_offset, "asdasd"))
                        print(i.name[-4:])
                        if i.name[-4:] != 'Task':
                            self.errors.append((1, 1, 'PYP001 is bad'))
                        
                        # for ii in i.bases:
                        #     ...
                        #     print(ii)
                        #     print(dir(ii))


                # for i in class_instance_as_three:
                #     print(i)
        # class_instance_as_text = inspect.getsource(class_instance)

        # class_instance_as_three = ast.parse(
        #     class_instance_as_text,
        #     # mode='eval'
        # )


    def run(self):
        # file_tokens = self.tokens
        filename = self.filename
        # noqa_line_numbers = ()
        tokens = None
        
        print("run")

        # if file_tokens is None:  # flake8 2.x
        #     tokens = list(get_tokens(filename))
        #     noqa_line_numbers = get_noqa_lines(tokens)
        # else:
        #     tokens = (Token(t) for t in file_tokens)


        # ast.parse(source, filename=filename)
        
        # print()

        for line_number, offset, text in self.errors:
            yield (
                line_number,
                offset,
                text,
                type(self),
            )
