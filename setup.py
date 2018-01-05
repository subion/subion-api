"""Setup subion_api."""
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_mako',
    'pyramid_debugtoolbar',
    'waitress',
    'pyjwt',
    'cryptography',
    'pymongo',
    'mongoengine',
    'bcrypt',
    'jsonschema',
    'blinker',
]

developments_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
    'pyramid_ipython',
    'mypy',
    'mypy-extensions',
    'flake8',
    'yapf',
    'pep8-naming',
    'flake8-docstrings',
]

setup(
    name='subion_api',
    version='0.0',
    description='subion-api',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='GuoJiaqi',
    author_email='gjq.uoiai@outlook.com',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'developing': developments_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': ['main = subion_api:main'],
    },
)
