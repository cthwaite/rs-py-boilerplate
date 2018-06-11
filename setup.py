#!/usr/bin/env python
# coding: utf-8

import subprocess

from contextlib import contextmanager
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.test import test


try:
    import setuptools_rust
except ImportError:
    import os, subprocess, sys
    try:
        subprocess.check_call([sys.executable, '-m', 'pip',
                               'install', 'setuptools-rust'])
        os.execvp(sys.executable, [sys.executable] + sys.argv)

        import setuptools_rust
    except subprocess.CalledProcessError as err:
        print('Please install setuptools-rust package')
        raise SystemExit(err.errno)

from setuptools_rust import RustExtension, Binding
from setuptools_rust.build import build_rust


RUST_EXTENSIONS = [
    RustExtension('rs_py_boilerplate._core',
                  'Cargo.toml',
                  binding=Binding.PyO3,
                  debug=None,
                  strip=setuptools_rust.Strip.Debug,
                  native=True)
]


@contextmanager
def ensure_nightly():
    '''Temporarily switch to the nightly toolchain, if not already using it.
    '''
    switched = False
    ret = subprocess.check_output('rustc -V'.split())
    if 'nightly' not in ret.decode('utf-8'):
        print('switching to nightly toolchain')
        subprocess.check_call('rustup default nightly'.split())
        switched = True
    yield
    if switched:
        print('switching back to stable toolchain')
        output = subprocess.check_output('rustup default stable'.split())


class EnsureNightlyInstall(install):
    def run(self):
        with ensure_nightly():
            super().run()

class EnsureNightlyTest(test):
    def run(self):
        with ensure_nightly():
            super().run()

class EnsureNightlyBuild(build_rust):
    def run(self):
        with ensure_nightly():
            super().run()



SETUP_REQUIRES = ['pytest-runner', 'setuptools', 'setuptools_rust']


setup(name='rs_py_boilerplate',
      version='0.0.0',
      author='cthwaite',
      packages=['rs_py_boilerplate'],
      rust_extensions=RUST_EXTENSIONS,
      setup_requires=SETUP_REQUIRES,
      tests_require=['pytest'],
      cmdclass = {
          'test': EnsureNightlyTest,
          'build_rust': EnsureNightlyBuild,
          'install': EnsureNightlyInstall
      },
      zip_safe=False)
