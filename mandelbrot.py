from PIL import Image


def converges(k, it):
    z = 0
    for i in range(0, it):
        z = z ** 2 + k

        if abs(z) >= 2:
            return True

    return False


im = Image.new('1', (10000, 7500), 'white')

data = []

for y_cor in range(3750, -3750, -1):
    print(y_cor)
    for x_cor in range(-5000, 5000):
        data.append(converges(complex(x_cor/3000 - .5, y_cor/3000), 50))

im.putdata(data)
im.save('mandelbrot.png')
im.show()
