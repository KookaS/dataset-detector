"""main.py module"""
from decorators import shutdown_cloud, timing
import mongodb

@timing
@shutdown_cloud
def main():
    """
    Entry code
    """
    client = mongodb.connect()
    file_name = 'images.csv'
    mongodb.find_images(client, file_name)


if __name__ == "__main__":
    main()
