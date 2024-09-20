from PIL import Image, ImageFilter
import numpy as np

def generate_rorschach(image_size=(400, 400), noise_intensity=255, threshold=128):
    width, height = image_size

    # Step 1: Generate random noise for the heightmap
    noise = np.random.rand(height, width // 2) * noise_intensity  # Generate noise in full range 0-255
    noise = noise.astype(np.uint8)  # Convert to 8-bit grayscale values

    # Step 2: Convert the noise array to an image
    left_half = Image.fromarray(noise, mode='L')  # 'L' mode is for grayscale

    # Step 3: Apply a Gaussian blur to smooth the noise and create more organic shapes
    blurred_left_half = left_half.filter(ImageFilter.GaussianBlur(radius=10))

    # Step 4: Rescale the image so that we use the full range from 0 to 255
    rescaled_left_half = blurred_left_half.point(lambda p: p * 255 // noise_intensity)

    # Step 5: Threshold to create binary inkblots
    binary_left_half = rescaled_left_half.point(lambda p: 255 if p > threshold else 0, mode='1')  # Binary image

    # Step 6: Mirror the left half to the right half
    mirrored_half = binary_left_half.transpose(Image.FLIP_LEFT_RIGHT)

    # Step 7: Create the full image by combining both halves
    full_image = Image.new('1', (width, height))  # '1' mode for binary images
    full_image.paste(binary_left_half, (0, 0))  # Paste left side
    full_image.paste(mirrored_half, (width // 2, 0))  # Paste mirrored right side

    # Convert the binary image back to grayscale to match with original heightmap for color mapping
    full_image_grayscale = full_image.convert('L')

    # Step 8: Apply random color gradient using heightmap information
    full_image_colored = Image.new('RGB', (width, height))
    pixels = full_image_colored.load()  # Load pixel data for manipulation

    # Generate a random gradient start and end colors (RGB)
    start_color = np.random.randint(0, 256, 3)  # Random RGB start color
    end_color = np.random.randint(0, 256, 3)  # Random RGB end color

    for y in range(height):
        for x in range(width):
            if full_image_grayscale.getpixel((x, y)) > threshold:
                # Calculate gradient based on heightmap value
                t = full_image_grayscale.getpixel((x, y)) / 255  # Normalized grayscale value
                r = int((1 - t) * start_color[0] + t * end_color[0])
                g = int((1 - t) * start_color[1] + t * end_color[1])
                b = int((1 - t) * start_color[2] + t * end_color[2])
                pixels[x, y] = (r, g, b)
            else:
                pixels[x, y] = (0, 0, 0)  # White background

    # Save the colored image
    full_image_colored.save("rorschach.png")

# Call the function to generate the Rorschach image with gradient
generate_rorschach()
