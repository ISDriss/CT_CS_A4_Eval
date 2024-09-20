from PIL import Image, ImageFilter
import numpy as np

#Empirical testing shows that the optimal threshold value is 128, satisfactory results can still be obtained in the 120-132 range
def generate_rorschach(image_size=(400, 400), noise_intensity=255, threshold=128):
    width, height = image_size

    # Step 1: Generate random noise for the heightmap
    noise = np.random.rand(height, width // 2) * noise_intensity  # Generate noise in full range 0-255
    noise = noise.astype(np.uint8)  # Convert to 8-bit grayscale values

    # Step 2: Convert the noise array to an image
    left_half = Image.fromarray(noise, mode='L')  # 'L' mode is for grayscale

    # Step 3: Apply a Gaussian blur to smooth the noise and create more organic shapes
    blurred_left_half = left_half.filter(ImageFilter.GaussianBlur(radius=10))

    # Step 4: Apply a threshold to turn the heightmap into binary inkblots
    # Rescale the image so that we use the full range from 0 to 255
    rescaled_left_half = blurred_left_half.point(lambda p: p * 255 // noise_intensity)

    # Step 5: Threshold to create binary inkblots
    binary_left_half = rescaled_left_half.point(lambda p: 255 if p > threshold else 0, mode='1')  # Binary image

    # Step 6: Mirror the left half to the right half
    mirrored_half = binary_left_half.transpose(Image.FLIP_LEFT_RIGHT)

    # Step 7: Create the full image by combining both halves
    full_image = Image.new('1', (width, height))  # '1' mode for binary images
    full_image.paste(binary_left_half, (0, 0))  # Paste left side
    full_image.paste(mirrored_half, (width // 2, 0))  # Paste mirrored right side

    # Optional: Convert to RGB for further manipulation, like coloring the inkblots
    full_image_rgb = full_image.convert('RGB')

    # Step 8: Show the generated Rorschach inkblot
    full_image_rgb.show()

    # Optionally save the image as PNG
    full_image_rgb.save("rorschach.png")

# Call the function to generate and display the image
generate_rorschach()

