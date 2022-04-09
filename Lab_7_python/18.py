files = {}


def add_directory(name):
    directories = name.split("/")
    while len(directories) != 1:
        if directories[0] in list(files.keys()):
            files[directories[0]].append(directories[1])
        else:
            files[directories[0]] = [directories[1]]
        directories.pop(0)
    files[directories[0]] = []


def print_directory(name):
    print(files[name])


class System:
    pass


class File:
    file_content = {}

    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.add_file_content(content)

    def add_file_content(self, content):
        if self.name in list(self.file_content.keys()):
            self.file_content[self.name] += content
        else:
            path = self.name.split("/")
            files[path[-2]].append(path[-1])
            self.file_content[self.name] = content

    def print_file_content(self):
        print(self.file_content[self.name])


sys = System()
add_directory("abc/aa")
file1 = File("abc/file.txt", "error")
file1.print_file_content()
