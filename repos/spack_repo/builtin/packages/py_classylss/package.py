# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyClassylss(PythonPackage):
    """a lightweight Python binding of the CLASS CMB Boltzmann code"""

    homepage = "https://github.com/nickhand/classylss"
    pypi = "classylss/classylss-0.2.9.tar.gz"

    # 0.3.x is upstream again (bundles CLASS 3.x; 0.2.9.x bundled CLASS 2.x)
    version("0.3.1", sha256="162dd3c10b9345d6ecf73c4e50e7a1c8650254a2f178c170b259c2994595a150")
    version("0.2.9.1", git="https://github.com/sbird/classylss.git", commit="6006fabb5abeab2611ab3300a5c927f447e9c9f0")
    version("0.2.9", sha256="1a8521d2bf9da3d2572245e801e243fcf76f7518b59cbe525a31aa80a884dd86")

    depends_on("python@:3.11", type=("build", "run"), when="@=0.2.9")

    depends_on("py-setuptools@42:", type="build", when="@0.2.9.1:")
    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type=("build", "run"), when="@0.3:")
    depends_on("py-cython", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-six", type=("build", "run"), when="@:0.2")

    patch('setup.py.patch', sha256='2ccf53b90f76cfd4643877bd9952c474dad1ac8a0a2d9daf2bee29c36972dec0', when="@=0.2.9")

    @when("@0.2.9.1")
    def patch(self):
        filter_file(r"'language': 'c'", "'language': 'c++'", "setup.py")

    @when("@=0.2.9")
    def patch(self):
        # Shouldn't rely on the Cythonized output being portable
        remove('classylss/binding.c')
