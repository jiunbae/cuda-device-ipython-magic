# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name              = 'cuda-device-ipython-magic',
    version           = '0.1.0',
    description       = 'set CUDA_VISIBLE_DEVICES in ipython',
    long_description  = open('README.md').read(),
    author            = 'Maydev',
    author_email      = 'alice.maydev@gmail.com',
    url               = 'https://github.com/MaybeS/cuda-device-ipython-magic',
    license           = 'MIT',
    install_requires  = (
        'ipython',
    ),
    classifiers       = [
        'Development Status :: 3 - Alpha',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
