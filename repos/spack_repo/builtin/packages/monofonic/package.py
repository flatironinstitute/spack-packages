# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Monofonic(CMakePackage):
    """MUSIC2-monofonIC: single-resolution cosmological initial conditions
    generator with higher-order LPT."""

    homepage = "https://github.com/cosmo-sims/monofonIC"
    git = "https://github.com/cosmo-sims/monofonIC.git"

    license("GPL-3.0-only")

    version("1.0b", tag="v1.0b", commit="564d78897506ca571042da4681b492d77117459f")

    variant("mpi", default=True, description="MPI support")
    # CLASS (v3.3.3) is downloaded at configure time via CMake FetchContent
    variant("class", default=True, description="CLASS transfer function support")
    variant("panphasia", default=True, description="PANPHASIA random number generators")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.13:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("gsl")
    depends_on("hdf5")
    depends_on("fftw@3: +openmp precision=float,double,long_double")
    depends_on("fftw@3: +mpi", when="+mpi")
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        return [
            self.define_from_variant("ENABLE_MPI", "mpi"),
            self.define_from_variant("ENABLE_CLASS", "class"),
            self.define_from_variant("ENABLE_PANPHASIA", "panphasia"),
            self.define_from_variant("ENABLE_PANPHASIA_HO", "panphasia"),
        ]

    def install(self, spec, prefix):
        # no install target upstream; the build produces a single executable
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "monofonIC"), prefix.bin)
