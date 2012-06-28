#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Python module for addheader

Features:
- Adds license headers to files
"""
__author__ = ' <steen@manniche.net>'

import os
import sys
import fnmatch
import license_dicts
import re

def write_header( path, var_dict ):
    """Add the required copyright and license header to module in path"""

    if has_license( path ):
       return

    ft = ""
    with open( path, 'r' ) as candidate:
        if var_dict[ 'postfix' ] == 'java':
            cmt_start = '/**'
            cmt_mid   = '*'
            cmt_end   = '*/'
        elif var_dict[ 'postfix' ] == 'py':
            cmt_start = cmt_mid = cmt_end = '#'

        licensetext = os.linesep.join( license_dicts.license_texts[ var_dict.get( 'license' ) ].split( os.linesep ) )
        
        if var_dict.get( 'license' ) == 'gpl':
            licensetext =  licensetext%( var_dict.get( 'year' ),
                                         var_dict.get( 'author' ),
                                         var_dict.get( 'project_name' ),
                                         var_dict.get( 'project_name' ),
                                         var_dict.get( 'project_name' ),
                                         var_dict.get( 'project_name' )
                                         )

        nt = cmt_start
        licensetext = [ '%s%s'%( cmt_mid, l ) for l in licensetext.split( os.linesep ) ]
        nt = nt + os.linesep.join( licensetext ) + cmt_end
        
        ft = candidate.read()
        ft = nt + ft
        
    with open( path, 'w' ) as new:
        new.write( ft )
        print "Wrote %s license to %s"%( var_dict.get( 'license' ), path )


def add_header( options, path ):
    """
    
    Arguments:
    - `type`:
    - `year`:
    """
    target = path[0]
    var_dict = set_vars( options )

    for (root, dirs, files) in os.walk(target):
        if root.find(os.sep + '.') != -1: # skip all dot dirs
            continue
        for name in files:
            path = os.path.join( root, name )
            if os.path.islink( path ): #skip symlinks
                continue
            print 'Checking if %s is of type %s' % ( path, options.filetype )
            if path.find( var_dict.get( 'postfix' ) ) > 0:
                print 'Matched for %s found in %s' % ( var_dict.get( 'postfix' ), path )
                write_header( path, var_dict )

def has_license( file_to_check ):
    """
   
    Arguments:
    - `file_to_check`:
    """
    gpl_re = "under the terms of the GNU General Public License"
    asl_re = "Licensed to the Apache Software Foundation"
    generic_re = "[Cc]opyright\s\d{4}\s\w+"

    with open( file_to_check ) as ftc:
        text = ftc.read()
        if re.search( gpl_re, text ):
            print "found GPL in %s"%( file_to_check )
            return True
        elif re.search( asl_re, text ):
            print "found ASL in %s"%( file_to_check )
            return True
        elif re.search( generic_re, text ):
            print "found license in %s"%( file_to_check )
            return True
        else:
            print "found no license in %s"%( file_to_check )
            return False

def set_vars( options ):
    vars = dict()

    if options.filetype == "java":
        vars[ "postfix" ] = "java"
    elif options.filetype == "python":
        vars[ "postfix" ] = "py"

    vars[ "year" ] = options.year

    vars[ "license" ] = options.license

    if options.author:
        vars[ "author" ] = options.author

    if options.project:
        vars[ "project_name" ] = options.project
    return vars


if __name__ == '__main__':
    
    from optparse import OptionParser

    usg = """%prog [options] path

This script add license headers to files in `path` that does not already have a license header
"""

    parser = OptionParser( usage = usg)
    parser.add_option("--filetype", dest="filetype", default="java",
                      help="filetype to examine, values are {java,python}")
    parser.add_option("-a", "--author", dest="author",
                      help="Author of the source code, can be empty")
    parser.add_option("-y", "--copyrightyear",
                      dest="year", default="2012",
                      help="Copyright year(s), specify with either a single year (2012) or a range (2010-2012)")
    parser.add_option("-l", "--licensetype", dest="license",
                      help="License to apply to the source files, can be one of {gpl, asl}")
    parser.add_option("-p", "--projectname", dest="project",
                      help="Name of the project")

    (options, args) = parser.parse_args()

    if not options.license:
        sys.exit( "A license must be choosen." )
    
    if not args:
        sys.exit( "A path to start the search from must be specified" )
    if len( args ) > 1:
        sys.exit( "Only a path should be specified" )
    add_header( options, args )

