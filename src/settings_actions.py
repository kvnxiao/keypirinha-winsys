from . import action
from . import keyword
from .lib import win as ms_settings_func


class SettingsActions(action.KPActions):
    def __init__(self, winsys):
        # Open Settings
        self.actions[keyword.MS_SETTINGS_OPEN_SETTINGS] = action.Action(
            keyword.MS_SETTINGS_OPEN_SETTINGS,
            "Opens the Settings application",
            winsys.load_resource_image("settings.png"),
            ms_settings_func.open_settings
        )

        # Open System Settings panel
        self.actions[keyword.MS_SETTINGS_SYSTEM] = action.Action(
            keyword.MS_SETTINGS_SYSTEM,
            "Opens the System settings panel",
            winsys.load_resource_image("settings_system.png"),
            ms_settings_func.open_settings_display
        )

        # Open System - Display settings panel
        self.actions[keyword.MS_SYSTEM_SETTINGS_DISPLAY] = action.Action(
            keyword.MS_SYSTEM_SETTINGS_DISPLAY,
            "Opens the Display settings panel",
            winsys.load_resource_image("settings_display.png"),
            ms_settings_func.open_settings_display
        )

        # Open System - Notification settings panel
        self.actions[keyword.MS_SYSTEM_SETTINGS_NOTIFICATIONS] = action.Action(
            keyword.MS_SYSTEM_SETTINGS_NOTIFICATIONS,
            "Opens the Notification & Actions panel",
            winsys.load_resource_image("settings_notifications.png"),
            ms_settings_func.open_settings_notification
        )

        # Open System - Battery settings panel
        self.actions[keyword.MS_SYSTEM_SETTINGS_BATTERY] = action.Action(
            keyword.MS_SYSTEM_SETTINGS_BATTERY,
            "Opens the Battery settings panel",
            winsys.load_resource_image("settings_battery.png"),
            ms_settings_func.open_settings_battery
        )
