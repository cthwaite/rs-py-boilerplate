#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
try:
    import setuptools_rust
    from setuptools_rust import RustExtension, Binding
except ImportError:
    import os, subprocess, sys
    try:
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', 'setuptools-rust'])
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    except subprocess.CalledProcessError as err:
        print("Please install setuptools-rust package")
        raise SystemExit(err.errno)

RUST_EXTENSIONS = [
    RustExtension('rs_py_boilerplate._core',
                  'Cargo.toml',
                  binding=Binding.PyO3,
                  debug=None,
                  strip=setuptools_rust.Strip.Debug,
                  native=True),
]

SETUP_REQUIRES = ['pytest-runner', 'setuptools', 'setuptools_rust']


setup(name='rs_py_boilerplate',
      version='0.0.0',
      author='cthwaite',
      #rust_extensions=RUST_EXTENSIONS,
      packages=['rs_py_boilerplate'],
      setup_requires=SETUP_REQUIRES,
      tests_require=['pytest'],
      zip_safe=False)
