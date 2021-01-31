import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update( frameNum, img, world, N ) :

    newWorld = world.copy( )
    for i in range (N):
        for j in range (N):
            total= (world[(i-1)%N][(j-1)%N]+world[(i-1)%N][j]+world[(i-1)%N][(j+1)%N]+
                   world[i][(j-1)%N]+world[i][(j+1)%N]+ world[(i+1)%N][(j-1)%N]+
                   world[(i+1)%N][j]+ world[(i+1)%N][(j+1)%N])/255

            if world[i][j]== 255:

                if total>3 or total<2:
                    newWorld[i][j]= 0
            else:

                if total == 3:
                    newWorld[i][j] = 255

    img.set_data( newWorld )
    world[:] = newWorld[:]
    return img

N = 50
SPEED = 100
PROB_LIFE = 40

world= np.random.choice([0,255], N*N, p=[1-((PROB_LIFE)/100),(PROB_LIFE)/100]).reshape(N,N)

fig, ax = plt.subplots( )
img = ax.imshow( world, interpolation='nearest' )
ani = animation.FuncAnimation( fig, update, fargs = ( img, world, N ),
                               frames = 10, interval = SPEED,
                               save_count = 50 )
plt.show( )