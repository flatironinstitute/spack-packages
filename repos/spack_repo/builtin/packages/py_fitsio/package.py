# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFitsio(PythonPackage):
    """A python package for FITS input/output wrapping cfitsio"""

    homepage = "https://github.com/esheldon/fitsio"
    pypi = "fitsio/fitsio-1.2.6.tar.gz"

    license("GPL-2.0-or-later", checked_by="lgarrison")

    version("1.4.2", sha256="92a02f0e63d539d85ca5a185ae0cc8d40029270858275964ee2539ee0136f0c3")
    version("1.2.6", sha256="33b0cdbc53f1779e3d0a765d5ab474baf6c86eccf7c21375a07671f7b09b33af")
    version("1.2.5", sha256="001e8689cf82229e19bc20e62494b1eba777aaca7471723ba67a4bac24fdd0d6")

    depends_on("c", type="build")
    depends_on("python@3.10:", when="@1.4:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    # dynamic version; without it setuptools silently records 0.0.0
    depends_on("py-setuptools-scm@8:", type="build", when="@1.4:")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("cfitsio@4.6:", when="@1.4:", type=("build", "link", "run"))
    depends_on("cfitsio@4.4.1:", type=("build", "link", "run"))

    def setup_build_environment(self, env):
        env.set("FITSIO_USE_SYSTEM_FITSIO", "1")
