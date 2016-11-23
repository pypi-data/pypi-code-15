# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import, unicode_literals
import numpy as np


class DMImage(object):
    """
    From DM4Import.py
    
    This structure-like class is for storing 2D image or 3D image stack information, since 
    Digital Micrography likes to have more than one in a file.  Should store 
    Calibrations, Data, and ImageTags.  
    
    Data we will store in numpy format, for the other stuff we'll use a dictionary.

    """
    def __init__( self ):
        self.imageInfo = {} # Calibrations, tags, all in a dictionary
        self.shape = [] # necessary for unraveling
        self.imageData = np.zeros(1)
    


class readDM4(object):
    """
    readDM4
    
    Created on Wed Apr 01 17:58:48 2015
    @author: Robert A. McLeod
    
    This is designed to be a fast DM4 file reader to strip the data out of the 
    large movie-mode files generated by K2 detectors along with important tags.  
    Due to the emphasis on speed it's not a general file parser with dynamic 
    allocation and such, so if Gatan changes the format a lot it will break the 
    script.
    
    Usage:
        
    dm4struct = readDM4( filename, verbose=False, useMemmap = False )
    
        dm4struct holds the (multiple) images in the DM4.  Typically the zeroth 
        image is the thumbnail, 
        
        i.e. to convert to MRCZ:
        
        
        imageData = dm4struct.im[1].imageData, is a NumPy array containing image 
        intensities.
        imageInfo = dm4struct.im[1].imageInfo, is a dict containing meta-data.
        
    Chris Boothroyd provides some information on the structure of .DM4 files here:
    
    http://www.er-c.org/cbb/info/dmformat/
    
    The directory structure of the file is tracked by passing the path of the parent to 
    each tag parser. Gatan likes to have empty tag directories, so I autonumber them.
    
    One can examine file structure by setting verbose = True, if you need to add 
    some more tags to the dictionary generated by the parseTag function, for example.
    """
    
    def __init__( self, filename, verbose=False, useMemmap = False ):
        # So basic strategy is use memmap to parse the tags and find the image data, which
        # can then be loaded fast with 
        self.f = open( filename, 'rb' )
        
        if verbose: print( "Opening DM4 file: %s" % filename )
        self.useMemmap = useMemmap
        
        # Instatiate class fields
        self._unnamedIndices = np.zeros( 20, dtype='int' ) # maximum number of nested tags
        self.im = [] # list of DMImage class objects
        self.verbose = verbose 
        
        # version = struct.unpack( '>I', f.read(4) )
        version = np.fromfile( self.f, dtype='>i4', count=1 )[0]
        if( version != 4):
            print( "Warning: Only DM4 is supported, will probably crash spectacularly" )
        np.fromfile( self.f, dtype='>i8', count=1 )[0] # rootlen
        byteord = np.fromfile( self.f, dtype='>i4', count=1 )[0] # 1 = little endian, generally it always is
        if byteord != 1:
            print( "Error: only little endian data ordering supported at present" )
            return
        
        np.fromfile( self.f, dtype='i1', count=1 )[0] # 1 = sorted
        np.fromfile( self.f, dtype='i1', count=1 )[0] # 1 = open structure
        ntags_root = np.fromfile( self.f, dtype='>i8', count=1 )[0] # number of tags
        
        if self.verbose: print( "DM version %d, byte order %d" %(version, byteord) )
        # Now the tags start
        for J in np.arange( 0, ntags_root ):
            
            tag_type = np.fromfile( self.f, dtype='i1', count=1 )[0] # 20 = tag directory, 21 = tag base, 0 == EOF
            
            #print( "DEBUG: root tag: %d" % tag_type )
            if( tag_type == 20 ):
                
                loc_tagstart = self.f.tell()
                tag_namelen = np.fromfile( self.f, dtype='>i2', count=1 )[0]


                if tag_namelen > 0:
                    tag_name = self.f.read( tag_namelen )
                    # tag_name = np.fromfile( self.f, dtype='S%d'%tag_namelen, count=1 )[0]
                else:
                    tag_name = b""
                    
                tag_fieldlen = np.fromfile( self.f, dtype='>i8', count=1 )[0]  
                #print( "rootTag: tag_name: %s has length %d and field length %d" %(tag_name, tag_namelen, tag_fieldlen ))      

                
                #print( "DEBUG: found tag %s with fieldlen %d" %(tag_name, tag_fieldlen) )
                if tag_name == b"ImageList":
                    self.f.seek( loc_tagstart )
                    # So each image is an unnamed tag directory, composed of /ImageData and /ImageTags and /UniqueID
                    self.parseTagDir( b"/" )
                    
                    # We currently do not care about any tag but ImageList
                    break
                else:
                    # Go to next tag/tagdir
                    #print( "Seeking to: " + str(self.f.tell() + tag_fieldlen) )
                    self.f.seek( self.f.tell() + tag_fieldlen )
                
            elif( tag_type == 21 ):
                # throw away tags in root because we don't care for them
                self.discardTag()
            elif( tag_type == 0 ):
                break # EOF
            pass
        self.f.close()
        
        # Unravel images
        for mage in self.im:
            # FYI: Gatan stores image stacks [z,y,x] which is opposite to how they store the dimensions (but is Numpy and C convention)
            mage.shape = np.flipud( np.array( mage.shape ) )
            # This y-flip [:,::-1,...] puts us on the same origin-standard for data as MRC
            # Gatan uses a different standard for the origin location inside DM4 files.
            mage.imageData =  np.reshape( mage.imageData, mage.shape, order='C' )[:,::-1,...]
            # Image data is now compatible with MRCs saved in GMS, IMOD, EMAN2, etc.
        # Clean up anything else
            
    def parseTag( self, parent ):
        """ Parse a tag at the given file handle location """
        tag_namelen = np.fromfile( self.f, dtype='>i2', count=1 )[0]
        
        if tag_namelen > 0:
            # tag_name = np.fromfile( self.f, dtype='S%d'% tag_namelen, count=1 )[0]
            tag_name = self.f.read( tag_namelen )
        else:
            tag_name = b""
        
        tag_fieldlen = np.fromfile( self.f, dtype='>i8', count=1 )[0]
        # print( "parseTag: tag_name: %s has length %d and field length %d" %(tag_name, tag_namelen, tag_fieldlen ))      
        loc_tag = self.f.tell() # Save location so we can seek to end of tag later
        self.f.read(4) # Throw away %%%% seperator
        tag_ninfo = np.fromfile( self.f, dtype='>i8', count=1 )[0]
        if self.verbose: 
            print( "Found tag: %s%s with %d elements" % (parent, tag_name, tag_ninfo)  )
            
        split_tag_name = (parent + tag_name).split( b'/' )
        
        # print( "DEBUG: split_tag_name : " + str(split_tag_name) )
        # Fixed nested parsing?
        # Skip ImageList
        
        imageIndex = np.int64( split_tag_name[2] )
        # print( "DEBUG: found imageIndex: %s" % imageIndex )
        
        # Check to see if self.im[imageIndex] exists
        try:
            self.im[imageIndex]
        except IndexError:
            self.im.append( DMImage() )    
            
        if split_tag_name[3] == b'ImageData':
            dimCount = 0
            if split_tag_name[4] == b'Calibrations':
                # No calibrations saved at present
                # /ImageList/1/ImageData/Calibrations/Brightness/Origin
                # /ImageList/1/ImageData/Calibrations/Brightness/Scale
                # /ImageList/1/ImageData/Calibrations/Brightness/Units
                # /ImageList/1/ImageData/Calibrations/Dimension/[0-2]/Origin
                # /ImageList/1/ImageData/Calibrations/Dimension/[0-2]/Scale
                # /ImageList/1/ImageData/Calibrations/Dimension/[0-2]/Units
                if split_tag_name[5] == b'Brightness':
                    if split_tag_name[6] == b'Origin':
                        self.im[imageIndex].imageInfo['IntensityOrigin'] = self.retrieveTagData( tag_ninfo )
                    elif split_tag_name[6] == b'Scale':
                        self.im[imageIndex].imageInfo['IntensityScale'] = self.retrieveTagData( tag_ninfo )  
                    elif split_tag_name[6] == b'Units':
#                        unicode_array = self.retrieveTagData( f, tag_ninfo )
#                        self.im[imageIndex].imageInfo['IntensityUnits'] = "".join([chr(item) for item in unicode_array])
                        self.im[imageIndex].imageInfo['IntensityUnits'] = self.retrieveTagData( tag_ninfo ).astype(np.uint8).tostring().decode('utf-8')
                        
                elif split_tag_name[5] == b'Dimension':
                    # 0 = x, 1 = y, 2 = z for split_tag_name[6]
                    #print( split_tag_name[6] )
                    #print( np.frombuffer( split_tag_name[6], dtype='>i8' ) )
                    #print( np.frombuffer( split_tag_name[6], dtype='<i8' ) )
                    
                    if np.int64( split_tag_name[6] ) == 0:
                        currDim = 'X'
                    elif np.int64( split_tag_name[6] ) == 1:
                        currDim = 'Y'
                    elif np.int64( split_tag_name[6]) == 2:
                        currDim = 'Z'
                    else:
                        raise ValueError( "DM4Import: Unknown dimension " + str(split_tag_name[6]) + " at location " + hex(self.f.tell()) )
                        
                    # Units is stored as uint16 array, which is actually unicode?
                    if split_tag_name[7] == b'Origin':
                        self.im[imageIndex].imageInfo['Dim'+currDim+'Origin'] = self.retrieveTagData( tag_ninfo )
                    elif split_tag_name[7] == b'Scale':
                        self.im[imageIndex].imageInfo['Dim'+currDim+'Scale'] = self.retrieveTagData( tag_ninfo )  
                    elif split_tag_name[7] == b'Units':
#                        unicode_array = self.retrieveTagData( f, tag_ninfo )
#                        self.im[imageIndex].imageInfo['Dim'+currDim+'Units'] = "".join([chr(item) for item in unicode_array])
                        # Sometimes we have wierd characters in the Units tag
                        try:
                            self.im[imageIndex].imageInfo['Dim'+currDim+'Units']= self.retrieveTagData( tag_ninfo ).astype(np.int16).tostring().decode('utf-8')
                        except:
                            try:
                                # "ISO-8859-1"
                                # 'windows-1252'
                                self.im[imageIndex].imageInfo['Dim'+currDim+'Units']= self.retrieveTagData( tag_ninfo ).astype(np.int16).tostring().decode("ISO-8859-1")
                            except:
                                pass
            
                pass
            elif split_tag_name[4] == b'Data':
                # self.verbose = True
                if self.verbose:
                    print( "Found image %d"%imageIndex + " at offset : " + str(self.f.tell() ) )
                self.im[imageIndex].imageData = self.retrieveTagData( tag_ninfo, memmap = self.useMemmap )
                # self.verbose = False
                pass
            elif split_tag_name[4] == b'Dimensions':
                self.im[imageIndex].shape.append( self.retrieveTagData( tag_ninfo ) )
                dimCount += 1
                pass
            #elif split_tag_name[4] == b'PixelDepth':
            #    pass
            pass
        elif split_tag_name[3] == b'ImageTags':
        
            if split_tag_name[4] == b'Acquisition':
                ### Find image flips ###
                # Here is where we can save any tags that we care for, like image rotations
                # /ImageList/1/ImageTags/Acquisition/Frame/Area/Transform/Transform List/0/Transpose/Horizontal Flip
                if split_tag_name[-1] == b"Horizontal Flip" and split_tag_name[-4] == b'Device':
                    # So annoyingly there are several of these tags, only some of which are the true flips.
                    self.im[imageIndex].imageInfo['HorzFlip'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[-1] == b"Vertical Flip" and split_tag_name[-4] == b'Device':
                    self.im[imageIndex].imageInfo['VertFlip'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[-1] == b"Diagonal Flip" and split_tag_name[-4] == b'Device':   
                    self.im[imageIndex].imageInfo['DiagFlip'] = self.retrieveTagData( tag_ninfo )
                    
                # Pixel size seems to be complex, not sure if I'm retrieving it correctly (only important for non-square pixel detectors)
                elif split_tag_name[-1] == b"Pixel Size (um)" and split_tag_name[-3] == b'Device':
                    self.im[imageIndex].imageInfo['DetectorPixelSize'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[-1] == b"Exposure" and split_tag_name[-2] == b'Detector':
                    self.im[imageIndex].imageInfo['Exposure'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[-1] == b"hbin" and split_tag_name[-2] == b'Detector':
                    self.im[imageIndex].imageInfo['HorzBin'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[-1] == b"vbin" and split_tag_name[-2] == b'Detector':
                    self.im[imageIndex].imageInfo['VertBin'] = self.retrieveTagData( tag_ninfo )
                
            elif split_tag_name[4] == b'Calibration':
                
                if split_tag_name[5] == b'Dose Rate':
                   if split_tag_name[6] == b'Calibration':
                       if not 'DoseRateCalibration' in self.im[imageIndex].imageInfo:
                           self.im[imageIndex].imageInfo['DoseRateCalibration'] = []
                         
                       try:
                           self.im[imageIndex].imageInfo['DoseRateCalibration'].append( self.retrieveTagData( tag_ninfo ) )
                       except:
                           print( "FAILED TO IMPORT DOSERATECALIBRATION" )
                       

#                       
#                       self.im[imageIndex].imageInfo['DoseRateCalibration'][int(split_tag_name[7][1])] = np.float32(    )


            elif split_tag_name[4] == b'Microscope Info':
                if split_tag_name[5] == b'Actual Magnification':
                    self.im[imageIndex].imageInfo['ActualMag'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[5] == b'Indicated Magnification':
                    self.im[imageIndex].imageInfo['NominalMag'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[5] == b'Cs(mm)':
                    self.im[imageIndex].imageInfo['C3'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[5] == b'Voltage':
                    self.im[imageIndex].imageInfo['Voltage'] = self.retrieveTagData( tag_ninfo )   
                elif split_tag_name[5] == b'Mode':
                    self.im[imageIndex].imageInfo['MicroscopeMode'] = self.retrieveTagData( tag_ninfo ).astype(np.uint8).tostring().decode('ascii')  
                pass
            elif split_tag_name[4] == b'EELS Spectrometer':
                if split_tag_name[5] == b'Aperture index':
                    self.im[imageIndex].imageInfo['EELSApertureIndex'] = self.retrieveTagData( tag_ninfo ) 
                elif split_tag_name[5] == b'Aperture label':
                    self.im[imageIndex].imageInfo['EELSApertureLabel'] = self.retrieveTagData( tag_ninfo ).astype(np.uint8).tostring().decode('ascii')
                elif split_tag_name[5] == b'Energy loss (eV)':
                    self.im[imageIndex].imageInfo['EELSEnergyLoss'] = self.retrieveTagData( tag_ninfo )    
                elif split_tag_name[5] == b'Slit inserted':
                    self.im[imageIndex].imageInfo['EELSSlitIn'] = self.retrieveTagData( tag_ninfo )
                elif split_tag_name[5] == b'Slit width (eV)':
                    self.im[imageIndex].imageInfo['EELSSlitWidth'] = self.retrieveTagData( tag_ninfo )   
            elif split_tag_name[4] == b"Latitude-S":
                if split_tag_name[5] == b"Distance To Focus Position":
                    self.im[imageIndex].imageInfo['LatSDistanceToFocus'] = self.retrieveTagData( tag_ninfo )   
                elif split_tag_name[5] == b"Intended Defocus":
                    self.im[imageIndex].imageInfo['LatSIntendedDefocus'] = self.retrieveTagData( tag_ninfo )      
                elif split_tag_name[5] == b"Beam Diameter (nm)":
                    self.im[imageIndex].imageInfo['LatSBeamDiameter'] = self.retrieveTagData( tag_ninfo )         
        # Go to next location
        self.f.seek( loc_tag + tag_fieldlen )
        return
        
    def getTagDType( self, bytecode ):
        if bytecode == 2: 
            return 'int16'
        elif bytecode == 3: 
            return 'int32'
        elif bytecode == 4: 
            return 'uint16'
        elif bytecode == 5:
            return 'uint32'
        elif bytecode == 6: 
            return 'float32'
        elif bytecode == 7: 
            return 'float64'
        elif bytecode == 8: 
            return 'bool'
        elif bytecode == 11:
            return 'int64'
        else:
            return ''
            
    def retrieveTagData( self, tag_ninfo, memmap = False ):
        """ Get the actual data from the tag, which is then stored in one of the dicts or imageData """
        # Here is basically where we should check tag_name to see if it's important...
        tag_loc = self.f.tell()
        tag_infos = np.fromfile( self.f, dtype='>i8', count=tag_ninfo )
        for K in np.arange(0,tag_infos.size):
            if tag_infos[K] == 15: # struct
                # Structs are organized really strangly in the file, they are essentially in the tag header so 
                # our reading doesn't work properly with them. In essence we need to go back to where 
                # we think the struct should be.  
                # print( "Correct struct ??? location: " + str( tag_loc + 8*K + 16 ) )
                self.f.seek( tag_loc + 8*K + 16 )
                struct_fieldcount = np.fromfile( self.f, dtype='>i8', count=1 )
                struct_fielddtype = []
                struct_fieldval = []
                for J in np.arange(0,struct_fieldcount):
                    np.fromfile( self.f, dtype='>i8', count=1 ) # Zero 
                    struct_fielddtype.append( self.getTagDType( np.fromfile( self.f, dtype='>i8', count=1 ) ) )
                    # print( str(J) + ": field dtype = " + str( struct_fielddtype[J] ) )
                for J in np.arange(0,struct_fieldcount):
                    struct_fieldval.append( np.fromfile(self.f, dtype=struct_fielddtype[J], count=1)[0] )
                    # print( str(J) + ": field val = " + str( struct_fieldval[J] ) )
                return struct_fieldval
            elif tag_infos[K] == 20: # array
                if self.verbose: print( "Found array" )
                try:
                    K += 1 # Warning: sometimes arrays are empty
                    array_dtype = self.getTagDType(tag_infos[K])
                    K += 1
                    array_ncount = tag_infos[K]
                    if self.verbose: print( "Array dtype: " + array_dtype + ", array ncount: " + str(array_ncount) )
                    if( array_ncount > 0 ):
                        if memmap:
                            return np.memmap( self.f, dtype=array_dtype, mode='r', shape=array_ncount )
                        else:
                            return np.fromfile( self.f, dtype=array_dtype, count=array_ncount )
                except IndexError:
                    pass
                pass
            elif tag_infos[K] == 9: # string
                tag_char = self.f.read(1)
                if self.verbose: print( "Found char: " + tag_char )
                pass
            elif tag_infos[K] == 18: # string
                # str_len = 
                if self.verbose: print( "FIXME Found string" )
                pass
            else: # singleton
                tag_dtype = self.getTagDType( tag_infos[K] )
                if tag_dtype != '':
                    tag_data = np.fromfile( self.f, dtype = tag_dtype, count=1 )[0]
                    # if self.verbose: print( "Singleton: " + tag_dtype + ": " + str(tag_data) ):
                    if self.verbose: print( "Singleton: " + tag_dtype + ": " + str(tag_data) )
                    return tag_data
        pass
    
    def discardTag( self ):
        """ Quickly parse to the end of tag that we don't care about its information """
        tag_namelen = np.fromfile( self.f, dtype='>i2', count=1 )[0]
        self.f.seek( self.f.tell() + tag_namelen )
        tag_fieldlen = np.fromfile( self.f, dtype='>i8', count=1 )[0]
        self.f.seek( self.f.tell() + tag_fieldlen )
        return
        
    def parseTagDir( self, parent ):
        """ Parse a tag directory at the given file handle location """
        try:
            tag_namelen = np.fromfile( self.f, dtype='>i2', count=1 )[0]
            
            if tag_namelen > 0:
                tag_name = self.f.read( tag_namelen )
                # tag_name = np.fromfile( self.f, dtype='S%d'%tag_namelen, count=1 )[0]
            else:
                tag_name = b""
            
            tag_fieldlen = np.fromfile( self.f, dtype='>i8', count=1 )[0]
            # print( "parseTagDir: tag_name: %s has length %d and field length %d" %(tag_name, tag_namelen, tag_fieldlen ))  
            
        except IndexError:
            if self.verbose: print( "Caught IndexError, trying to recover position in file" )
            # f.seek( f.tell() )
            return self.f
    
        # Handle empty tag_name by giving it an auto-generated number
        if not bool(tag_name):
            if( self.verbose ) : print( "Found empty tag" )
            tag_depth = int( parent.count( b'/') - 1 )
            
            # This is kind of mental gymnastics to maintain portablity between Python 2 and 3
            tag_name = bytearray( str(self._unnamedIndices[ tag_depth ]).encode('ascii') )
            # print( "Gymnastics " + str(self._unnamedIndices[ tag_depth ]) + " -> " + str(tag_name) )
            self._unnamedIndices[ tag_depth ] += 1
            # Reset all higher indices
            self._unnamedIndices[ tag_depth+1:] = 0
        loc_tagdir = self.f.tell()
        self.f.read( 2 ) # Throw away sorted and closed
        ntags_dir = np.fromfile( self.f, dtype='>i8', count=1 )[0]
        if self.verbose:
            print( "Found tag dir " + str(parent) + str(tag_name) + " with " + str(ntags_dir) + " tags" )
        
        # So typically ImageList has two empty name tag directories, of which one is various stuff and the other is the data
        for I in np.arange(0, ntags_dir ):
            try:
                subtag_type = np.fromfile( self.f, dtype='i1', count=1 )[0] # 20 = tag directory, 21 = tag base, 0 == EOF
            except IndexError:
                if self.verbose:
                    print( "Caught IndexError, trying to recover" )
                break
            if( subtag_type == 20 ):
                self.parseTagDir( bytes(parent) + bytes(tag_name) + b"/" )
            elif( subtag_type == 21 ):
                self.parseTag( bytes(parent) + bytes(tag_name) + b"/" )
            elif( subtag_type == 0 ):
                break # EOF
        # Go to next tag in root directory
        self.f.seek( loc_tagdir + tag_fieldlen )
        return
    
    

