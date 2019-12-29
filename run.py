from drawing_tool.drawer import CommandReader, Drawer
if __name__ == '__main__':
    path = CommandReader().set_file_path()
    commands = CommandReader().commands
    Drawer(commands, path).draw()
