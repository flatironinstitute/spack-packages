# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Music2(CMakePackage):
    """MUSIC2: multi-scale (zoom) cosmological initial conditions generator,
    the successor of MUSIC."""

    homepage = "https://github.com/cosmo-sims/MUSIC"
    git = "https://github.com/cosmo-sims/MUSIC.git"

    license("GPL-3.0-only")

    version("2025-08-25", commit="967651b21d9bf52f9017982d4b8a5edb5c59ecb0")
    version("2.0-beta", tag="v2.0-beta", commit="ed259a9fcd8ee6f1a09710bc1a8428183dfbb384")

    # CLASS is downloaded at configure time via CMake FetchContent
    variant("class", default=True, description="CLASS transfer function support")
    variant("panphasia", default=True, description="PANPHASIA random number generator")
    variant("hdf5", default=True, description="HDF5 output formats")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.11:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("gsl")
    depends_on("fftw@3: +openmp precision=float,double,long_double")
    depends_on("hdf5", when="+hdf5")

    def cmake_args(self):
        return [
            self.define_from_variant("ENABLE_CLASS", "class"),
            self.define_from_variant("ENABLE_PANPHASIA", "panphasia"),
        ]

    def install(self, spec, prefix):
        # no install target upstream; the build produces a single executable
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "MUSIC"), prefix.bin)
