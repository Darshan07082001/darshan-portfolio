from PIL import Image, ImageDraw, ImageFont
import os

# Create a professional placeholder profile image
def create_placeholder_image():
    # Create a 400x400 image with a professional background
    size = (400, 400)
    
    # Create gradient background
    img = Image.new('RGB', size, color='#2b6cb0')
    draw = ImageDraw.Draw(img)
    
    # Create a circular background
    center = (200, 200)
    radius = 180
    
    # Draw circle background
    draw.ellipse([center[0]-radius, center[1]-radius, 
                  center[0]+radius, center[1]+radius], 
                 fill='#3498db', outline='#2c3e50', width=8)
    
    # Add initials "DN"
    try:
        # Try to use a system font
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Draw initials
    text = "DN"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = center[0] - text_width // 2
    text_y = center[1] - text_height // 2 - 10
    
    draw.text((text_x, text_y), text, fill='white', font=font)
    
    # Add a subtle border effect
    draw.ellipse([center[0]-radius-5, center[1]-radius-5, 
                  center[0]+radius+5, center[1]+radius+5], 
                 fill=None, outline='#1a365d', width=3)
    
    # Save the image
    img.save('profile.jpg', 'JPEG', quality=95)
    print("Professional placeholder profile image created: profile.jpg")

if __name__ == "__main__":
    create_placeholder_image()