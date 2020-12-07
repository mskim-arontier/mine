import re

from setuptools import find_namespace_packages, setup


def find_version(path):
    with open(path, 'r', encoding='utf-8') as stream:
        return re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]",
            stream.read(),
            re.M,
        ).group(1)


def read_long_description(path):
    with open(path, 'r', encoding='utf-8') as stream:
        return stream.read()


# @see https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords  # noqa
# @see https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages  # noqa
setup(
    name='python-template',
    version=find_version('arontier/yours/__init__.py'),
    packages=find_namespace_packages(include=['arontier.*']),
    include_package_data=True,
    license='Arontier Proprietary License',
    description='Arontier Python package template',
    long_description=read_long_description('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/arontier/python-template',
    author='Eagu Kim',
    author_email='egkim@arontier.co',
    zip_safe=False,
    scripts=[
        'bin/drive-yours',
    ],
    python_requires='>=3.6',
    setup_requires=[
        'setuptools>=38.6.0',
    ],
    install_requires=[
        # LIST THE DEPENDENCIES OF YOUR PACKAGE
        # FOR INSTANCE,
        # 'numpy==1.18.1',
        # 'pillow==6.2.1',
    ],
    keywords='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
