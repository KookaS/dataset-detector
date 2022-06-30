"""main.py module"""
from decorators import shutdown_cloud, timing
from mongodb import connect, find_images
# from data import get_scrapper_loader


@timing
@shutdown_cloud
def main():
    """
    Entry code
    """
    client = connect()
    file_name = "images.csv"
    find_images(client, file_name)
    # dataloader = get_scrapper_loader(file_name)


if __name__ == "__main__":
    main()
