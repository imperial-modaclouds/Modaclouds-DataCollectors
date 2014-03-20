#!/usr/bin/env python
#
# Copyright ${year} deib-polimi
# Contact: imperial <weikun.wang11@imperial.ac.uk>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

from distutils.core import setup, Extension

_sigar = Extension(
    "_sigar",
    ["_sigar.c"],
    include_dirs = ['../java/sigar-bin/include'],
    extra_compile_args = ['-Wall'],
    libraries=['sigar-universal-macosx'],
    library_dirs=['../java/sigar-bin/lib'],
    extra_link_args=[],
    define_macros=[],
    undef_macros=[])

setup(name="pysigar", version="0.1",
      py_modules = ['sigar'],
      ext_modules=[_sigar])