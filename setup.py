from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mandarin",
    version="0.0.1a1",
    description="Template engine for Python",
    packages=["citrine"],
    py_modules=["citrine"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/password-mixin",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com",
)
