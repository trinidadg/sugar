class Navigable:
    def __init__(self):
        self.nav_queue = []
        self.nav_pos = 0

    def start_navigation(self):
        self.nav_pos = -1
        return self.navigation_right()

    def navigate_from_end(self):
        self.nav_pos = len(self.nav_queue)
        return self.navigation_left()

    def navigate(self):
        size = len(self.nav_queue) - 1
        if size == -1:
            return -2
        button = self.nav_queue[self.nav_pos]
        if button.get_palette() is None:
            button.create_palette()
        button.get_palette().popup()
        if size == 0:
            return 2
        if self.nav_pos == 0:
            return -1
        if size > self.nav_pos:
            return 0
        if size == self.nav_pos:
            return 1

    def navigation_right(self):
        self.nav_pos += 1
        return self.navigate()

    def navigation_left(self):
        self.nav_pos -= 1
        return self.navigate()

    def enter_key_pressed(self):
        button = self.nav_queue[self.nav_pos]
        button.get_child().clicked()
