# Keypirinha | A semantic launcher for Windows | http://keypirinha.com

import keypirinha as kp

from . import system_actions
from . import shell_actions
from . import settings_actions


class WinSys(kp.Plugin):
    """
    Provides Windows 10 system functions such as shutdown, reboot, empty recycle bin, and access to "modern" Windows
    shell folders and Windows Settings app
    """

    # Initialize
    def __init__(self):
        super().__init__()

        self._actions = {}

    # Cleanup
    def __del__(self):
        self._cleanup()

    def on_start(self):
        self.dbg('WinSys plugin startup initialized.')
        self._cleanup()
        self._init_system_actions()
        self._init_shell_actions()
        self._init_windows_settings_actions()

    def on_catalog(self):
        catalog = []

        for keyword, kpaction in self._actions.items():
            self.dbg('Creating catalog item for action: ', kpaction.label)
            catalog.append(self.create_item(
                category=kp.ItemCategory.KEYWORD,
                label=kpaction.label,
                short_desc=kpaction.description,
                target=kpaction.label,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.NOARGS,
                icon_handle=kpaction.icon_handle
            ))

        self.set_catalog(catalog)

    def on_suggest(self, user_input, items_chain):
        self.dbg(user_input)

    def on_execute(self, item, action):
        if item and item.category() == kp.ItemCategory.KEYWORD:
            selected_action = self._actions[item.target()]
            self.dbg('Found catalog item for action:', selected_action.label)
            if selected_action:
                selected_action.function()

    def on_activated(self):
        self.dbg('Activated the WinSys plugin.')

    def on_deactivated(self):
        self.dbg('Deactivated the WinSys plugin.')

    def on_events(self, flags):
        if flags & kp.Events.PACKCONFIG:
            self.info("Configuration changed, rebuilding catalog...")
            self.on_catalog()

    def load_resource_image(self, image_name):
        return self.load_icon('res://{package}/icons/{image}'.format(
            package=self.package_full_name(),
            image=image_name)
        )

    # Private functions
    def _init_system_actions(self):
        self._actions.update(system_actions.SystemActions(self).actions)

    def _init_shell_actions(self):
        self._actions.update(shell_actions.ShellActions(self).actions)

    def _init_windows_settings_actions(self):
        self._actions.update(settings_actions.SettingsActions(self).actions)

    def _cleanup(self):
        self.dbg("Cleaning up resources.")

        # Cleanup icons
        for key, kpaction in self._actions.items():
            kpaction.icon_handle.free()
