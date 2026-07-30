# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMpsort(PythonPackage):
    """Massively Parallel Histogram Sort"""

    homepage = "https://github.com/rainwoodman/MP-sort"
    pypi = "mpsort/mpsort-0.1.19.tar.gz"

    version("0.1.19", sha256="7f337b96aca53b8b688456fe18ae532919bfabeb991650f9cf64006cc758d24b")

    depends_on("c", type="build")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("mpi")
    depends_on("py-mpi4py", type=("build", "run"))
