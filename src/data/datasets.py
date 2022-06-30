"""data.datasets.py module"""
import random
from torch.utils.data import Dataset
from PIL import Image
from torchvision.transforms import Compose


class Scrapper(Dataset):
    """Dataset class for the Scrapper dataset."""

    def __init__(self, file_name: str, transform: Compose, mode: str, seed: int):
        """Initialize and preprocess the Scrapper dataset."""

        self.file_name = file_name
        self.transform = transform
        self.mode = mode
        self.train_dataset = []
        self.val_dataset = []
        self.test_dataset = []
        self.preprocess(seed)

        if mode == "train":
            self.num_images = len(self.train_dataset)
        elif mode == "val":
            self.num_images = len(self.val_dataset)
        else:
            self.num_images = len(self.test_dataset)

    def preprocess(self, seed: int):
        """Preprocess the Scrapper attribute file."""
        with open(self.file_name, "r", encoding='utf-8') as file:
            lines = [line.rstrip() for line in file]
            random.seed(seed)
            random.shuffle(lines)
            length = len(lines)
            test_ratio = 0.1
            val_ratio = 0.1
            for i, line in enumerate(lines):
                if (i + 1) < length*test_ratio:
                    self.test_dataset.append(line)
                elif length*test_ratio < (i + 1) < length*(test_ratio+val_ratio):
                    self.val_dataset.append(line)
                else:
                    self.train_dataset.append(line)
            print("Finished preprocessing the Scrapper dataset...")

    def __getitem__(self, index):
        """Return one image and its corresponding attribute label."""
        match self.mode:
            case "train":
                dataset = self.train_dataset
            case "test":
                dataset = self.test_dataset
            case "val":
                dataset = self.val_dataset
        filename = dataset[index]
        image = Image.open(filename)
        return self.transform(image)

    def __len__(self):
        """Return the number of images."""
        return self.num_images
