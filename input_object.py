class InputObject:
    mode = -1
    dataList = []
    def __init__(self,mode,dataList):
        self.mode = mode
        self.dataList = dataList
        # mode 0 - dots
        # mode 1 - funcs
        # datalist - list of data :D
    def setMode(self,mode):
        self.mode = mode

    def setDataList(self, dataList):
        self.dataList = dataList

    def getMode(self):
        return (self.mode)

    def getDataList(self):
        return self.dataList
