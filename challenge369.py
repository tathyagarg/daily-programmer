def hexcolor(red: int, green: int, blue: int) -> str:
    """
    One common way for software specifications such as HTML to specify colors is with a hexadecimal string.
    For instance the color aquamarine is represented by the string "#7FFFD4". Here's how the string breaks down:

    The first character is always "#".

    The second and third character are the red channel value, represented as a hexadecimal value between 00 and FF.
    In this example, the red channel value is 127, which in hexadecimal is 7F.

    The fourth and fifth character are the green channel value, represented the same way.
    In this example, the green channel value is 255, which in hexadecimal is FF.

    The sixth and seventh character are the blue channel value, represented the same way.
    In this example, the blue channel value is 212, which in hexadecimal is D4.

    All three channel values must be an integer between 0 (minimum brightness) and 255 (maximum brightness).
    In all cases the hex values are two digits each, including a leading 0 if necessary.
    """
    hexmap = '0123456789ABCDEF'

    red_hex = ""
    while red:
        red_hex = hexmap[red % 16] + red_hex
        red //= 16

    green_hex = ""
    while green:
        green_hex = hexmap[green % 16] + green_hex
        green //= 16

    blue_hex = ""
    while blue:
        blue_hex = hexmap[blue % 16] + blue_hex
        blue //= 16

    red_hex = red_hex.rjust(2, '0')
    green_hex = green_hex.rjust(2, '0')
    blue_hex = blue_hex.rjust(2, '0')

    return '#' + red_hex + green_hex + blue_hex

assert hexcolor(255, 99, 71) == "#FF6347"
assert hexcolor(184, 134, 11) == "#B8860B"
assert hexcolor(189, 183, 107) == "#BDB76B"
assert hexcolor(0, 0, 205) == "#0000CD"
