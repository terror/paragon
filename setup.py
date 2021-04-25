import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="paragon",
    version="1.0.0",
    author="Liam Scalzulli",
    author_email="liamscalzulli@gmail.com",
    description=("A tiny command line benchmarking utility"),
    long_description_content_type="text/markdown",
    license="BSD",
    keywords="benchmark, benchmarking",
    url="http://packages.python.org/paragon",
    project_urls={"Source Code": "https://github.com/terror/paragon"},
    packages=find_packages(),
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["click", "progress", "colorama"],
    entry_points={"console_scripts": ["paragon = paragon.cli:cli"]},
    python_requires=">=3.7",
)
