from setuptools import setup, find_packages
import sys, os

version = '0.5'

setup(
    name='pythonopensubtitles',
    version=version,
    description="Wrapper to use the OpenSubtitles API for domain opensubtitles.org",
    keywords='opensubtitles python api',
    author='\xc3\x81lex Gonz\xc3\xa1lez, Sebastian Pfeifer',
    author_email='agonzalezro@gmail.com, pfeifer_s@web.de',
    url='http://twitter.com/agonzalezro',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'Support for encoding detection on downloaded subtitle':
            [
                'charset_normalizer'
            ],
    }
)
