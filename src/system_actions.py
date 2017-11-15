from . import action
from . import keyword
from .lib import win as sys_func


class SystemActions(action.KPActions):
    def __init__(self, winsys):
        # Empty Recycle Bin
        self.actions[keyword.SYSTEM_EMPTY_RECYCLE_BIN] = action.Action(
            keyword.SYSTEM_EMPTY_RECYCLE_BIN,
            "Empty the Recycle Bin",
            winsys.load_resource_image("recycle_empty.png"),
            sys_func.empty_recycling_bin
        )

        # Lock
        self.actions[keyword.SYSTEM_LOCK] = action.Action(
            keyword.SYSTEM_LOCK,
            "Locks the computer and brings you to the lock screen",
            winsys.load_resource_image("lock.png"),
            sys_func.lock
        )

        # Hibernate
        self.actions[keyword.SYSTEM_HIBERNATE] = action.Action(
            keyword.SYSTEM_HIBERNATE,
            "Puts the computer into hibernate mode",
            winsys.load_resource_image("hibernate.png"),
            sys_func.hibernate
        )

        # Logout
        self.actions[keyword.SYSTEM_LOGOUT] = action.Action(
            keyword.SYSTEM_LOGOUT,
            "Logs out the current user",
            winsys.load_resource_image("logout.png"),
            sys_func.logout
        )

        # Sleep
        self.actions[keyword.SYSTEM_SLEEP] = action.Action(
            keyword.SYSTEM_SLEEP,
            "Puts the computer to sleep",
            winsys.load_resource_image("sleep.png"),
            sys_func.sleep
        )

        # Restart
        self.actions[keyword.SYSTEM_RESTART] = action.Action(
            keyword.SYSTEM_RESTART,
            "Restarts the computer",
            winsys.load_resource_image("restart.png"),
            sys_func.restart
        )

        # Shutdown
        self.actions[keyword.SYSTEM_SHUTDOWN] = action.Action(
            keyword.SYSTEM_SHUTDOWN,
            "Shuts down the computer",
            winsys.load_resource_image("shutdown.png"),
            sys_func.shutdown
        )
