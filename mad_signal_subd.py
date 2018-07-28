#######################################################################
# MAD:
#       Miguel & Daniel Sepulveda    2017
# 
#   Naive implementation of this subdivision scheme:
#   "Univariate subdivision schemes for noisy data with geometric
#       application"
#         Journal Computer Aided Geometric Design
#         N Dyn, A Heard, Kai Horman, Nir Sharon
#
#   Note: We do not assume equidistant samples here
#######################################################################
import math
import logging
import random
import os
import mad_regression

#######################################################################
def load_data( path ):

    x = []
    y = []
    
    if not os.path.exists(path):
        logging.error("Unable to find the file {}".format(path))
        exit(1)

    f = open(path, "rt")
    line = f.readline().strip()

    while(line):

        (xi, yi) = line.split()
        x.append( float(xi) )
        y.append( float(yi) )
        
        line = f.readline().strip()
    
    return (x,y)

#######################################################################
def subdivide( sn, x, y ):

    xp = []
    yp = []

    Ntotal = len(x)
    if( len(y) != Ntotal ):

        logging.error("Inconsistent input data")
        exit(1)

    # For every input point we generate to subdivided points f(k) and f(k+1),
    # last one being a half-step refinement

    m = 4 * sn - 1
    N = 2 * sn - 1

    Nstart = 2 * sn - 1
    Nend   = Ntotal -1 - 2 * sn

    # Copy first Nstart values (Can't be subdivided)
    for i in range(Nstart):
        xp.append( x[i] )
        yp.append( y[i] )

    # Apply subdivision rules
    for i in range(Nstart, Nend+1):

        i0 = i - N
        i1 = i + N + 1

        # F(k) subdivision rule
        beta = mad_regression.linear_regression(m, x[i0:i1], y[i0:i1])
        ypi = beta[0] + beta[1] * x[i]

        xp.append(x[i])
        yp.append(ypi)
        
        # F(k+1) subdivision rule
        beta = mad_regression.linear_regression(m, x[i0:i1+1], y[i0:i1+1])

        xpi = 0.5 * (x[i] + x[i+1])
        ypi = beta[0] + beta[1] * xpi

        xp.append(xpi)
        yp.append(ypi)

    # Copy last Nstart values (Can't be subdivided)
    for i in range(Nstart):
        j = Nend + 1 + i
        xp.append( x[j] )
        yp.append( y[j] )

    return (xp, yp)


#######################################################################
def main():

    logging.basicConfig( level=logging.DEBUG )
    
    ##############################################
    # Parse command line arguments

    import argparse

    parser = argparse.ArgumentParser(description="Command to denoise a time signal")

    parser.add_argument("-i",  help="input file name", type=str, required=True)
    parser.add_argument("--out", "-o", help="output file name", type=str)
    parser.add_argument("-sn", help="Sn subdivision scheme", type=int, default=1)
    parser.add_argument("-n", help="number of subdivision iterations", type=int, default=1)
    
    args = parser.parse_args()

    # If not out file specified write to console
    outpath = None
    if args.out:
        outpath = args.out

    # Check input data
    if not os.path.exists( args.i ):
        logging.error("File {} not found ".format(args.i))
        exit(1)

    # Number of interpolation steps
    if args.n <= 0:
        logging.error("Invalid number of subdivisions n={} ".format(args.n))
        exit(1)

    if args.sn <= 0:
        logging.error("Invalid subdivision scheme Sn={} ".format(args.sn))
        exit(1)


        
    ##############################################
    # Load signal data

    (x,y) = load_data( args.i )


    ##############################################
    # Apply de-noising algorithm

    xp = x
    yp = y
    for step in range(args.n):
        (xp, yp) = subdivide( args.sn, xp, yp )


    ##############################################
    # Output
    
    if not outpath:

        N = len(xp)
        
        for i in range(N):

            print "{:.6f} {:.6f}".format( xp[i], yp[i] )

    else:

        out = open( outpath, "wt")

        N = len(xp)
        
        for i in range(N):

            out.write( "{:.6f} {:.6f} \n".format( xp[i], yp[i] ) )

        out.close()
            
        

#######################################################################
if __name__ == '__main__':

    main()
