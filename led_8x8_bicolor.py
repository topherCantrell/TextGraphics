import ascii_art


def print_images(art, mapping, code_name):
    images = ascii_art.separate_images(art)
    if len(images) == 1:
        data = ascii_art.to_pixel_array(images[0], mapping)
        d = to_8x8_bicolor(data)
        print(f'{code_name} = {d}')
    else:
        print(f'{code_name} = [')
        for im in images:
            data = ascii_art.to_pixel_array(im, mapping)
            d = to_8x8_bicolor(data)
            print('    '+str(d)+',')
        print(']')


def to_image_data(art, mapping):
    pixels = ascii_art.to_pixel_array(art, mapping)
    return to_8x8_bicolor(pixels)


def to_8x8_bicolor(pixels):
    ret = [0]*16
    for j in range(8):
        for i in range(8):
            dval = pixels[i][j]
            ret[14-j*2] |= (dval & 1) << i
            ret[14-j*2+1] |= ((dval & 2) >> 1) << i
    return ret
