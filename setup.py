from setuptools import setup


setup(
        name='pre_commit_python_dummy_package',
        version=open('VERSION', 'r').read().strip(),
        install_requires=['piprot', 'docutils'],
)
