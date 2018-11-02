#!/bin/bash
# Himanshu Buckchash - 2018-11-02
# Project: https://github.com/hardikvasa/google-images-download

# to download over 100 images; chromedriver has to be used

source activate e1_dl_py3.5     # switch to virtual environment
googleimagesdownload --keywords "tomato" --limit 10 --chromedriver "./chromedriver"
# googleimagesdownload --keywords "tomato" --offset 210 --limit 310 --chromedriver "./chromedriver"
    # above command will download 100 images
    # the size argument can be used to specify size of the images to be downloaded
source deactivate