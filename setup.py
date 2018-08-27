#/usr/bin/env python
import os
from setuptools import setup, find_packages

import photologue


def get_requirements(source):
    # https://stackoverflow.com/questions/49837301/pip-10-no-module-named-pip-req
    with open(source) as f:
        required = f.read().strip().split('\n')
    # Temp situation: transition from PIL to Pillow, add a hook so people can
    # skip installing Pillow.
    if os.path.exists('/tmp/PHOTOLOGUE_NO_PILLOW'):
        required = [item for item in required if not item.startswith('Pillow')]
    return required

setup(
    name="django-photologue",
    version=photologue.__version__,
    description="Powerful image management for the Django web framework.",
    author="Justin Driscoll, Marcos Daniel Petry, Richard Barran",
    author_email="justin@driscolldev.com, marcospetry@gmail.com, richard@arbee-design.co.uk",
    url="https://github.com/jdriscoll/django-photologue",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Utilities'],
    install_requires=get_requirements('requirements.txt'),
)
