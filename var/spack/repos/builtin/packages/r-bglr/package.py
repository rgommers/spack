# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RBglr(RPackage):
    """Bayesian Generalized Linear Regression."""

    cran = "BGLR"

    version('1.0.9', sha256='440a96f9f502e0d6ecc8c00720d1ccdbab5ee8223e1def6c930edaa9a9de9099')
    version('1.0.8', sha256='5e969590d80b2f272c02a43b487ab1ffa13af386e0342993e6ac484fc82c9b95')

    depends_on('r@3.5.0:', type=('build', 'run'))
    depends_on('r-truncnorm', type=('build', 'run'))
    depends_on('r-mass', type=('build', 'run'), when='@1.0.9:')
