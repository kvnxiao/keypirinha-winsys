from . import action
from . import keyword
from .lib import system as sys_func


class SystemActions(action.KPActions):
    def __init__(self, winsys):
        # Empty Recycle Bin
        self.actions[keyword.KEYWORD_EMPTY_RECYCLE_BIN] = action.Action(
            keyword.KEYWORD_EMPTY_RECYCLE_BIN,
            "Empty the Recycle Bin.",
            winsys.load_resource_image("empty_recycle_bin.png"),
            sys_func.empty_recycling_bin
        )
