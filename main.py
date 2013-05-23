# -*- coding: utf-8 -*-
# PEP8:OK, LINT:OK, PY3:OK


#############################################################################
## This file may be used under the terms of the GNU General Public
## License version 2.0 or 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http:#www.fsf.org/licensing/licenses/info/GPLv2.html and
## http:#www.gnu.org/copyleft/gpl.html.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#############################################################################


# metadata
' Ninja-IDE Link Checker '
__version__ = ' 0.4 '
__license__ = ' GPL '
__author__ = ' juancarlospaco '
__email__ = ' juancarlospaco@ubuntu.com '
__url__ = ''
__date__ = ' 05/05/2013 '
__prj__ = ' linkcheck '
__docformat__ = 'html'
__source__ = ''
__full_licence__ = ''


# imports
from sip import setapi
from PyQt4.QtGui import QIcon, QLabel, QDockWidget, QScrollArea

try:
    from PyKDE4.kdecore import KPluginLoader
    from PyKDE4.kparts import *
except ImportError:
    pass

from ninja_ide.core import plugin


# API 2
(setapi(a, 2) for a in ("QDate", "QDateTime", "QString", "QTime", "QUrl",
                        "QTextStream", "QVariant"))


###############################################################################


class Main(plugin.Plugin):
    " dock Class "
    def initialize(self):
        " Init Class dock "
        self.dock = QDockWidget()
        self.dock.setFeatures(QDockWidget.DockWidgetFloatable |
                              QDockWidget.DockWidgetMovable)
        self.dock.setWindowTitle(__doc__)
        self.dock.setStyleSheet('QDockWidget::title{text-align: center;}')
        self.scrollable = QScrollArea()
        self.dock.setWidget(self.scrollable)
        try:
            self.factory = KPluginLoader("klinkstatuspart").factory()
            self.scrollable.setWidget(self.factory.create(self).widget())
        except:
            self.scrollable.setWidget(QLabel(""" <center> <h3>ಠ_ಠ<br>
            ERROR: Please, install KLinkCheck and PyKDE ! </h3><br>
            <br><i> (Sorry, cant embed non-Qt Apps). </i><center>"""))
        self.misc = self.locator.get_service('misc')
        self.misc.add_widget(self.dock, QIcon.fromTheme("insert-link"), __doc__)


###############################################################################


if __name__ == "__main__":
    print(__doc__)
