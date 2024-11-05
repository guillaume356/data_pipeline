import os
from PIL import Image
from datetime import datetime
from typing import Final


class ImageProcessor:
    def __init__(self, folder: str) -> None:
        self.folder: Final[str] = folder

    def process_folder(self, destination_size: int) -> None:
        dataset_path: Final[str] = os.path.join(os.getcwd(), "datasets")
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)

        unique_id: Final[str] = datetime.now().strftime("%Y%m%d%H%M%S")
        output_folder: Final[str] = os.path.join(dataset_path, unique_id)
        os.makedirs(output_folder)

        for filename in os.listdir(self.folder):
            file_path: str = os.path.join(self.folder, filename)
            if os.path.isfile(file_path) and self.is_image_file(filename):
                try:
                    with Image.open(file_path) as img:
                        print(f"Ouvrir l'image : {filename}")
                        output_path: str = os.path.join(output_folder, filename)
                        self.resize_and_pad_image(img, destination_size, output_path)
                except Exception as e:
                    print(
                        f"Erreur lors de l'ouverture ou du traitement de l'image {filename}: {e}"
                    )

    @staticmethod
    def is_image_file(filename: str) -> bool:
        image_extensions: Final[tuple] = (".png", ".jpg", ".jpeg")
        return filename.lower().endswith(image_extensions)

    @staticmethod
    def resize_and_pad_image(
        img: Image.Image, destination_size: int, output_path: str
    ) -> None:
        width: int = img.width
        height: int = img.height
        aspect_ratio: float = width / height

        if width > height:
            new_height: int = destination_size
            new_width: int = int(destination_size * aspect_ratio)
        else:
            new_width: int = destination_size
            new_height: int = int(destination_size / aspect_ratio)

        img_resized: Image.Image = img.resize(
            (new_width, new_height), Image.Resampling.LANCZOS
        )
        padded_img: Image.Image = Image.new(
            "RGB", (destination_size, destination_size), (114, 114, 144)
        )
        left: int = (destination_size - new_width) // 2
        top: int = (destination_size - new_height) // 2
        padded_img.paste(img_resized, (left, top))

        padded_img.save(output_path)
        print(f"Image sauvegardée : {output_path}")
