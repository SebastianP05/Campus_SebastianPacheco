if __name__ == '__main__':
    n = int(input().strip())

    word_count = {}

    order_of_appearance = []

    for _ in range(n):
        word = input().strip()

        if word not in word_count:
            word_count[word] = 1
            order_of_appearance.append(word)
        else:
            word_count[word] += 1

    print(len(order_of_appearance))

    for word in order_of_appearance:
        print(word_count[word], end=' ')
    print()
    
