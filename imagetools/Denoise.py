from numpy import *

def denoise(im, U_init, tolerance = 0.1, tau=0.125, tv_weight=100):
    m,n = im.shape

    #initialize
    U = U_init
    Px = im # x-component to the dual field
    Py = im # y-component of the dual field
    error = 1

    while(error > tolerance):
        Uold = U

        #gradient of the primal variable
        GradUx = roll(U, -1, axis = 1) - U
        GradUy = roll(U, -1, axis = 0) - U

        #update the dial variable
        PxNew = Px + (tau/tv_weight)*GradUx
        PyNew = Py + (tau/tv_weight)*GradUy
        NormNew = maximum(1, sqrt(PxNew**2, PyNew**2))

        Px = PxNew/NormNew
        Py = PyNew/NormNew

        #update the primal variable
        RxPx = roll(Px, 1, axis=1)
        RyPy = roll(Py, 1, axis=0)

        DivP = (Px - RxPx) + (Py-RyPy) #divergence of the dual field
        U = im + tv_weight*DivP

        #update of the error
        error = linalg.norm(U-Uold)/sqrt(n*m);
        print(error)
    return U, im-U #denoised image and texture residual




