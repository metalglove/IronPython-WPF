import wpf

from System.Windows.Controls import UserControl

class Shooter(UserControl):
    """Shooter class"""
    def __init__(self, left, top):
        UserControl.__init__(self)
        wpf.LoadComponent(self, "../Design/Shooter.xaml")
        self.Left = left
        self.Top = top
        self.DataContext = self


