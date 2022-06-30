"""mongodb.image.py module"""
import os
import csv
import pymongo
from dotenv import load_dotenv

load_dotenv()

def find_images(client: pymongo.MongoClient, file_name: str):
    """
    Find all the images in DB and write their path in a CSV file.

    Parameters
    ----------
    client : MongoClient
        The pymongo client of MongoDB
    file_name : str
        the name of the CSV file for storing all the images path
    """
    if os.path.exists(file_name):
        os.remove(file_name)

    image_path = os.getenv("IMAGE_PATH")
    data_base = client[os.getenv("SCRAPPER_DB")]
    collection = data_base[os.getenv("IMAGES_COLLECTION")]

    with open(file_name, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        cursor = collection.find({}, {"origin": 1, "path": 1})
        for document in cursor:
            absolute_path = os.path.join(
                image_path, document["origin"], document["path"]
            )
            writer.writerow([absolute_path])  # one line is a list of char
    print(f"Finished loading the images in {file_name}")
