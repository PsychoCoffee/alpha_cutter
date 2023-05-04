# Alpha Cutter
![](https://github.com/PsychoCoffee/alpha_cutter/blob/main/banner_ac.png)
This is a python script, that can be used for cutting color textures according to the alpha texture.

# How it works
It uses opencv2 to convert both inputted images (alpha and color textures) into arrays, and then cuts them, and saves them as a .png file to save the transparency.
This can be useful for game engines and texturing programs, as you don't need to do this manually with photoshop anymore. 

# How to run
You can run this in Python IDLE or Python 3.10 by just double clicking on it. You might need to run Command Prompt as admin, and then run `pip install opencv-python` and `pip install os` to install opencv2 and be able to run it.

As far as I'm aware, numpy should install alongside with opencv2, but if it doesn't, make sure to do so with `pip install numpy`

# With which file type does it work
Well, to be honest, I'm not sure. As far as I tested, it works with jpeg, png, jpg, tiff, tif and bmp files. If something doesn't work feel free to report an issue on github.

