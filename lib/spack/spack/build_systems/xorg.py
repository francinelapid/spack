# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import spack.util.url
import spack.package


class XorgPackage(spack.package.PackageBase):
    """Mixin that takes care of setting url and mirrors for x.org
       packages."""
    #: Path of the package in a x.org mirror
    xorg_mirror_path = None

    #: List of x.org mirrors used by Spack
    base_mirrors = [
        'https://www.x.org/archive/individual/',
        'https://mirrors.ircam.fr/pub/x.org/individual/',
        'http://xorg.mirrors.pair.com/individual/'
    ]

    @property
    def urls(self):
        self._ensure_xorg_mirror_path_is_set_or_raise()
        return [
            spack.util.url.join(m, self.xorg_mirror_path,
                                resolve_href=True)
            for m in self.base_mirrors
        ]

    def _ensure_xorg_mirror_path_is_set_or_raise(self):
        if self.xorg_mirror_path is None:
            cls_name = type(self).__name__
            msg = ('{0} must define a `xorg_mirror_path` attribute'
                   ' [none defined]')
            raise AttributeError(msg.format(cls_name))
