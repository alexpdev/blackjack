#! /env/Scripts/python
# -*- coding: utf-8 -*-

#######################################################################
# BlackJack Card Counting
# Copyright (C) 2021  alexpdev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses
#########################################################################

import os
import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication

TOP = Path(__file__).parent.parent
IMGS = os.path.join(TOP,"img")

sys.path.insert(0,str(TOP))
os.environ["IMG_DIR"] = IMGS

app = QApplication(sys.argv)
