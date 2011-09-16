import os

from distutils.core import setup

from shortwave import VERSION


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-shortwave',
    version=VERSION,
    description='Django app for managing Shortwave command files.',
    url='https://github.com/benspaulding/django-shortwave/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    license='BSD',
    download_url='https://github.com/benspaulding/django-shortwave/tarball/v%s' % VERSION,
    long_description = read('README.rst'),
    packages = [
        'shortwave',
        'shortwave.tests'
    ],
    package_data = {
        'shortwave': [
            'fixtures/*',
            'locale/*/LC_MESSAGES/*',
            'templates/shortwave/*',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
