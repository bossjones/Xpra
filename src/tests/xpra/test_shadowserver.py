#!/usr/bin/env python
# This file is part of Xpra.
# Copyright (C) 2012, 2013 Antoine Martin <antoine@devloop.org.uk>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import logging
logging.basicConfig(format="%(asctime)s %(message)s")
logging.root.setLevel(logging.DEBUG)

import gtk
from xpra.scripts.config import make_defaults_struct
from xpra.platform.shadow_server import ShadowServer
import gobject
import socket
import os.path

def main():
    from xpra.os_util import set_application_name, set_prgname
    set_prgname("OSX Shadow Test")
    set_application_name("OSX Shadow Test")

    defaults = make_defaults_struct()
    for x in ("daemon", "clipboard", "mmap", "speaker", "microphone",
              "cursors", "bell", "notifications",
              "system_tray", "sharing",
              "delay_tray", "opengl"):
        setattr(defaults, x, False)

    loop_exit = gtk.main_quit
    loop_run = gtk.main


    XPRA_DISPLAY = ":10"
    sp = "~/.xpra/%s-%s" % (socket.gethostname(), XPRA_DISPLAY[1:])
    sockpath = os.path.expanduser(sp)

    listener = socket.socket(socket.AF_UNIX)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.setblocking(1)
    listener.bind(sockpath)
    sockets = [listener]

    ss = ShadowServer()
    ss.init(sockets, defaults)
    ss.run()

    gobject.timeout_add(1000*120, loop_exit)
    loop_run()

if __name__ == "__main__":
    main()
