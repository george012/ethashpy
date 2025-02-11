#!/usr/bin/env python
import os
from distutils.core import setup, Extension
sources = [
    'src/python/core.c',
    'src/libethash/io.c',
    'src/libethash/internal.c',
    'src/libethash/sha3.c',
    ]
if os.name == 'nt':
    sources += [
        'src/libethash/util_win32.c',
        'src/libethash/io_win32.c',
        'src/libethash/mmap_win32.c',
    ]
else:
    sources += [
        'src/libethash/io_posix.c'
    ]
depends = [
    'src/libethash/ethash.h',
    'src/libethash/compiler.h',
    'src/libethash/data_sizes.h',
    'src/libethash/endian.h',
    'src/libethash/ethash.h',
    'src/libethash/io.h',
    'src/libethash/fnv.h',
    'src/libethash/internal.h',
    'src/libethash/sha3.h',
    'src/libethash/util.h',
    'src/libethash/nmap.h',
    'src/libethash/sha3.h',
    ]
ethashpy = Extension('ethashpy',
                     sources=sources,
                     depends=depends,
                     extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"])

setup(
    name='ethashpy',
    author="WMYeah",
    author_email="george012@163.com",
    license='MIT',
    version='0.0.1',
    url='https://github.com/george012/ethashpy',
    download_url='https://github.com/george012/ethashpy/v0.0.1',
    description=('修改的Python适配包'),
    ext_modules=[ethashpy],
)

