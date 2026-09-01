# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class MpiRockstar(MakefilePackage):
    """MPI-Rockstar: a Hybrid MPI and OpenMP Parallel Implementation of the Rockstar Halo finder"""

    homepage = "https://github.com/Tomoaki-Ishiyama/mpi-rockstar"
    url = "https://github.com/Tomoaki-Ishiyama/mpi-rockstar/archive/97eb6c1da2fb31380ab9cd495173c5b59da47a6c.tar.gz"

    license("GPL-3.0-only", checked_by="lgarrison")

    # the commit the (moved) v1.0.0 tag pointed at when the JOSS paper was
    # accepted; preferred because describe-style version strings don't sort
    version(
        "1.0.0.2026-03-24.5febd8c",
        url="https://github.com/Tomoaki-Ishiyama/mpi-rockstar/archive/5febd8c16d4246cdf457d5d50f1fe52dcc8c092f.tar.gz",
        sha256="b64c5292ec02884f1c0f8051b2014c8918cd23310e0958a712f90d734c070d1d",
        preferred=True,
    )
    version(
        "v1.0.0-31-g97eb6c1",
        sha256="c227a8ab2296b0e8343920f93b4028f519f45a000a724f98fc06b510f0e9a072",
    )

    variant("hdf5", default=False, description="Enable HDF5 support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("mpi")
    depends_on("hdf5", when="+hdf5")
    depends_on("libtirpc")

    build_directory = "src"

    def edit(self, spec, prefix):
        makefile = FileFilter(join_path(self.build_directory, "Makefile"))
        makefile.filter(r"-I/usr/include/tirpc", "")
        makefile.filter(r"-std=c\+\+11", "-std=c++14")

    @property
    def build_targets(self):
        targets = ["find_parents"]
        if "+hdf5" in self.spec:
            targets += ["mpi-rockstar_hdf5"]
        else:
            targets += ["mpi-rockstar"]
        return targets

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("find_parents", prefix.bin)

        if "+hdf5" in spec:
            install("mpi-rockstar_hdf5", prefix.bin)
        else:
            install("mpi-rockstar", prefix.bin)
