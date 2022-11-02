# lit_dataloader.py ---
#
# Filename: lit_dataloader.py
# Author: Fred Qi
# Created: 2022-02-11 16:51:25(+0800)
#
# Last-Updated: 2022-02-12 16:59:07(+0800) [by Fred Qi]
#     Update #: 57
# 

# Commentary:
#
#
# 

# Change Log:
#
#
#
import os
from torch.utils.data import DataLoader
from torch.utils.data import random_split
from torchvision import transforms
from torchvision.datasets import MNIST
from pytorch_lightning.core.datamodule import LightningDataModule
from pytorch_lightning.utilities.cli import DATAMODULE_REGISTRY

       
@DATAMODULE_REGISTRY
class MNISTDataModule(LightningDataModule):
    def __init__(self, batch_size=64):
        super().__init__()
        self.data_path = os.path.join(os.getcwd(), 'data')
        self.batch_size = batch_size

    def prepare_data(self):
        # download only
        MNIST(self.data_path, train=True, download=True, transform=transforms.ToTensor())
        MNIST(self.data_path, train=False, download=True, transform=transforms.ToTensor())

    def setup(self, stage: str = None):
        # transform
        transform = transforms.Compose([transforms.ToTensor()])
        mnist_train = MNIST(self.data_path, train=True, download=False, transform=transform)
        mnist_test = MNIST(self.data_path, train=False, download=False, transform=transform)

        # train/val split
        mnist_train, mnist_val = random_split(mnist_train, [55000, 5000])

        # assign to use in dataloaders
        self.train_dataset = mnist_train
        self.val_dataset = mnist_val
        self.test_dataset = mnist_test

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size)

    
# 
# lit_dataloader.py ends here
