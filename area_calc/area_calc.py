def paint_calc(height, width, cover):
  return print(round((int(height)*int(width))/cover))

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
