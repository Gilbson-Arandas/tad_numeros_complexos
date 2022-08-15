class ComplexNumbers:
    @classmethod
    def Create(self, a, b):
        x = a
        y = b
        return complex(x, y)

    def Show(a):
        x = a
        print('A combinação', x, 'é do tipo', type(x))
        print('O valor', x.real, 'é a parte Real')
        print('O valor', x.imag, 'é a parte Imaginária\n')

    def Sum(a, b, c):
        print('A soma dos valores', a, '+', b, '+', c, '=', a + b + c, '\n')

    def Sub(a, b, c):
        print('A subtração dos valores', a, '-',
              b, '-', c, '=', a - b - c, '\n')

    def Mult(a, b, c):
        print('A Múltiplicação dos valores', a,
              'x', b, 'x', c, '=', a * b * c, '\n')

    def Div(a, b, c):
        print('A Divisão dos valores', a, '÷', b, '÷', c, '=', a / b / c, '\n')


first = ComplexNumbers.Create(7, 3)
second = ComplexNumbers.Create(3, 4)
third = ComplexNumbers.Create(5, 2)

ComplexNumbers.Show(first)
ComplexNumbers.Show(second)
ComplexNumbers.Show(third)

ComplexNumbers.Sum(first, second, third)
ComplexNumbers.Sub(first, second, third)
ComplexNumbers.Mult(first, second, third)
ComplexNumbers.Div(first, second, third)
