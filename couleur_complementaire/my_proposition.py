from colorsys import rgb_to_hls, hls_to_rgb


EQUIVALENCE_HEX_DEC = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f',
]

def convert_to_rgb(hex):
    red_hex = (
        EQUIVALENCE_HEX_DEC.index(hex[1].lower()),
        EQUIVALENCE_HEX_DEC.index(hex[2].lower())
    )
    green_hex = (
        EQUIVALENCE_HEX_DEC.index(hex[3].lower()),
        EQUIVALENCE_HEX_DEC.index(hex[4].lower())
    )
    blue_hex = (
        EQUIVALENCE_HEX_DEC.index(hex[5].lower()),
        EQUIVALENCE_HEX_DEC.index(hex[6].lower())
    )

    red_decimal = red_hex[0] * 16 + red_hex[1]
    green_decimal = green_hex[0] * 16 + green_hex[1]
    blue_decimal = blue_hex[0] * 16 + blue_hex[1]

    return [red_decimal, green_decimal, blue_decimal]

def get_color_types(color:str)->dict:
    rgb = convert_to_rgb(color)

    r_index = rgb[0] / 255
    g_index = rgb[1] / 255
    b_index = rgb[2] / 255

    hls = rgb_to_hls(r_index, g_index, b_index)

    tsl_norm = (f"{round(hls[0] * 360)}Â°", f"{round(hls[2] * 100)}%", f"{round(hls[1] * 100)}%")

    tsl = (hls[0], hls[2], hls[1])

    return {'hex': color, 'rgb': rgb, 'tsl_norm': tsl_norm, 'tsl': tsl}


def get_complementary(color:str)->str:
    color_types = get_color_types(color)

    color_tint = color_types['tsl'][0] * 360
    complementary_tint = color_tint + 180 if color_tint <= 180 else color_tint - 180
    complementary_tint_indice = complementary_tint / 360

    complementary_hls = (complementary_tint_indice, color_types['tsl'][2], color_types['tsl'][1])

    complementary_rgb_indice = hls_to_rgb(*complementary_hls)

    complementary_hex = convert_to_hex(*complementary_rgb_indice)

    return complementary_hex

def convert_to_hex(r_index, g_index, b_index):
    r = r_index * 255
    g = g_index * 255
    b = b_index * 255

    r_hex_first_char = r // 16
    r_hex_second_char = ((r / 16) - (r // 16)) * 16
    r_hex = f"{EQUIVALENCE_HEX_DEC[int(round(r_hex_first_char))]}{EQUIVALENCE_HEX_DEC[int(round(r_hex_second_char))]}"

    g_hex_first_char = g // 16
    g_hex_second_char = ((g / 16) - (g // 16)) * 16
    g_hex = f"{EQUIVALENCE_HEX_DEC[int(round(g_hex_first_char))]}{EQUIVALENCE_HEX_DEC[int(round(g_hex_second_char))]}"

    b_hex_first_char = b // 16
    b_hex_second_char = ((b / 16) - (b // 16)) * 16
    b_hex = f"{EQUIVALENCE_HEX_DEC[int(round(b_hex_first_char))]}{EQUIVALENCE_HEX_DEC[int(round(b_hex_second_char))]}"

    return f"#{r_hex}{g_hex}{b_hex}"

if __name__ == "__main__":
    color = '#19021e'
    print(get_color_types(color))
    print(get_complementary(color))
