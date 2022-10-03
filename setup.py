from __future__ import with_statement

import setuptools

requires = [
    'flake8 > 3.0.0',
]

setuptools.setup(
    name='flake8_pyporto',
    license='MIT',
    version='0.1',
    description='our extension to flake8',
    author='Me',
    author_email='example@example.com',
    url='https://github.com/discoroveryx/flake8-pyporto',
    packages=[
        'flake8_pyporto',
    ],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'PYP001 = flake8_pyporto:PyPorto',
        ],
    },
    classifiers=[
        'Framework :: Flake8',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
