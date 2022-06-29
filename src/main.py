"""main.py module"""
from decorators import shutdown_cloud, timing

@timing
@shutdown_cloud
def main():
    """
    Entry code
    """


if __name__ == "__main__":
    main()
