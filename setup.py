from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pyodbc"]
packages = ["pydb"]

setup(
    name="pydb",
    version="0.0.1",
    author="Pablo Valverde",
    author_email="pabludo8cho@gmail.com",
    description="Database API wrapper for python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Pablo-Valverde/pydb",
    packages=packages,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)