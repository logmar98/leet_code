def convert_base(nbr, base):
    size = len(base)
    if nbr // size != 0:
        convert_base(nbr // size, base)
    print(base[nbr % size], end="")

convert_base(13422, "0123456789ABCDEF")
print()
convert_base(0, "0123456789ABCDEF")
print()
convert_base(13422, "01")
print()
convert_base(0, "01")
