import os

# class Command(object):
#     def __init__(self, autoSplit):
#         self.AutoSplit = autoSplit

def executeCommand(AutoSplit, commands, format = "utf-8"):
    if (commands == b""):
        return
    for command in commands.decode(format).splitlines():
        strCommand = command.split(' ')
        if (strCommand[0] == "setImage"):
            AutoSplit.setSplit(int(strCommand[1]))
        # elif (strCommand[0] == "reset"):
        #     self.AutoSplit.reset()
        elif (strCommand[0] == "setSettings"):
            os.chdir(strCommand[1])
            AutoSplit.loadSettings()
            