#######################################################################
# MAD:
#       Miguel & Daniel Sepulveda    2017
#   
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
def linear_regression( m, w, x, y ):

    yp = []

    # Total number of dataa points
    Ntotal = len(x)

    if( len(y) != Ntotal ):

        logging.error("Inconsistent input data")
        exit(1)
    

    # Check if m provided
    if m > 0:

        N = (m-1)/2
        
        Nstart = N
        Nend   = Ntotal -1 - N
        
        # Copy first N values
        for i in range(N):
            yp.append( y[i] )

        # Interpolate values locally using linear
        # regression and fixed size window
        for i in range(Nstart, Nend+1):

            i0 = i - N
            i1 = i + N + 1

            beta = mad_regression.linear_regression(m, x[i0:i1], y[i0:i1])

            # Local approximation
            ypi = beta[0] + beta[1] * x[i]
            yp.append(ypi)

        # Copy last N values
        for i in range(N):
            j = Nend + 1 + i
            yp.append( y[j] )

            
    return yp
#######################################################################
def quadratic_regression( m, w, x, y ):

    yp = []

    # Total number of dataa points
    Ntotal = len(x)

    if( len(y) != Ntotal ):

        logging.error("Inconsistent input data")
        exit(1)
    

    # Check if m provided
    if m > 0:

        N = (m-1)/2
        
        Nstart = N
        Nend   = Ntotal -1 - N
        
        # Copy first N values
        for i in range(N):
            yp.append( y[i] )

        # Interpolate values locally using linear
        # regression and fixed size window
        for i in range(Nstart, Nend+1):

            i0 = i - N
            i1 = i + N + 1

            beta = mad_regression.quadratic_regression(m, x[i0:i1], y[i0:i1])

            # Local approximation
            ypi = beta[0] + beta[1] * x[i] + beta[2] * x[i] * x[i]
            yp.append(ypi)

        # Copy last N values
        for i in range(N):
            j = Nend + 1 + i
            yp.append( y[j] )

            
    return yp

#######################################################################
def local_linear_regression( m, w, x, y ):

    yp = []

    # Total number of dataa points
    Ntotal = len(x)

    if( len(y) != Ntotal ):

        logging.error("Inconsistent input data")
        exit(1)
    

    # Check if m provided
    if m > 0:

        N = (m-1)/2
        
        Nstart = N
        Nend   = Ntotal -1 - N
        
        # Copy first N values
        for i in range(N):
            yp.append( y[i] )

        # Interpolate values locally using linear
        # regression and fixed size window
        for i in range(Nstart, Nend+1):

            i0 = i - N
            i1 = i + N + 1
            im = (i0+i1)/2

            beta = mad_regression.local_linear_regression(m, w, x[i], x[i0:i1], y[i0:i1])

            # Local approximation
            ypi = beta[0] + beta[1] * x[i]
            yp.append(ypi)

        # Copy last N values
        for i in range(N):
            j = Nend + 1 + i
            yp.append( y[j] )

            
    return yp

#######################################################################
def local_quadratic_regression( m, w, x, y ):

    yp = []

    # Total number of dataa points
    Ntotal = len(x)

    if( len(y) != Ntotal ):

        logging.error("Inconsistent input data")
        exit(1)
    

    # Check if m provided
    if m > 0:

        N = (m-1)/2
        
        Nstart = N
        Nend   = Ntotal -1 - N
        
        # Copy first N values
        for i in range(N):
            yp.append( y[i] )

        # Interpolate values locally using linear
        # regression and fixed size window
        for i in range(Nstart, Nend+1):

            i0 = i - N
            i1 = i + N + 1
            im = (i0+i1)/2

            beta = mad_regression.local_quadratic_regression(m, w, x[i], x[i0:i1], y[i0:i1])

            # Local approximation
            ypi = beta[0] + beta[1] * x[i] + beta[2] * x[i] * x[i]
            yp.append(ypi)

        # Copy last N values
        for i in range(N):
            j = Nend + 1 + i
            yp.append( y[j] )

            
    return yp

#######################################################################
def main():

    logging.basicConfig( level=logging.DEBUG )
    
    ##############################################
    # Parse command line arguments

    import argparse

    parser = argparse.ArgumentParser(description="Command to denoise a time signal")

    parser.add_argument("-i",  help="input file name", type=str, required=True)
    parser.add_argument("--out", "-o", help="output file name", type=str)
    parser.add_argument("--algorithm", help="algorithm use for denoising", type=str)
    parser.add_argument("-m", help="number of points for local interpolation", type=int)
    parser.add_argument("--width", "-w", help="width of local interpolation window", type=float) 
    
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
    m = None
    if args.m > 0:

        m = 2 * args.m + 1
        if m < 2:
            logging.error("m={} must be larger than 0 ".format(args.m))
            exit(1)

    # Optional interpolation width
    w = None
    if args.width > 0.0:

        w = args.width

    # Algorithm selection
    algoritm = None
    if not args.algorithm:

        logging.error("You must provide an algorithm for denoising")
        exit(1)

    elif args.algorithm == "lr":
        algorithm = linear_regression

    elif args.algorithm == "qr":
        algorithm = quadratic_regression

    elif args.algorithm == "llr":
        algorithm = local_linear_regression

    elif args.algorithm == "lqr":
        algorithm = local_linear_regression

    else:
        
        logging.error("Unknown algorithm")
        exit(1)

        

        
    ##############################################
    # Load signal data

    (x,y) = load_data( args.i )


    ##############################################
    # Apply de-noising algorithm
    
    yp = algorithm( m, w, x, y )


    ##############################################
    # Output
    
    if not outpath:

        N = len(x)
        
        for i in range(N):

            print "{:.6f} {:.6f}".format( x[i], yp[i] )

    else:

        out = open( outpath, "wt")

        N = len(x)
        
        for i in range(N):

            out.write( "{:.6f} {:.6f} \n".format( x[i], yp[i] ) )

        out.close()
            
        

#######################################################################
if __name__ == '__main__':

    main()
    
