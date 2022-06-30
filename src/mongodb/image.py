import pymongo
import os
from dotenv import load_dotenv
import csv

load_dotenv()

def find_images(client: pymongo.MongoClient, file_name: str):
    """
    Find all the images in DB and write their path in a CSV file
    """
    if os.path.exists(file_name):
        os.remove(file_name)

    image_path = os.getenv("IMAGE_PATH")
    db = client[os.getenv("SCRAPPER_DB")]
    collection = db[os.getenv("IMAGES_COLLECTION")]

    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        cursor = collection.find({}, {"origin":1, "path":1})
        for document in cursor:
            absolute_path = os.path.join(image_path, document["origin"], document["path"])
            writer.writerow([absolute_path]) # one line is a list of char
        