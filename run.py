from drawing_tool.drawer import CommandReader, Drawer
if __name__ == '__main__':
    commands = CommandReader().commands
    Drawer(commands).draw()
