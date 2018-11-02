#!/bin/bash
# Himanshu Buckchash - 2018-11-02
# Project: https://github.com/hardikvasa/google-images-download

# to download over 100 images; chromedriver has to be used
googleimagesdownload --keywords "tomato" --limit 200 --chromedriver "./chromedriver"
# googleimagesdownload --keywords "tomato" --offset 210 --limit 310 --chromedriver "./chromedriver"
    # above command will download 100 images
    # the size argument can be used to specify size of the images to be downloaded
