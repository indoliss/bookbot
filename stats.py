   
def counting_words(text):
    num_words=0
    words=text.split()
    for words in words:
        num_words+=1
    return print(f"Found {num_words} total words")


def sort_on(dict_item):
    return dict_item["count"]

def sorted_letters(letters_unsorted):
    sorted_list=[]
    
    for key , count in letters_unsorted.items():
        sorted_list.append({"char":key,"count":count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



def counting_letter(text):
    characters_count={}
    text=text.lower()
    
    for letters in text:
        if letters not in characters_count:
            characters_count[letters] = 1
        else:
            characters_count[letters]+=1
    return characters_count