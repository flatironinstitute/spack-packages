# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKdcount(PythonPackage):
    """ KDTree for low dimensional spatial indexing, a Python extension"""

    homepage = "https://github.com/rainwoodman/kdcount"
    pypi = "kdcount/kdcount-0.3.30.tar.gz"

    version("0.3.30", sha256="9375f298fbfdfeabce01a1a548ecd1fcfebb109f531819deadea94bfc21910e4")

    variant('sharedmem', default=True, description='Use sharedmem')

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-sharedmem", type=("build", "run"), when='+sharedmem')
