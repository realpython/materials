#! /usr/bin/env sh

center=0   # Start position of the center of the first image.
             # This can be ANYTHING, as only relative changes are important.

  for image in ./images/*
  do

    # Add 70 to the previous images relative offset to add to each image
    #
    center=`convert xc: -format "%[fx: $center +10 ]" info:`

    # read image, add fluff, and using centered padding/trim locate the
    # center of the image at the next location (relative to the last).
    #
    convert -size 800x800 "$image" -thumbnail 800x800 \
            -set caption '%t' -bordercolor black -background black \
            -pointsize 12  -density 96x96  +polaroid  -resize 200% \
            -gravity center -background None -extent 100x100 -trim \
            -repage +${center}+0\!    MIFF:-

  done |
    # read pipeline of positioned images, and merge together
    convert -background white   MIFF:-  -layers merge +repage \
            -bordercolor black -border 1x1 assortment_team.jpg
