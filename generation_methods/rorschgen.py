import numpy as np
import matplotlib.pyplot as plt
import random

def generate_rorschach(image_size=(400, 400), blotch_count=10):
    # Create a blank canvas (RGB image)
    width, height = image_size
    canvas = np.zeros((height, width, 3), dtype=np.uint8)

    # Generate random blotches on one half (left side)
    for _ in range(blotch_count):
        # Random size of blotch
        blotch_size = random.randint(20, 100)
        # Random position (only on left half)
        x_center = random.randint(0, width // 2)
        y_center = random.randint(0, height)
        # Random color for the blotch
        color = np.random.randint(0, 255, 3)

        # Draw random circular blotch (using a simple circle approximation)
        for x in range(max(0, x_center - blotch_size), min(width // 2, x_center + blotch_size)):
            for y in range(max(0, y_center - blotch_size), min(height, y_center + blotch_size)):
                if (x - x_center) ** 2 + (y - y_center) ** 2 <= blotch_size ** 2:
                    canvas[y, x] = color
    
    # Mirror the left half to the right half to create symmetry
    left_half = canvas[:, :width // 2]
    canvas[:, width // 2:] = np.fliplr(left_half)

    # Display the generated Rorschach inkblot image
    plt.imshow(canvas)
    plt.axis('off')  # Hide axes
    plt.show()

# Call the function to generate and display the image
generate_rorschach()
