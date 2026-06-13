README.md
# 📸 Photos Slideshow Album Application

A simple and user-friendly desktop slideshow application built with Python, Tkinter, and Pillow (PIL). This application allows users to display a collection of images in an automatic slideshow format with a single button click.

## ✨ Features

- Display multiple images in a slideshow
- Simple graphical user interface using Tkinter
- Automatic image transitions every 2 seconds
- Image resizing for consistent display
- Lightweight and easy to customize

## 🛠️ Technologies Used

- Python
- Tkinter (GUI)
- Pillow (PIL)

## 📂 Project Structure


Photos-Slideshow-Album/
│
├── slideshow.py
├── images/
│ ├── image1.jpg
│ ├── image2.jpg
│ ├── image3.jpg
│ └── ...
└── README.md


## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/photos-slideshow-album.git
2. Navigate to the Project Folder
cd photos-slideshow-album
3. Install Required Package
pip install pillow
▶️ Running the Application
python slideshow.py
⚙️ Configuration

Edit the image_paths list inside the Python file and add the paths of your own images:

image_paths = [
    r'path/to/image1.jpg',
    r'path/to/image2.jpg',
    r'path/to/image3.jpg'
]

You can also adjust:

Image Size
image_size = (700, 700)
Slideshow Duration
time.sleep(2)

Change the value to display images for a longer or shorter duration.

📷 How It Works
Images are loaded from local storage.
Each image is resized to a fixed dimension.
Images are converted into Tkinter-compatible formats.
Clicking the Play Slideshow button starts the slideshow.
Images automatically switch every 2 seconds.
🔮 Future Improvements
Previous/Next buttons
Pause and Resume functionality
Full-screen slideshow mode
Dynamic image folder selection
Transition effects (fade, zoom, slide)
Background music support
👨‍💻 Author

Created as a Python GUI project using Tkinter and Pillow.

📜 License

This project is open-source and available under the MIT License.


### GitHub Repository Description (Short)

> A Python Tkinter-based photo slideshow application that displays local images in an automated album format with smooth image transitions using Pillow (PIL). 📸✨

### GitHub Topics/Tags


python
tkinter
pillow
gui
slideshow
photo-viewer
desktop-application
image-processing
python-project
album-viewer


One improvement I'd recommend before uploading: replace `time.sleep(2)` with Tkinter's `after()` method. It prevents the GUI from freezing during the slideshow and makes the application feel much smoother.
