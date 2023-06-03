# Alpha Cutter
![](https://github.com/PsychoCoffee/alpha_cutter/blob/main/banner_ac.png)
This is a python script, that can be used for cutting color textures according to the alpha texture.

# How it works
It uses opencv2 to convert both inputted images (alpha and color textures) into arrays, and then cuts them, and saves them as a .png file to save the transparency.
![](https://github.com/PsychoCoffee/alpha_cutter/blob/main/result_white.png)
This can be useful for game engines and texturing programs, as you don't need to do this manually with photoshop anymore. 

# How to run
You can run this in Python IDLE or Python 3.10 by just double clicking on it. You might need to run Command Prompt as admin, and then run `pip install opencv-python` and `pip install os` to install opencv2 and be able to run it.

As far as I'm aware, numpy should install alongside with opencv2, but if it doesn't, make sure to do so with `pip install numpy`

# With which file type does it work
Well, to be honest, I'm not sure. As far as I tested, it works with jpeg, png, jpg, tiff, tif and bmp files. If something doesn't work feel free to report an issue on github.

# License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
