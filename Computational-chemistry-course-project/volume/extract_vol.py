def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def extrct_vol_from_output(inp):
    with open(inp+".out") as f:
        lines = f.readlines()
    words = ["Oops"]
    for line in lines:
        if "cm**3/mol" in line:
            words = line.split(" ")
    vol = words[words.index("cm**3/mol)\n")-1]
    if vol[0]=="(":
        vol = vol[1:]
    assert is_number(vol), "Volume was not found:" + str(vol)
    vol = float(vol)

    return vol

