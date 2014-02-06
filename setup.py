from setuptools import setup, find_packages


setup(
    name='tangled.mako',
    version='0.1.dev0',
    description='Tangled Mako integration',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=find_packages(),
    install_requires=(
        'tangled.web>=0.1.dev0',
        'Mako>=0.9.1',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
        ),
    },
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
