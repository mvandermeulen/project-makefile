from setuptools import find_packages, setup

VERSION = "0.1.0-dev"

setup(
    author="Jeffrey A. Clark (Alex)",
    author_email="aclark@aclark.net",
    classifiers=[],
    description="A generic makefile for projects.",
    entry_points={
        "console_scripts": ["project-makefile=install:main"],
    },
    include_package_data=True,
    install_requires=[],
    keywords="",
    license="",
    long_description=open("README.rst").read(),
    name="project-makefile",
    namespace_packages=[],
    packages=find_packages(),
    py_modules=["install"],
    test_suite="",
    url="https://github.com/project-makefile/project-makefile",
    version=VERSION,
    zip_safe=False,
)
