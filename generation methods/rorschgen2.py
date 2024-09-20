from PIL import Image, ImageDraw
import random

def generate_rorschach_image_pillow(image_size=(400, 400), blotch_count=10):
    # Create a blank canvas (RGB image)
    width, height = image_size
    image = Image.new("RGB", (width, height), (255, 255, 255))  # White background
    draw = ImageDraw.Draw(image)

    # Generate random blotches on the left side
    for _ in range(blotch_count):
        # Random size of the blotch
        blotch_size = random.randint(20, 100)
        # Random position (only on the left half)
        x_center = random.randint(0, width // 2)
        y_center = random.randint(0, height)
        # Random color
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Create an ellipse (blotch) on the left half
        x0 = x_center - blotch_size
        y0 = y_center - blotch_size
        x1 = x_center + blotch_size
        y1 = y_center + blotch_size
        draw.ellipse([x0, y0, x1, y1], fill=color)

    # Mirror the left side onto the right side
    left_half = image.crop((0, 0, width // 2, height))
    mirrored_half = left_half.transpose(Image.FLIP_LEFT_RIGHT)
    image.paste(mirrored_half, (width // 2, 0))

    # Show the generated Rorschach image
    image.show()

    # Optionally save the image
    image.save("generated rorschach.png")

# Call the function to generate and display the image
generate_rorschach_image_pillow()
