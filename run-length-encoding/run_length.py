from itertools import groupby
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def encode(letters):
    pre_code = ["".join(grp) for num, grp in groupby(letters)]
    code = []
    for item in pre_code:
        if len(item) > 1:
            code.append(len(item))
        code.append(item[0])
    return ''.join(str(a) for a in code)


def decode(code):
    code = list(code)
    try:
        code = [''.join(g) for _, g in groupby(code, unicode.isdigit)]
    except:
        code = [''.join(g) for _, g in groupby(code, str.isdigit)]
    decoded = []
    for i, item in enumerate(code):
        if code[i].isdigit():
            decoded.append((int(code[i]) - 1) * code[i+1][0])
        else:
            decoded.append(code[i])
    return ''.join(decoded)