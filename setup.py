import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-shortwave',
    version='0.9.0',
    description='Shortwave command file management for Django apps.',
    url='http://github.com/benspaulding/django-shortwave/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.com',
    license='BSD',
    download_url='http://github.com/benspaulding/django-shortwave/tarball/v0.9.0',
    long_description = read('README'),
    packages = ['shortwave', 'shortwave.tests'],
    package_data = {'shortwave': ['fixtures/*',
                                  'locale/*/LC_MESSAGES/*',
                                  'templates/shortwave/*']},
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP :: Site Management'],
)
