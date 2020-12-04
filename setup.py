from setuptools import setup
from definitions import (
    NAME,
    VERSION,
    PACKAGES,
    URL,
    LICENSE,
    AUTHOR,
    AUTHOR_EMAIL,
    DESCRIPTION,
    INSTALL_REQUIRES,
)

setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    url=URL,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
)
