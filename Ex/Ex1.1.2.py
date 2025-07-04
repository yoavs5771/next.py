def plus_ch(ch):
    return ch * 2

def double_letter(my_str):
        return "".join(map(plus_ch, list(my_str)))