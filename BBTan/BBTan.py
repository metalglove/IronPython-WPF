import wpf

from GameFieldViewModel import GameFieldViewModel
from System.Windows import Application, Window

class WindowBinder(Window):
    def __init__(self, filename, context):
        wpf.LoadComponent(self, filename)
        DataContext = context
        
class BBTan(Application):
    def OnStartup(self, args):
        Application.OnStartup(self, args)
        vm = GameFieldViewModel()
        window = WindowBinder("../Design/GameField.xaml", vm)
        window.Show()
        
if __name__ == '__main__':
    BBTan().Run()
    wind = Window()
    
