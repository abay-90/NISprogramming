def generate_letter():
    current = 97
    while True:
        yield chr(current)
        current += 1
        if current == 102:
            current = 97

# Alternative (longer) way to do it
# def generate_letter():
#     current = 0
#     while True:
#         if current == 0:
#             yield 'a'
#         if current == 1:
#             yield 'b'
#         if current == 2:
#             yield 'c'
#         if current == 3:
#             yield 'd'
#         if current == 4:
#             yield 'e'
#             current = -1
#
#         current += 1


if __name__ == "__main__":
    letter_generator = generate_letter()
    for i in range(0, 10):
        print(next(letter_generator))
