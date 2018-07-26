import random

from Helpers.ViewModelBase import ViewModelBase
from Helpers.Command import Command
from Ball import Ball
from Shooter import Shooter
from System.Collections.ObjectModel import *
from System.Windows.Controls import UserControl, Image, Canvas
from System import Uri
from System.Windows.Media.Imaging import BitmapImage

class GameFieldViewModel(ViewModelBase):
    """GameFieldViewModel"""
    def __init__(self):
        ViewModelBase.__init__(self)
        self.Items = ObservableCollection[UserControl]()
        self.CreateShooter()
        #[self.CreateBall(random.randint(0, 675), random.randint(0, 400)) for _ in range(10)]
        self.Header = "BBTan 1.0"
        self.ChangeCommand = Command(self.Change)
        self.ShootCommand = Command(self.ShootBall)
    
    def Change(self):
        self.ShooterRail = self.Shooter.Left = random.randint(0, 675)
        self.Header = "BBTan " + str(self.ShooterRail)
        Canvas.SetLeft(self.Shooter, self.ShooterRail)
        self.RaisePropertyChanged("Header")

    def CreateBall(self, left, top):
        self.Items.Add(Ball(left, top))

    def CreateShooter(self):
        self.ShooterRail = 400
        self.Shooter = Shooter(self.ShooterRail, 400)
        self.Items.Add(self.Shooter)

    def ShootBall(self):
        self.CreateBall(self.Shooter.Left + 20, self.Shooter.Top - 10)

