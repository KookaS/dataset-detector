"""data.dataloaders.py module"""
from torchvision import transforms as T
from torch.utils import data
from .datasets import Scrapper


# pylint: disable=too-many-arguments
def get_scrapper_loader(
    file_name,
    seed=777,
    crop_size=178,
    image_size=128,
    batch_size=16,
    mode="train",
    num_workers=1,
):
    """
    Build and return a data loader.

    Parameters
    ----------
    file_name : str
        The file name where all images path are stored
    seed : int
        The seed to control the results
    crop_size : int
        The CenterCrop size
    image_size : int
        the Resize size
    batch_size : int
        The amount of images per batch process
    mode : str
        The mode of the Dataloader, either `train`, `val` or `test`
    num_worker : int
        how many subprocesses to use for data loading.
        `0` means that the data will be loaded in the main process.
        (default: `0`)

    Returns
    -------
    data_loader
        Pytorch Dataloader for the Scrapper Dataset
    """

    transform = []
    if mode == "train":
        transform.append(T.RandomHorizontalFlip())
    transform.append(T.CenterCrop(crop_size))
    transform.append(T.Resize(image_size))
    transform.append(T.ToTensor())
    transform.append(T.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)))
    transform = T.Compose(transform)
    dataset = Scrapper(file_name, transform, mode, seed)

    data_loader = data.DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=(mode == "train"),
        num_workers=num_workers,
    )
    return data_loader
