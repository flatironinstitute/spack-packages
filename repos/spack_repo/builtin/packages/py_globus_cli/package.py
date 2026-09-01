# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGlobusCli(PythonPackage):
    """Globus CLI is a standalone application that can be installed on the user's machine
    and is used to access the Globus service. The CLI provides an interface to Globus
    services from the shell, and is suited to both interactive and simple scripting use cases."""

    homepage = "https://docs.globus.org/cli"
    git = "https://github.com/globus/globus-cli.git"
    url = "https://github.com/globus/globus-cli/archive/refs/tags/3.16.0.zip"

    maintainers("climbfuji")

    version("3.43.0", sha256="c31c266791abc9c2f064551bbd751c54e9de972e0dd2d3173a8844869cc63dbd")
    version("3.16.0", sha256="0ef721060870d9346505e52b9bf30c7bed6ae136cc08762deb2f8893bd25d8c5")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("python@3.10:", when="@3.43:", type=("build", "run"))
    depends_on("py-setuptools", when="@3.16.0", type="build")
    depends_on("py-flit-core@3.11:3", when="@3.43:", type="build")
    depends_on("py-globus-sdk@3.25.0", when="@3.16.0", type=("build", "run"))
    depends_on("py-globus-sdk@4.9.0", when="@3.43.0", type=("build", "run"))
    depends_on("py-click@8", when="@3.16.0", type=("build", "run"))
    depends_on("py-click@8.4", when="@3.43.0", type=("build", "run"))
    depends_on("py-jmespath@1.0.1", when="@3.16.0", type=("build", "run"))
    depends_on("py-jmespath@1.1.0", when="@3.43.0", type=("build", "run"))
    depends_on("py-packaging@17:", type=("build", "run"))
    depends_on("py-requests@2.34.2:2", when="@3.43:", type=("build", "run"))
    depends_on("py-typing-extensions@4:", when="@3.43: ^python@:3.10", type=("build", "run"))
