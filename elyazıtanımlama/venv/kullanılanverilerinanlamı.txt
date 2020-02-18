Data description
================

Images
  Directory with the images 

Images/Lines 
  Directory with the line images. These line images are in grayscale.
  These images were manually annotated.

  Line name convention:

  We follow this name convention. For example, consider this name:
  072_094_004_02_05.png

  072_094_004: page file name according to UCL BENTHAM PROJECT    
  02: region identifier
  05: line identifier 
 
  The line identifiers in the PAGE xml files are not necessarily in
  correspondence with the file names in the Images/Lines directory.
  That means, for example, that file 072_094_004_02_05.png could not
  be (geometrically speaking) line 05 of region 02.

  Therefore, if you use your own methods for line extraction then you
  should also extract the associated transcript from the PAGE
  file. The same comments are applied to regions identifiers. This is
  because the lines in the PAGE xml files are not sorted according to
  their geometric position in the image. We extracted the lines
  geometrically following these steps:

  The idea for sorting the region and lines is the classical top-down,
  left-to-right reading order algorithm.
 
  1. Ordering is performed at two levels: the lines within the text
     region order, the text region order. (bottom up).

  2. For each text line, the average height of the polygon that
     contains it was calculated. The y coordinate was added and
     divided by the number of points.

  3. For each individual text region, the text lines were according to the
     average height calculated in step 2. (XML hierarchy gives you the
     text line-text region hierarchy).
 
  4. For each text region, its height was computed as the average height
     of its highest text line (calculated in step 3).
 
  5. Sort the text regions by the height calculated in step 4.
 
  6. For each text region (by order, higher Y first) go through its
     text lines (by order, higher Y first) and save the images.
 
     Note: If there is a line at the same average height as another of
     the same text region, then they should be ordered them
     horizontally. In this case, the X of the text region was
     considered as its smallest x value (closest to the left
     margin). This really never happens in the corpus, there are no
     lines from the same text region that start at the same height and
     added text is always a bit above or below the actual text line.
 
Images/Pages
  Directory with the page images in jpg format. These images are
  in colour. The file names do not follow clear sorting criterion.
  
PAGE
  PAGE xml files in 2010 format. Each line is registered with a polygon
  and has associated its transcript. There is a PAGE xml file for each
  file in Images/Pages.
  
  
Partitions
  This directory has the files names for the partitions. Use this information
  as you prefer.

Transcriptions

  This directory has the transcripts at line level. There is a
  transcript file for each file in Images/Lines. The file names in
  this directory are in correspondence with the file names in
  Images/Lines.  

  In these transcripts, the punctuation symbols are separated from the
  words. 

If you have any addition comment, please send an email to
jandreu@prhlt.upv.es with the subject Bentham Dataset R0

June 2014
