from libpymux.panes import ExecPane
import os

class BashPane(ExecPane):
    def __init__(self, pane_executor, pymux_pane_env):
        super().__init__(pane_executor)
        self._pymux_pane_env = pymux_pane_env

    def _do_exec(self):
        os.environ['PYMUX_PANE'] = self._pymux_pane_env
        os.execv('/bin/bash', ['bash'])

