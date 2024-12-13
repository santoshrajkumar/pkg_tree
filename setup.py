from setuptools import setup, find_packages

setup(
    name="pkg_tree",
    version="0.1.0",
    author="Santosh Rajkumar",
    author_email="rajkumar.nits@gmail.com",
    description="A Python package to analyze and generate a tree of Python package structures.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/santoshrajkumar/pkg_tree",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
