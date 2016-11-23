# -*- coding: utf-8 -*-

from __future__ import print_function
import libsbgnpy.libsbgn as libsbgn

if __name__ == "__main__":
    f_in = 'sbgn/adh.sbgn'
    sbgn = libsbgn.parse(f_in)

    # map is a container for the glyphs and arcs 
    map = sbgn.get_map()

    # we can get a list of glyphs (nodes) in this map with getGlyph()
    for g in map.get_glyph():
        # print the sbgn class of this glyph
        print (" Glyph with class", g.get_id())

        # if there is a label, print it as well
        if g.get_label():
            print (", and label ", g.get_label().get_text())
        else:
            print (", without label")

    # we can get a list of arcs (edges) in this map with getArc()
    for a in map.get_arc():
        # print the class of this arc
        print (" Arc with class ", a.get_class())
