from data_structures_and_algorithms.challenges.repeated_word.repeated_word import repeat_word

def test_repeat_word1():
    test = 'Once upon a time, there was a brave princess who'
    actual = repeat_word(test)
    expected = 'a'
    assert actual == expected


def test_repeat_word2():
    test = "THE WEATHER IS VERY HOT AND THE AC DOESN'T WORIt was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...K "
    actual = repeat_word(test)
    expected = 'THE'
    assert actual == expected


def test_repeat_word3():
    test = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    actual = repeat_word(test)
    expected = 'summer'
    assert actual == expected
    
def test_repeat_word4():
    test = 'we will be there on the time '
    actual = repeat_word(test)
    expected = None
    assert actual == expected
