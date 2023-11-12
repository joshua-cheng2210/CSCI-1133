import copy

#If you're not sure how to start, look at the swap_red_blue and blur
#examples below.

#Problem A: Invert Colors
def invert(img_matrix):
    '''
    Purpose:
      Inverts the colors in an image by setting each color component to
      255 minus its original value.
    Input Parameter(s):
      A 3D matrix (list of lists of lists) representing an .bmp image
      Each element of the matrix represents one row of pixels in the image
      Each element of a row represents a single pixel in the image
      Each pixel is represented by a list of three numbers between 0 and 255
      in the order [red, green, blue]
    Return Value:
      A 3D matrix of the same dimensions, with the colors of each pixel inverted
    '''
    out = copy.deepcopy(img_matrix)
    for rows in out:
        for pixcels in rows:
            for c_pixcels in range(len(pixcels)):
                pixcels[c_pixcels] = 255 - pixcels[c_pixcels]
    return out
    
#Problem B: High Contrast
def high_contrast(img_matrix):
    '''
    Purpose:
      For every pixel, sets each color component to 0 (if the original
      value was 127 or less), or 255 (if the original value was >= 128).
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, with high-contrast colors
      as described above.
    '''
    out = copy.deepcopy(img_matrix)
    for rows in out:
        for pixcels in rows:
            for c_pixcels in range(len(pixcels)):
                # print(f"{pixcels}[{c_pixcels}] = {pixcels[c_pixcels]}")
                if pixcels[c_pixcels] <=  127:
                    pixcels[c_pixcels] = 0
                else:
                    pixcels[c_pixcels] = 255
    return out

#Problem C: Rotate Quadrants
def rotate_quadrants(img_matrix):
    '''
    Purpose:
      Split the image into four equally sized quadrants, and rotate
      them clockwise to form the output image.
    Input Parameter(s):
      (see invert) - plus, it can be assumed the img_matrix will have
      an even number of rows and columns.
    Return Value:
      A 3D matrix of the same dimensions, where each pixel has been moved
      to the corresponding location.  
    '''
    out = copy.deepcopy(img_matrix)
    # print(len(out))
    for yy in range(len(out)):
        for xx in range(len(out[yy])):
            # print(out[yy][xx])
            if (yy < (len(out) / 2) and xx < (len(out[yy]) / 2)):# if at top left,
                out[yy][xx] = copy.deepcopy(img_matrix[yy + int(len(out) / 2)][xx])
            elif (yy < (len(out) / 2) and xx >= (len(out[yy]) / 2)):# if at top right,
                out[yy][xx] = copy.deepcopy(img_matrix[yy][xx - int(len(out[yy]) / 2)])
            elif (yy >= (len(out) / 2) and xx < (len(out[yy]) / 2)):# if at bottom left,
                out[yy][xx] = copy.deepcopy(img_matrix[yy][xx + int(len(out[yy]) / 2)])
            elif (yy >= (len(out) / 2) and xx >= (len(out[yy]) / 2)):# if at bottom right,
                out[yy][xx] = copy.deepcopy(img_matrix[yy - int(len(out) / 2)][xx])
    return out

#Problem D: Your Own Filter
def custom_filter(img_matrix):
    '''
    Purpose:
      1) invert the image horizontally
      2) invert the image vertically
      3) make grayscale image filter
    Input Parameter(s):
      A 3D matrix (list of lists of lists) representing an .bmp image
      Each element of the matrix represents one row of pixels in the image
      Each element of a row represents a single pixel in the image
      Each pixel is represented by a list of three numbers between 0 and 255
      in the order [red, green, blue]
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    out1 = copy.deepcopy(img_matrix)
    for yy in range(len(out1)):
        for xx in range(len(out1[yy])):
        #     print(out[yy][xx])
        # print("-------------------------")
            out1[yy][xx] = copy.deepcopy(img_matrix[yy][(-1)*(xx + 1)])
    out2 = copy.deepcopy(out1)
    for yyy in range(len(out2)):
        out2[yyy] = copy.deepcopy(out1[(-1)*(yyy + 1)])
    out3 = copy.deepcopy(out2)
    for yyyy in range(len(out3)):
        for xxxx in range(len(out3[yyyy])):
            avg = sum(out3[yyyy][xxxx]) / 3
            for pixcell in range(len(out3[yyyy][xxxx])):
                out3[yyyy][xxxx][pixcell] = avg
    return out3

print(custom_filter([[ [255, 0, 0], [255,153,0], [255,255,0],[255,204,51]],
 [ [0, 255, 0], [0,255,255],[50,128,255],[255,204,51]],
 [ [0, 0, 255], [153,0,255], [255,0,255],[255,204,51]],
 [   [0, 0, 0],[255,204,51], [122,0,25] , [122,0,25] ],
 [[255,204,51], [122,0,25] , [122,0,25] , [122,0,25] ],
 [ [122,0,25] , [122,0,25] , [122,0,25] , [122,0,25] ],
 [ [122,0,25] , [122,0,25] , [122,0,25] , [122,0,25] ],
 [ [122,0,25] , [122,0,25] , [122,0,25] , [122,0,25] ]]))

#Example #1: Swapping red and blue components
def swap_red_blue(img_matrix):
    '''
    Purpose:
      Swaps the red and blue components in an image
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, with all colors inverted
      (that is, for every pixel list, the first and last values have been
      swapped.
    '''
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height):
        for x in range(width):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            old_red = img_matrix[y][x][0]
            old_blue = img_matrix[y][x][2]
            img_matrix[y][x][0] = old_blue
            img_matrix[y][x][2] = old_red
    return img_matrix


#Example #2: Blur the image
#(this is a little more complex than the ones you need to do)
def blur(img_matrix):
    '''
    Purpose:
      Blurs an image by applying a 3x3 pixel filter
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, with each pixel blurred:
      each color component is averaged with the surrounding 9 pixels
    '''
    height = len(img_matrix)
    width = len(img_matrix[0])
    #Make a deep copy of the matrix to use as our output matrix.
    #This is just a convenient way to get an output matrix of the same
    #dimensions as the original.
    new_matrix = copy.deepcopy(img_matrix)

    #Loops through every pixel we need to compute via (x, y) coordinates
    for y in range(height):
        for x in range(width):

            #To compute each pixel, for each of the three color components
            #take the average of that component for the surrounding 9 pixels
            new_pixel = [0, 0, 0]
            for j in range(-1,2):  #Loop through y-1, y, y+1
                for i in range(-1,2):  #Loop through x-1, x, x+1
                    for color in range(3):
                        #If x+i or y+j is out of bounds, ignore it
                        if 0 <= x+i < width and 0 <= y+j < height:
                            new_pixel[color] += img_matrix[y+j][x+i][color]/9

            #Averaging might result in a float, so truncate down to nearest int
            for color in range(3):
                new_pixel[color] = int(new_pixel[color])

            #Replace pixel in output matrix
            new_matrix[y][x] = new_pixel
    return new_matrix



#--------------------------------------------------
# DO NOT EDIT ANYTHING BELOW THIS LINE
# .bmp file manipulation functions.  You don't have to understand these.
#--------------------------------------------------

def big_end_to_int(ls):
    '''
    Byte conversion helper 
    Purpose:
      Compute the integer represented by a sequence of bytes
    Input Parameter(s):
      A list of bytes (integers between 0 and 255), in big-endian order
    Return Value:
      Integer value that the bytes represent
    '''
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

def transform_image(fname,operation):
    '''
    .bmp conversion function
    Purpose:
      Turns a .bmp file into a matrix of pixel values, performs an operation
      on it, and then converts it back into a new .bmp file
    Input Parameter(s):
      fname, a string representing a file name in the current directory
      operation, a string representing the operation to be performed on the
      image. 
    Return Value:
      None
    '''
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [red,green,blue].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i+2],data[i+1],data[i]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()

    #Perform operation on the pixel matrix
    if operation == 'invert':
        new_matrix = invert(matrix[::-1])
    elif operation == 'high_contrast':
        new_matrix = high_contrast(matrix[::-1])
    elif operation == 'custom_filter':
        new_matrix = custom_filter(matrix[::-1])
    elif operation == 'rotate_quadrants':
        new_matrix = rotate_quadrants(matrix[::-1])
    elif operation == 'blur':
        new_matrix = blur(matrix[::-1])
    elif operation == 'swap_red_blue':
        new_matrix = swap_red_blue(matrix[::-1])
    else:
        return
    new_matrix = new_matrix[::-1]
    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i+2],data[i+1],data[i] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()
