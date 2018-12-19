from setuptools import setup

setup(
    name='ws',
    version='0.1',
    py_modules=['ws'],
    install_requires=[
        'Click',
    ],
    # metadata to display on PyPI
    author="Olumide Ogundele",
    author_email="olumideralph@gmail.com",
    description="This is a project setup Package",
    entry_points='''
        [console_scripts]
        ws=ws:cli
    ''',
)