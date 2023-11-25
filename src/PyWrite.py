class File:
    def __init__(self, file_name, mode=None, encoding=None):
        if file_name == None:
            print("The file name you inputted does not exist")
            return

        if mode == None:
            mode = "t"

        if encoding == None:
            encoding = "utf8"
            if mode == "b":
                encoding = None

        self.file_name = str(file_name)
        self.mode = mode
        self.encoding = encoding

        try:
            f = open(file_name, "x")
            f.close()
        except:
            pass

    def write(self, string):
        if string == None:
            print("The string you inputted does not exist")
            return False

        if self.encoding != "b":
            string = str(string)

        if self.file_name == None:
            print("The file name you inputted still does not exist.")
            return False

        try:
            with open(self.file_name, f"w{self.mode}", encoding=self.encoding) as f:
                string = str(string)
                f.write(string)
                f.close()
        except Exception as e:
            print(f"pyWriter ran into a python error: {e}")
            return False

        return True

    def add(self, string):
        if string == None:
            print("The string you inputted does not exist")
            return False
        if self.encoding != "b":
            string = str(string)

        if self.file_name == None:
            print("The file name you inputted still does not exist.")
            return False

        try:
            with open(self.file_name, f"a{self.mode}", encoding=self.encoding) as f:
                f.write(string)
                f.close()
        except Exception as e:
            print(f"pyWriter ran into a python error: {e}")
            return e

        return True

    def read(self):
        if self.file_name == None:
            print("The file name you inputted still does not exist.")
            return False

        try:
            with open(self.file_name, f"r{self.mode}", encoding=self.encoding) as f:
                read = f.read()
                f.close()
                return read
        except Exception as e:
            print(f"pyWriter ran into a python error: {e}")
            return False
