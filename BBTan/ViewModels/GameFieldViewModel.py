from Helpers.ViewModelBase import ViewModelBase
from Helpers.Command import Command

class GameFieldViewModel(ViewModelBase):
    """description of class"""
    def __init__(self):
        ViewModelBase.__init__(self)
        self.FirstName = "Joe"
        self.Surname = "Smith"
        self.ChangeCommand = Command(self.change)
    
    def change(self):
        self.FirstName = "Dave"
        self.Surname = "Brown"
        self.RaisePropertyChanged("FirstName")
        self.RaisePropertyChanged("Surname")

