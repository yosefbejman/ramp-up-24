def tallest_skyscraper(lst):
    max_height = 0
    for col in zip(*lst):
        height = sum(col)
        if height > max_height:
            max_height = height       
    return max_height