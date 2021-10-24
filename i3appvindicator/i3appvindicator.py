#!/usr/bin/env python
import subprocess
from functools import cached_property
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk
from gi.repository.AppIndicator3 import Indicator
from gi.repository.AppIndicator3 import IndicatorCategory
from gi.repository.AppIndicator3 import IndicatorStatus


class i3AppVindicator:
    def __init__(self, title, icon, floating=False):
        self.title = title
        self.icon = icon
        self._floating = floating
        self._criteria = None
        self.criteria = ""

    def set_criteria(self, *criteria):
        self._criteria = criteria
        del self.criteria

    @cached_property
    def criteria(self):
        return " ".join(self._criteria)

    @cached_property
    def floating(self):
        return f"[{self.criteria}] floating disable" if not self._floating else ""

    def run(self):
        if not self.criteria:
            raise ValueError()
        indicator = Indicator.new(self.title, self.icon, IndicatorCategory.APPLICATION_STATUS)
        indicator.set_status(IndicatorStatus.ACTIVE)
        menu, toggle_item = self._get_menu()
        indicator.set_menu(menu)
        indicator.set_secondary_activate_target(toggle_item)
        Gtk.main()

    def _get_menu(self):
        menu = Gtk.Menu()

        toggle_item = Gtk.MenuItem(label='Toggle')
        toggle_item.connect('activate', self.toggle_action)
        menu.append(toggle_item)

        exit_item = Gtk.MenuItem(label='Exit Tray')
        exit_item.connect('activate', self.exit_action)
        menu.append(exit_item)

        menu.show_all()
        return menu, toggle_item

    def toggle_action(self, _):
        try:
            self._show_app()
        except subprocess.CalledProcessError:
            # if couldn't show then it is already visible, hide!
            self._hide_app()

    def _hide_app(self):
        return subprocess.check_call(["i3-msg", f"[{self.criteria}] move scratchpad"])

    def _show_app(self):
        return subprocess.check_call(["i3-msg", f"[{self.criteria}] scratchpad show; {self.floating}"])

    def exit_action(self, _):
        Gtk.main_quit()
