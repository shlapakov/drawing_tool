from drawing_tool.drawer import CommandReader, Drawer
if __name__ == '__main__':
    reader = CommandReader()
    path = reader.set_file_path()
    Drawer(reader.commands, path).draw()
