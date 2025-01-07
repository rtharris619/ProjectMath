from IPython.display import display, Math

def exercises():
  x = 7
  y = -2
  z = 5

  ans = 3 * x * (4 + y)
  print(ans)

  ans = -y - ((x + 3) / z)
  print(ans)


def print_equations():
  display( '4 + 3 = 7' )
  display( '4 + 3 = ' + str(4+3) )

  display(Math('4+3=7'))
  

def driver():
  print_equations()
