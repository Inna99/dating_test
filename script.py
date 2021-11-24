from PIL import Image


def watermark_with_photo(
    input_image_path, output_image_path, watermark_image_path, position
):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # add watermark to image
    base_image.paste(watermark, position)
    base_image.save(output_image_path)


# if __name__ == '__main__':
#     img = 'kitty.jpg'
#     watermark_with_photo(img, 'lighthouse_watermarked2.jpg',
#                          'watermark.jpg', position=(0, 0))
