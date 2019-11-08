import os
import threading
import time

class Command(object):

    def __init__(self, autoSplit):
        self.AutoSplit = autoSplit
        self.remainingCommands = []

    def executeCommand(self, commands, format = "utf-8"):
        if (commands != b""):
            self.remainingCommands += commands.decode(format).splitlines()
        while (len(self.remainingCommands) > 0):
            command = self.remainingCommands.pop(0)
            strCommand = command.split(' ')
            if (strCommand[0] == "setImage"):
                self.AutoSplit.setSplit(int(strCommand[1]))
            elif (strCommand[0] == "start"):
                # I can't just call startAutoSplitter, else the AutoSplitter will start inside this method, and block the command object.
                thread1 = threading.Thread(target = self.AutoSplit.startAutoSplitter)
                thread1.start()
                thread1.join()
                return
            elif (strCommand[0] == "reset"):
                self.AutoSplit.startReset()
            elif (strCommand[0] == "setSettings"):
                os.chdir(strCommand[1])
                self.AutoSplit.loadSettings()