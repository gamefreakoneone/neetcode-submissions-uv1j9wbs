class File:
    def __init__(self):
        self.isFile = False
        self.files = {}
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = File()

    def ls(self, filePath: str) -> List[str]:
        curr = self.root
        files = []
        if filePath != "/":
            path = filePath.split("/")
            for i in range(1, len(path)):
                curr = curr.files[path[i]]
            if curr.isFile:
                files.append(path[-1])
                return files
        result = sorted(curr.files.keys())
        return result

    def mkdir(self, filePath: str) -> None:
        curr = self.root
        path = filePath.split("/")
        for i in range( 1 , len(path) ):
            if path[i] not in curr.files:
                curr.files[path[i]] = File()
            curr = curr.files[path[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        path = filePath.split("/")
        for i in range(1, len(path)-1):
            curr = curr.files[path[i]]
        if path[-1] not in curr.files:
            curr.files[path[-1]] = File()
        curr.files[path[-1]].content += content
        curr.files[path[-1]].isFile = True

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        path = filePath.split("/")
        for i in range(1, len(path)-1): # We are stopping at the parent
            curr = curr.files[path[i]]
        return curr.files[path[-1]].content



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
