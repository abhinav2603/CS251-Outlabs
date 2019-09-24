import numpy as np
#
import sys
#
np.set_printoptions(threshold=sys.maxsize)

def reconstruct_from_noisy_patches(input_dict, shape):
    """
    input_dict: 
    key: 4-tuple: (topleft_row, topleft_col, bottomright_row, bottomright_col): location of the patch in the original image. topleft_row, topleft_col are inclusive but bottomright_row, bottomright_col are exclusive. i.e. if M is the reconstructed matrix. M[topleft_row:bottomright_row, topleft_col:bottomright_col] will give the patch.

    value: 2d numpy array: the image patch.

    shape: shape of the original matrix.
    """
    # Initialization: Initialise M, black_count, mid_count, white_count, mid_total
    M=np.zeros(shape).astype(np.int)
    black_count=np.zeros(shape).astype(np.int)
    mid_count=np.zeros(shape).astype(np.int)
    white_count=np.zeros(shape).astype(np.int)
    mid_total=np.zeros(shape).astype(np.int)

    for topleft_row, topleft_col, bottomright_row, bottomright_col in input_dict: # no loop except this!
        tlr, tlc, brr, brc = topleft_row, topleft_col, bottomright_row, bottomright_col ##WHY?
        patch = input_dict[(tlr, tlc, brr, brc)]
        # change black_count, mid_count, white_count, mid_total here
        #is_black=patch==0#wherver it was zero
        #is_white=patch==255
        #is_mid=(patch!=0) and (patch!=255)
        black_count[topleft_row:bottomright_row,topleft_col:bottomright_col]+=(patch==0).astype(np.int)
        white_count[topleft_row:bottomright_row,topleft_col:bottomright_col]+=(patch==255).astype(np.int)
        mid_count[topleft_row:bottomright_row,topleft_col:bottomright_col]+=np.logical_and(patch>0,patch<255).astype(np.int)
        #mid_count[topleft_row:bottomright_row,topleft_col:bottomright_col]+=1
        #mid_count[topleft_row:bottomright_row,topleft_col:bottomright_col]-=(patch==255).astype(np.int)
        #mid_count[topleft_row:bottomright_row,topleft_col:bottomright_col]-=(patch==0).astype(np.int)
        mid_total[topleft_row:bottomright_row,topleft_col:bottomright_col]+=patch*(np.logical_and(patch!=0,patch!=255).astype(np.int))
    # Finally change M here
    M[mid_count!=0]=np.around(mid_total[mid_count!=0]/mid_count[mid_count!=0])
    M[M==256]=255
    #M[np.logical_and(black_count==white_count,mid_count==0)]=0
    M[np.logical_and(np.logical_and(black_count<=white_count,mid_count==0),white_count!=0)]=255
    M[np.logical_and(black_count>white_count,mid_count==0)]=0
    M[np.logical_and(np.logical_and(black_count==0,white_count==0),mid_count==0)]=0
    #print(mid_total[mid_count!=0]==0)
    return M # You have to return the reconstructed matrix (M).

