# printASCII

A Python script that turns any photo into ASCII art.

## Getting Started

### Prerequisites

This script was written using Python 3.7 and uses the Pillow Library: https://python-pillow.org/#. 

Using a virtual envrionemnt is advised. If you're not familiar with virtual envrionments, here's the docs (Python):
https://docs.python.org/3/library/venv.html

Make sure you have python3 and pip installed. If not, install them before continuing (duh.) 
Here's the site for python > https://www.python.org/downloads/

### Installing

These steps are intended to be done after creating a virtual envrionment and activating it in your terminal

Install the required libraries using requirements.txt and pip
```
$pip install -r requirements.txt
```
And you're ready to go!
I've included some sample images in /res and the outputs in /output
Any images you want to make ASCII art out of must go in the /res folder

Demo:

This snippet shows an example of how to use the script to generate ASCII art

```
$python value-chart.png 1
```
The script takes command-line arguments:
The first one being the name of the file (with extension) is the first 
and the second one being the scale factor, which is how much you would like the image to be scaled. 
The second value is optional. Omitting it will cause the script to take the default value of 1 (the image is not scaled)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Image credits:

awwww-it's-so-cute.jpg : Photo by Tranmautritam from Pexels (original name: Gray and White Kitten on White Bed)
dignified-and-mad-cat.jpg : Photo by Pixabay from Pexels (orignal name : Short-fur Black, Orange, and Gray Cat)
pillow-logo.jpeg : https://github.com/python-pillow/pillow-logo (edited)
python-logo.jpeg : https://www.python.org/community/logos/ (edited)
value-chart.png: me. i is make it.
