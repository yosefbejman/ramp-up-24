def reverse_string(input_str):
    vowels = 'aeiouAEIOU'
    reversed_str = input_str[::-1]
    vowel_count = sum(1 for char in reversed_str if char in vowels)
    
    print(f"Reversed String: {reversed_str}")
    print(f"Number of Vowels: {vowel_count}")
