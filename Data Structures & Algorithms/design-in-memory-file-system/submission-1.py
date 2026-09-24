class File:
    def __init__(self):
        self.children = {}
        self.isFile = False
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = File()
        

    def ls(self, path: str) -> List[str]:
        curr = self.root
        result = []
        if path != "/":
            broken_path = path.split("/")
            for i in range(1 , len(broken_path)):
                curr = curr.children[broken_path[i]]
            if curr.isFile:
                result.append(broken_path[-1])
                return result
        return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        curr = self.root
        broken_path = path.split("/")
        for i in range(1 , len(broken_path)):
            if broken_path[i] not in curr.children:
                curr.children[broken_path[i]] = File()
            curr = curr.children[broken_path[i]]
        
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        broken_path = filePath.split("/")
        for i in range(1 , len(broken_path)):
            if broken_path[i] not in curr.children:
                curr.children[broken_path[i]] = File()
            curr = curr.children[broken_path[i]]
        curr.isFile = True 
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        broken_path = filePath.split("/")
        for i in range(1 , len(broken_path)):
            if broken_path[i] not in curr.children:
                curr.children[broken_path[i]] = File()
            curr = curr.children[broken_path[i]]
        return curr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
