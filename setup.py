from setuptools import setup


setup(
    name='tangled.mako',
    version='0.1a2.dev0',
    description='Tangled Mako integration',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    include_package_data=True,
    packages=[
        'tangled',
        'tangled.mako',
        'tangled.mako.tests',
    ],
    install_requires=[
        'tangled.web>=0.1.dev0',
        'Mako>=0.9.1',
    ],
    extras_require={
        'dev': [
            'tangled[dev]',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
