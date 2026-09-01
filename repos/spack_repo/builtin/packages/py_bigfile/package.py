# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyBigfile(PythonPackage):
    """A reproducible massively parallel IO library for hierarchical data"""

    homepage = "https://github.com/rainwoodman/bigfile"
    pypi = "bigfile/bigfile-0.1.51.tar.gz"

    version("0.1.52", sha256="9137c208b9fd965c9e33c8cbd684c67ad3f2386b68585f8177941a19dd9ef5db")
    version("0.1.51", sha256="1fad962defc7a5dff2965025dff9a3efa23594e1c2300de0c9a43940d4717b65")

    variant("mpi", default=True, description="MPI support")

    depends_on("py-setuptools", type="build")

    depends_on("py-cython", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    depends_on("mpi", when="+mpi")
    depends_on("py-mpi4py", type=("build", "run"), when="+mpi")

    def patch(self):
        # removing cythonized file from sdist
        remove('bigfile/pyxbigfile.c')
