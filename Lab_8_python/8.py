def reverse():
    with open("8_input.dat", "rb") as in_file:
        a = in_file.read()
    with open("9_output.dat", "wb") as out_file:
        out_file.write(a[::-1])


reverse()
