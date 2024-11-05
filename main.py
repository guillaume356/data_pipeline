from src.image_processor import ImageProcessor
import os


def main():

    # Dossier contenant les images à traiter
    input_folder = f"{os.getcwd()}/input_images"
    destination_size = 6400

    # Créer une instance de ImageProcessor et exécuter le traitement
    processor = ImageProcessor(input_folder)
    processor.process_folder(destination_size)


if __name__ == "__main__":
    main()
