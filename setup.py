from setuptools import setup


setup(
    name="pre_commit_python_dummy_package",
    version=open("VERSION", "r").read().strip(),
    install_requires=["piprot", "docutils"],
    description="Dummy package for installing with pre-commit.",
    long_description=open("README.rst", "r").read(),
    long_description_content_type="text/x-rst",
    url="https://git.shore.co.il/nimrod/python-pre-commit",
    author="Nimrod Adar",
    author_email="nimrod@shore.co.il",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="pre-commit",
)
