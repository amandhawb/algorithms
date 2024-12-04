def capitalize_words(s):
    words = s.split(' ')
    capitalized = ''
    for word in words:
        capitalized += word.capitalize()
        capitalized += ' '
    return ''.join(capitalized)
