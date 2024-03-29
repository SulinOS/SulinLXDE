#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
	#Not sure but it is not needed (obsoleteman)
    autotools.autoreconf("-fiv")

    autotools.configure("--enable-gtk3")

def build():
    autotools.make()

def install():
    autotools.install()
    inarytools.dodoc("AUTHORS", "COPYING")
