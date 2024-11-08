from src.image_processor import ImageProcessor
import os


def main():
    """
    main
    """
    input_folder = f"{os.getcwd()}/input_images"
    destination_size = 640

    processor = ImageProcessor(input_folder)
    processor.process_folder(destination_size)


if __name__ == "__main__":
    main()
