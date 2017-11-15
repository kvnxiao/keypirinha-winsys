class Action:
    label = None
    description = None
    icon_handle = None
    function = None

    def __init__(self, label, description, icon_handle, action_func):
        self.label = label
        self.description = description
        self.icon_handle = icon_handle
        self.function = action_func


class KPActions:
    actions = {}

