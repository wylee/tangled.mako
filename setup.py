from setuptools import setup, PEP420PackageFinder


setup(
    name='tangled.mako',
    version='1.0a6.dev0',
    description='Tangled Mako integration',
    long_description=open('README.rst').read(),
    url='https://tangledframework.org/',
    download_url='https://github.com/TangledWeb/tangled.mako/tags',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    include_package_data=True,
    packages=PEP420PackageFinder.find(include=['tangled*']),
    install_requires=[
        'tangled.web>=1.0a12',
        'Mako>=1.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
