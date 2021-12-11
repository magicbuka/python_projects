class Editor:
    str = ''
    history = list()
    reset = False
    count = -1
    last_index = 0
    undo_lst = list()
    redo_unable = False

    def __init__(self, command):
        self.command = command
    
    def GetIndex(self):
        if len(self.command) > 0:
            return int(self.command[0])

    def GetParam(self):
        if len(self.command) >= 3:
            return self.command[2:]
        else:
            return False

    def AddElem(self, parameter):
        Editor.count = -1
        old_str = Editor.str
        Editor.str += parameter
        if Editor.last_index == 4:
            if not Editor.reset:
                Editor.reset = True
                Editor.undo_lst = list()
                Editor.undo_lst.append(old_str)
                Editor.undo_lst.append(Editor.str)
        elif Editor.reset:
            Editor.undo_lst.append(Editor.str)
    
    def DelElem(self, num):
        Editor.count = -1
        Editor.old_str = Editor.str
        if num > len(Editor.str):
            Editor.str = ''
        else:
            Editor.str = Editor.str[0:len(Editor.str)-num]
        
        if Editor.last_index == 4:
            if not Editor.reset:
                Editor.reset = True
                Editor.undo_lst.append(Editor.old_str)
                Editor.undo_lst.append(Editor.str)
        elif Editor.reset:
            Editor.undo_lst.append(Editor.str)

    def ReturnElem(self, i):
        if i > len(Editor.str)-1 or i < 0:
            return ''
        return Editor.str[i]

    def Undo(self):
        Editor.before_redo = Editor.str
        Editor.count -= 1
        if Editor.reset:
            Editor.history = Editor.undo_lst[:]
            Editor.reset = False
        
        if Editor.count < -len(Editor.history):
            Editor.count = -len(Editor.history)
            return Editor.history[-len(Editor.history)]
        return Editor.history[Editor.count]

    def Redo(self):
        if Editor.last_index == 4:
            Editor.redo_unable = True
        Editor.count += 1
        
        if Editor.count > -1:
            Editor.count = -1
        return Editor.history[Editor.count]
    
    def Corrector(self):
        index = self.GetIndex()
        parameter = self.GetParam()
        if index == 1 and parameter:
            self.AddElem(parameter)
            Editor.history.append(Editor.str)
        elif index == 2 and parameter:
            if parameter.isnumeric():
                self.DelElem(int(parameter))
                Editor.history.append(Editor.str)
        elif index == 3 and parameter:
            if parameter.isnumeric():
                res = self.ReturnElem(int(parameter))
                Editor.last_index = index
                return res
        elif index == 4 and not parameter:
            Editor.str = self.Undo()
        elif index == 5 and not parameter:
            if Editor.last_index == 4 or Editor.redo_unable:
                Editor.str = self.Redo()
        Editor.last_index = index
        return Editor.str

def BastShoe(command):
    action = Editor(command)
    return action.Corrector()
