# Errors and Exceptions

x = -5
if x < 0:
    raise Exception('x should not be negative.')


x = -5
assert (x >= 0), 'x is not positive.'


try:
    a = 5 / 0
except:
    print('Error!')


try:
    a = 5 / 0
except Exception as e:
    print(e)
else:
    pass
finally:
    print('cleaning up')


# Defining
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
