from abc import ABCMeta, abstractstaticmethod

#Receiver
class paket:
    def diantar(self):
        print("Status : Paket sedang diantar")

    def diterima(self):
        print("Status : Paket sudah diterima")

#ICommand Interface
class ICommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def execute():
        """A Static Interface method"""

#Command diantar
class diantarCommand(ICommand):
    def __init__(self, paket):
        self._paket = paket

    def execute(self):
        self._paket.diantar()

#Command diterima
class diterimaCommand(ICommand):
    def __init__(self, paket):
        self._paket = paket

    def execute(self):
        self._paket.diterima()

#Invoker
class aksi:
    """The inviker class"""
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print("Command tidak ditemukan")

#Client
if __name__ == "__main__":
    #Receiver
    PAKET = paket()

    #commands
    antar = diantarCommand(PAKET)
    terima = diterimaCommand(PAKET)

    #invoker
    AKSI = aksi()

    #Register commands di invoker
    AKSI.register("diantar", antar)
    AKSI.register("diterima", terima)

    AKSI.execute("diantar")
    AKSI.execute("diterima")
    AKSI.execute("diantar")
    AKSI.execute("diterima")
