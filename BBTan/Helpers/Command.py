from System.Windows.Input import ICommand

class Command(ICommand):
    """Command class; for executing commands"""
    def __init__(self, execute):
        self.execute = execute
    
    def Execute(self, parameter):
        self.execute()
        
    def add_CanExecuteChanged(self, handler):
        pass
    
    def remove_CanExecuteChanged(self, handler):
        pass

    def CanExecute(self, parameter):
        return True

