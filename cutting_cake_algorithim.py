def max_congruent_pieces(cake_string):
    length_of_cake_string = len(cake_string)

    def repeating_substring(substring_length):
        substring = cake_string[:substring_length]
        for i in range(substring_length, length_of_cake_string, substring_length):
            if cake_string[i: i + substring_length] != substring:
                return False 
        return True  
    
    max_pieces = 1

    for substring_length in range(1, length_of_cake_string +1 ):
       if length_of_cake_string % substring_length == 0:
            if repeating_substring(substring_length):
                max_pieces = max(max_pieces, length_of_cake_string // substring_length)
    print(max_pieces)

max_congruent_pieces("abcdabcdabcdabcd")