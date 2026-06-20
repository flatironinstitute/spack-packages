# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class HealpixCxx(AutotoolsPackage, SourceforgePackage):
    """Healpix-CXX is a C/C++ library for calculating
    Hierarchical Equal Area isoLatitude Pixelation of a sphere."""

    homepage = "https://healpix.sourceforge.io"
    sourceforge_mirror_path = "healpix/healpix_cxx-3.50.0.tar.gz"

    license("GPL-2.0-or-later", checked_by="lgarrison")

    version(
        "3.83",
        url="https://downloads.sourceforge.net/project/healpix/Healpix_3.83/Healpix_3.83_2024Nov13.tar.gz",
        sha256="8876c18efc596fd706b2a004ac15f2fb60b795f2db6fbabea9d8ccf549531dda",
    )
    version("3.82", sha256="47629f057a2daf06fca3305db1c6950edb9e61bbe2d7ed4d98ff05809da2a127")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cfitsio@3")
