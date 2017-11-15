from . import action
from . import keyword
from .lib import win as shell_func


class ShellActions(action.KPActions):
    def __init__(self, winsys):
        # Open Recycle Bin
        self.actions[keyword.SHELL_OPEN_RECYCLE_BIN] = action.Action(
            keyword.SHELL_OPEN_RECYCLE_BIN,
            "Opens the Recycle Bin folder",
            winsys.load_resource_image("recycle_bin.png"),
            shell_func.open_recycling_bin
        )
