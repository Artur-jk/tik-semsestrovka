def bwt_decoder(encoded_word, position):
    decode_matrix = list(sorted(encoded_word))
    for _ in range(len(encoded_word) - 1):
        for i in range(len(encoded_word)):
            decode_matrix[i] = encoded_word[i] + decode_matrix[i]
        decode_matrix.sort()
    # print(*decode_matrix, sep='\n')
    # print('________________________________')
    return decode_matrix[position]

print('bwt decode ', bwt_decoder("рдакраааабб", 2))