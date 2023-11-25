from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.0'
DESCRIPTION = 'A python module for easy file handling.'
LONG_DESCRIPTION = 'A python module for beginners that allows for easy file handling.'

# Setting up
setup(
    name="pyWrite",
    version=VERSION,
    author="ha-rt (Oliver)",
    author_email="<oliver.contactme@proton.me>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'file', 'writing', 'beginner', 'help'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)