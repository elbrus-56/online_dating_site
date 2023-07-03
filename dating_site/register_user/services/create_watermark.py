from PIL import Image
from config.settings import MEDIA_ROOT


class Watermark:

    @staticmethod
    def create_watermark(input_image_path, output_image_path) -> None:
        """
        :param input_image_path: путь к изображению без watermark
        :param output_image_path: полный путь для сохранения готового
        изображения
        :return: None
        """

        base_image = Image.open(input_image_path)
        watermark = Image.open(MEDIA_ROOT / 'images/watermark.png')

        width, height = base_image.size

        im = Image.new('RGB', (width, height), (0, 0, 0, 0))
        im.paste(base_image, (0, 0))
        im.paste(watermark, (0, 0), mask=watermark)
        im.save(output_image_path)
