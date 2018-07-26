import wpf

from System.Windows.Controls import UserControl

class Ball(UserControl):
    """Ball class"""
    def __init__(self, left, top):
        UserControl.__init__(self)
        wpf.LoadComponent(self, "../Design/Ball.xaml")
        self.Left = left
        self.Top = top
        self.DataContext = self


