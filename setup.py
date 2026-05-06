# Copyright: (c) 2024, Dell Technologies

"""Setup file for PowerStore SDK"""

from setuptools import setup


setup(
    name="mv-pypowerstore",
    version="3.4.2.0",
    description="Python Library for Dell PowerStore Modified by Moviri for use with Dynatrace extensions.",
    author="Moviri",
    author_email="dynatrace_extensions@moviri.com",
    install_requires=[
        "urllib3>=2.6.3",
        "requests>=2.23.0",
        "packaging>=26.0",
        "setuptools>=80.10.2",
    ],
    license_files=("LICENSE",),
    classifiers=["License :: OSI Approved :: Apache Software License"],
    url="https://github.com/dell/python-powerstore",
    packages=["PyPowerStore", "PyPowerStore.utils", "PyPowerStore.objects"],
)
