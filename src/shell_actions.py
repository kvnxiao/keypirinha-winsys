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

        # AppData
        self.actions[keyword.SHELL_APP_DATA] = action.Action(
            keyword.SHELL_APP_DATA,
            "Opens the user's AppData folder",
            winsys.load_resource_image("folder.png"),
            shell_func.open_appdata
        )

        # Local AppData
        self.actions[keyword.SHELL_LOCAL_APP_DATA] = action.Action(
            keyword.SHELL_LOCAL_APP_DATA,
            "Opens the user's AppData/Local folder",
            winsys.load_resource_image("folder.png"),
            shell_func.open_local_appdata
        )

        # LocalLow AppData
        self.actions[keyword.SHELL_LOCAL_LOW_APP_DATA] = action.Action(
            keyword.SHELL_LOCAL_LOW_APP_DATA,
            "Opens the user's AppData/LocalLow folder",
            winsys.load_resource_image("folder.png"),
            shell_func.open_locallow_appdata
        )

        # Desktop
        self.actions[keyword.SHELL_DESKTOP] = action.Action(
            keyword.SHELL_DESKTOP,
            "Opens the user's Desktop folder",
            winsys.load_resource_image("desktop.png"),
            shell_func.open_desktop
        )

        # Downloads
        self.actions[keyword.SHELL_DOWNLOADS] = action.Action(
            keyword.SHELL_DOWNLOADS,
            "Opens the user's Downloads folder",
            winsys.load_resource_image("downloads.png"),
            shell_func.open_downloads
        )

        # Documents
        self.actions[keyword.SHELL_DOCUMENTS] = action.Action(
            keyword.SHELL_DOCUMENTS,
            "Opens the user's Documents folder",
            winsys.load_resource_image("documents.png"),
            shell_func.open_documents
        )
