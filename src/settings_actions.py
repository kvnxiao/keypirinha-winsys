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
            "Opens the system settings panel",
            winsys.load_resource_image("settings_system.png"),
            ms_settings_func.open_settings_display
        )

        # Open System - Display settings panel
        self.actions[keyword.MS_SYSTEM_SETTINGS_DISPLAY] = action.Action(
            keyword.MS_SYSTEM_SETTINGS_DISPLAY,
            "Opens the display settings panel",
            winsys.load_resource_image("settings_display.png"),
            ms_settings_func.open_settings_display
        )

        # Open System - Notification settings panel
        self.actions[keyword.MS_SYSTEM_SETTINGS_NOTIFICATIONS] = action.Action(
            keyword.MS_SYSTEM_SETTINGS_NOTIFICATIONS,
            "Opens the notification & actions panel",
            winsys.load_resource_image("settings_notifications.png"),
            ms_settings_func.open_settings_notification
        )

        # Open System - Battery settings panel
        self.actions[keyword.MS_SYSTEM_SETTINGS_BATTERY] = action.Action(
            keyword.MS_SYSTEM_SETTINGS_BATTERY,
            "Opens the battery settings panel",
            winsys.load_resource_image("settings_battery.png"),
            ms_settings_func.open_settings_battery
        )

        # Open Devices - Bluetooth panel
        self.actions[keyword.MS_DEVICE_SETTINGS_BLUETOOTH] = action.Action(
            keyword.MS_DEVICE_SETTINGS_BLUETOOTH,
            "Opens the Bluetooth & other devices panel",
            winsys.load_resource_image("settings_bluetooth.png"),
            ms_settings_func.open_settings_bluetooth
        )

        # Open Devices - Printers & Scanners panel
        self.actions[keyword.MS_DEVICE_SETTINGS_PRINTERS] = action.Action(
            keyword.MS_DEVICE_SETTINGS_PRINTERS,
            "Opens the printers & scanners panel",
            winsys.load_resource_image("settings_printer.png"),
            ms_settings_func.open_settings_printer
        )

        # Open Time & Language - Time settings panel
        self.actions[keyword.MS_TIME_SETTINGS_TIME] = action.Action(
            keyword.MS_TIME_SETTINGS_TIME,
            "Opens the date & time panel",
            winsys.load_resource_image("settings_time.png"),
            ms_settings_func.open_settings_time
        )

        # Open Time & Language - Region & Language panel
        self.actions[keyword.MS_TIME_SETTINGS_REGION] = action.Action(
            keyword.MS_TIME_SETTINGS_REGION,
            "Opens the region & language panel",
            winsys.load_resource_image("settings_language.png"),
            ms_settings_func.open_settings_region
        )
