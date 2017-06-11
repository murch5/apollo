from distutils.core import setup
from process.__init__ import __version__ as version

setup(
    name='process',
    version=version,
    packages=['process'],
    url='',
    license='',
    author='Ryan',
    author_email='',
    description='Data processing classes', requires=['pandas', 'matplotlib']
)
