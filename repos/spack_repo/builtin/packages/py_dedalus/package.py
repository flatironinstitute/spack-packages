# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDedalus(PythonPackage):
    """A flexible framework for solving PDEs with modern spectral methods."""

    homepage = "https://dedalus-project.readthedocs.io"
    pypi = "dedalus/dedalus-3.0.5.tar.gz"

    license("GPL-3.0-or-later")

    version("3.0.5", sha256="4b504ef52dcd0eb176d136edb85e8adcd79b57af357137d4af85ecc1a0c7e47c")

    depends_on("c", type="build")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython@3.0.5:", type="build")

    depends_on("mpi")
    depends_on("fftw@3: +mpi")

    depends_on("py-mpi4py@2.0.0:", type=("build", "run"))
    depends_on("py-numpy@1.20.0:", type=("build", "run"))
    depends_on("py-docopt", type=("build", "run"))
    depends_on("py-h5py@3:", type=("build", "run"))
    depends_on("py-matplotlib@3.7.0:", type=("build", "run"))
    depends_on("py-numexpr", type=("build", "run"))
    depends_on("py-py", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-pytest-benchmark", type=("build", "run"))
    depends_on("py-pytest-cov", type=("build", "run"))
    depends_on("py-pytest-xdist", type=("build", "run"))
    depends_on("py-scipy@1.4.0:", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set("FFTW_PATH", self.spec["fftw"].prefix)
        env.set("MPI_PATH", self.spec["mpi"].prefix)
