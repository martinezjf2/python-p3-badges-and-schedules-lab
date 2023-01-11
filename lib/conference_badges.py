def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # sentences = []
    # for name in names:
    #    sentence =  badge_maker(name)
    #    sentences.append(sentence)
    # return sentences
    sentences = [badge_maker(name) for name in names]
    return sentences

def assign_rooms(names):
    # sentences = []
    # index = 1
    # for name in names:
    #     sentence = f"Hello, {name}! You'll be assigned to room {index}!"
    #     sentences.append(sentence)
    #     index += 1
    # return sentences
   
    sentences = [i + 1 and f"Hello, {name}! You'll be assigned to room {i + 1}!" for (i, name) in enumerate(names)]
    return sentences

# Resource for the List Comprehension: https://tutorial.eyehunts.com/python/python-list-comprehension-multiple-variables-example-code/

def printer(names):

    for sentence in batch_badge_creator(names):
        print(sentence)

    for sentence in assign_rooms(names):
        print(sentence)
    


#Try using List Comprehensions for the last three methods
