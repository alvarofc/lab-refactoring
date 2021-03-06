# All characters accepted
options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'ç', 'ñ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç', 'Ñ',
           ' ,', '.', ' ']

# Rotors aka Dictionaries to encrypt.
a1 = {'a': 'z', 'b': 'k', 'c': 'L', 'd': 'M', 'e': '3', 'f': 'T', 'g': 'P', 'h': 'u', 'i': '7', 'j': 'Ç', 'k': 'r',
      'l': 'Q', 'm': 'O', 'n': 'Ñ', 'o': '.', 'p': 'n', 'q': '8', 's': 'f', 't': 'V', 'u': 'b', 'v': 'W', 'w': 'p',
      'x': 'Z', 'y': 'I', '1': '2', '2': 't', '4': 'D', '5': 'y', '7': 'e', '8': 'C', '0': ',', 'A': 'd', 'C': '6',
      'E': '0', 'F': 'q', 'G': 'j', 'L': 'g', 'Q': 'E', 'R': 'K', 'S': 'w', 'T': 'v', 'V': 'B', ',': 'A', '.': 's',
      ' ': 'c', 'r': 'S', 'ç': '4', 'H': 'ç', 'ñ': 'i', '9': 'F', 'D': 'J', 'U': 'l', 'Ç': '9', '3': 'Y', 'B': 'H',
      'I': 'G', 'J': 'x', 'O': '5', 'P': 'R', 'Z': 'm', 'Ñ': '1', 'z': ' ', 'W': 'ñ', 'Y': 'h', 'K': 'X', 'M': 'a',
      '6': 'U', 'X': 'o'}
a2 = {'a': 'J', 'b': '2', 'c': 'W', 'd': 'b', 'e': 'w', 'f': '3', 'g': 'v', 'h': 'ñ', 'i': 'q', 'j': 'S', 'k': 'j',
      'o': 'c', 'r': 'P', 's': '0', 'u': 'U', 'w': '.', 'x': 'L', 'y': 'o', 'z': 'D', 'ç': ' ', '2': 'G', '3': 'n',
      '4': 'h', '8': 'ç', '9': 's', 'A': '6', 'B': 'V', 'D': 't', 'E': 'Z', 'F': 'Y', 'H': '5', 'I': 'O', 'J': 'p',
      'K': 'r', 'L': 'X', 'M': 'Ñ', 'T': '8', 'V': 'i', 'Y': 'M', 'm': 'B', 'n': 'R', 'p': 'y', 'ñ': 'd', '5': 'T',
      '6': ',', '7': 'a', '0': 'x', 'C': 'H', 'X': '7', 'Ñ': 'k', '.': '1', ' ': 'f', '1': 'g', 'P': 'e', 'S': 'F',
      'U': 'z', 'W': 'Ç', 'l': 'l', 'Q': 'Q', 'Z': '4', ',': 'K', 'q': 'm', 'v': '9', 'G': 'C', 'Ç': 'I', 't': 'E',
      'O': 'A', 'R': 'u'}
a3 = {'a': 'q', 'b': '1', 'c': 'r', 'd': 'Q', 'e': 'F', 'f': '8', 'g': 'U', 'h': '0', 'i': 'j', 'l': 'l', 'm': 'X',
      'n': 'f', 'p': 'I', 'q': 'c', 't': 'W', 'u': 'Y', 'v': 'v', 'w': '3', 'y': 'u', 'z': ',', 'ç': 'i', 'ñ': 'w',
      '2': 'P', '3': 'h', '4': ' ', '6': '9', '8': 'o', '9': 'S', '0': 'e', 'D': 'T', 'E': '.', 'G': 'z', 'H': 'd',
      'L': 't', 'M': 'k', 'O': 'O', 'P': 'K', 'R': 'ñ', 'U': 'H', 'W': 'B', 'X': 'Ç', 'Z': '4', 'Ñ': 'E', 'k': 'M',
      'r': 'A', 'x': 'C', '5': 'R', '7': 'V', 'C': 'J', 'F': 'Z', 'J': 'Ñ', 'S': 'y', 'T': 'D', ' ': '7', '1': 'a',
      'A': 'ç', 's': 'g', 'B': 'L', 'V': '6', 'Q': 'G', 'o': '5', 'I': 'x', '.': 'b', 'j': 'p', ',': 'n', 'Ç': 'm',
      'K': 's', 'Y': '2'}
b1 = {'a': ',', 'b': 's', 'c': 'Q', 'd': 'p', 'e': 'L', 'f': 'H', 'g': 'r', 'h': ' ', 'i': 'M', 'j': 'K', 'k': 'I',
      'l': 'v', 'm': 'n', 'n': 'j', 'o': 'f', 's': '.', 't': 'V', 'u': 'B', 'v': 'u', 'x': 'W', 'y': 'a', 'z': '3',
      'ñ': 'S', '1': 'J', '2': 'e', '3': 'h', '4': 'x', '5': '9', '6': 'G', '8': 'C', '9': 'A', '0': 'ç', 'F': '8',
      'G': 'E', 'J': 'R', 'O': '5', 'Ç': '2', 'Ñ': 'P', ',': 'g', 'p': 'l', 'w': 'Z', '7': 'T', 'B': 'w', 'C': 'X',
      'D': 'd', 'E': 'q', 'H': 'F', 'K': 'b', 'M': 'o', 'W': 'm', 'X': '4', 'Z': 'Ç', 'q': 'D', 'A': '6', 'Y': 'i',
      'ç': '0', 'L': 'O', 'R': '1', 'r': 'ñ', 'P': 't', 'I': 'y', ' ': 'U', 'Q': 'Y', 'S': 'k', 'V': 'Ñ', 'T': 'z',
      'U': '7', '.': 'c'}
b2 = {'a': 'z', 'b': 'W', 'c': 'D', 'd': 'x', 'e': 'F', 'f': '8', 'g': 'J', 'h': ',', 'i': '0', 'j': 'C', 'k': 'p',
      'l': 'K', 'n': 'ñ', 'o': '2', 'p': 'e', 'q': 'V', 'r': 'P', 'w': '5', 'x': '7', 'z': '.', 'ç': 'r', 'ñ': '1',
      '1': 'I', '2': 'Ç', '3': ' ', '4': 'l', '6': 'k', '7': 'd', 'A': 'S', 'B': 'T', 'C': 'h', 'D': 'i', 'E': 'm',
      'K': 'a', 'O': 'n', 'T': '3', 'U': 'b', 'X': 'j', 'Y': 'ç', 'Ñ': 'g', ' ': 'w', '9': '6', '0': 'Q', 'H': 'A',
      'L': 'u', 'M': 's', 'S': 'Y', 'Ç': 'f', 'm': 'O', 'v': 't', 'I': 'E', 'P': 'c', 'Q': 'G', '8': 'v', 'W': '9',
      'u': 'M', ',': 'H', 'F': 'q', 'Z': 'L', '.': 'Ñ', 'G': 'U', 'V': 'R', '5': 'Z', 'y': 'X', 's': 'B', 't': '4',
      'R': 'y', 'J': 'o'}
b3 = {'a': 'g', 'b': 'D', 'c': 'Z', 'd': 'c', 'e': 'H', 'f': 'j', 'g': 'f', 'h': 'K', 'j': 'x', 'k': 'F', 'l': 'O',
      'm': 'l', 'n': 'G', 'o': '8', 'p': ',', 'q': 'M', 'r': 'n', 's': '1', 't': 'ç', 'u': 'Y', 'v': 'ñ', 'w': 'e',
      'x': '3', 'y': 'h', 'z': 'R', 'ç': 'Q', 'ñ': 'B', '1': '0', '2': ' ', '5': '7', '7': '4', '8': 'm', 'C': 'P',
      'D': 'W', 'G': 'U', 'I': 'L', 'J': 'J', 'L': 'p', 'M': 'A', 'U': 's', 'W': 'w', 'Y': 'S', '.': '6', ' ': 'C',
      'i': 'o', '6': 'u', '0': 'y', 'B': 'i', 'F': 't', 'P': 'I', 'T': 'a', 'Q': 'd', 'S': 'V', '3': '.', 'K': 'Ç',
      'O': '5', 'X': 'T', 'A': 'k', 'Ç': 'r', 'Ñ': 'Ñ', 'V': 'b', 'Z': 'z', 'R': '2', '9': 'v', '4': 'X', 'E': 'q',
      ',': 'E', 'H': '9'}
c1 = {'a': 'w', 'b': 'q', 'c': 'W', 'd': '9', 'e': '7', 'f': '3', 'g': 'H', 'h': 'j', 'i': 'B', 'j': 'r', 'k': 'y',
      'l': 'R', 'm': '0', 'n': 'a', 'o': 'e', 'r': 'ç', 's': '2', 't': 'l', 'u': 'Y', 'x': 'ñ', 'y': 'Q', 'z': 'b',
      'ç': 'S', 'ñ': 'E', '1': 'O', '2': 'h', '3': 'Z', '4': 'T', '6': '8', '7': 'd', 'A': 'K', 'E': 'z', 'F': '5',
      'H': 'V', 'K': 'x', 'M': 'D', 'P': 'G', 'S': 'X', 'T': 'i', 'V': 'u', 'Y': ',', 'Z': '.', 'Ç': 'P', '.': 'Ç',
      'p': 'k', 'v': '6', '9': 'A', 'J': '1', 'O': 'Ñ', 'U': 'n', '0': 'f', 'I': 'g', '5': 'o', 'C': 'F', 'L': 's',
      'Q': ' ', 'W': 'm', ',': '4', 'w': 'J', '8': 'p', 'D': 't', 'q': 'M', ' ': 'c', 'R': 'C', 'G': 'I', 'Ñ': 'U',
      'X': 'v', 'B': 'L'}
c2 = {'a': 'ñ', 'b': 'n', 'c': 'l', 'd': 'M', 'e': 'r', 'f': 'Ç', 'g': 'D', 'h': 'J', 'j': 'F', 'k': 'S', 'l': 'q',
      'm': '0', 'n': '2', 'p': 'v', 'q': 's', 'r': 'o', 's': 'C', 't': 'P', 'u': 'R', 'x': '5', 'y': 'Q', 'z': 'E',
      '4': '4', '5': 'Ñ', '7': 'u', '8': ' ', '9': 'W', 'A': 'A', 'B': 't', 'C': 'f', 'D': 'h', 'E': 'B', 'I': '6',
      'K': ',', 'M': '9', 'Q': '8', 'R': 'g', 'V': 'b', 'X': 'O', 'Z': 'z', 'Ñ': 'e', ' ': 'K', 'o': 'ç', 'w': 'k',
      'ñ': 'a', '3': 'T', '6': 'm', 'G': 'j', 'L': 'V', 'S': 'X', 'W': '7', 'Ç': 'd', ',': '.', '0': 'c', 'F': 'L',
      'U': 'G', 'i': 'w', 'v': 'x', 'ç': 'Y', '1': 'H', 'P': 'Z', 'H': 'i', '.': '3', 'T': 'I', 'J': 'p', 'Y': 'y',
      '2': '1', 'O': 'U'}
c3 = {'a': '7', 'b': 'A', 'c': '1', 'd': 'T', 'e': 's', 'f': 'Z', 'g': 'q', 'h': 'r', 'i': 'z', 'j': 'l', 'k': 'n',
      'l': 'ç', 'm': 'V', 'n': 'a', 'p': 'F', 'r': 'c', 's': 'd', 't': 'b', 'u': '0', 'v': 'D', 'x': 'x', 'z': 'G',
      'ñ': 'g', '1': 'Y', '2': 'X', '3': '4', '4': 'f', '5': '3', '6': 'H', '7': 'J', '8': '2', 'C': 'j', 'D': 'I',
      'G': 'L', 'H': '.', 'I': '9', 'J': 'y', 'K': 'p', 'P': 'e', 'Q': 'h', 'T': 'O', 'Z': 'w', 'Ñ': 'K', ',': '6',
      '.': 'o', 'y': 'Ç', '0': 'Ñ', 'E': 'k', 'S': 'M', 'U': '8', 'X': ',', 'M': ' ', 'O': '5', 'W': 't', 'q': 'B',
      'w': 'Q', 'V': 'm', 'Ç': 'U', 'ç': 'E', '9': 'i', ' ': 'S', 'o': 'W', 'F': 'P', 'A': 'C', 'B': 'v', 'R': 'R',
      'L': 'u', 'Y': 'ñ'}

# Rotors (dictionaries) to decrypt

in_a1 = {'z': 'a', 'k': 'b', 'L': 'c', 'M': 'd', '3': 'e', 'T': 'f', 'P': 'g', 'u': 'h', '7': 'i', 'Ç': 'j', 'r': 'k',
         'Q': 'l', 'O': 'm', 'Ñ': 'n', '.': 'o', 'n': 'p', '8': 'q', 'f': 's', 'V': 't', 'b': 'u', 'W': 'v', 'p': 'w',
         'Z': 'x', 'I': 'y', '2': '1', 't': '2', 'D': '4', 'y': '5', 'e': '7', 'C': '8', ',': '0', 'd': 'A', '6': 'C',
         '0': 'E', 'q': 'F', 'j': 'G', 'g': 'L', 'E': 'Q', 'K': 'R', 'w': 'S', 'v': 'T', 'B': 'V', 'A': ',', 's': '.',
         'c': ' ', 'S': 'r', '4': 'ç', 'ç': 'H', 'i': 'ñ', 'F': '9', 'J': 'D', 'l': 'U', '9': 'Ç', 'Y': '3', 'H': 'B',
         'G': 'I', 'x': 'J', '5': 'O', 'R': 'P', 'm': 'Z', '1': 'Ñ', ' ': 'z', 'ñ': 'W', 'h': 'Y', 'X': 'K', 'a': 'M',
         'U': '6', 'o': 'X'}
in_a2 = {'J': 'a', '2': 'b', 'W': 'c', 'b': 'd', 'w': 'e', '3': 'f', 'v': 'g', 'ñ': 'h', 'q': 'i', 'S': 'j', 'j': 'k',
         'c': 'o', 'P': 'r', '0': 's', 'U': 'u', '.': 'w', 'L': 'x', 'o': 'y', 'D': 'z', ' ': 'ç', 'G': '2', 'n': '3',
         'h': '4', 'ç': '8', 's': '9', '6': 'A', 'V': 'B', 't': 'D', 'Z': 'E', 'Y': 'F', '5': 'H', 'O': 'I', 'p': 'J',
         'r': 'K', 'X': 'L', 'Ñ': 'M', '8': 'T', 'i': 'V', 'M': 'Y', 'B': 'm', 'R': 'n', 'y': 'p', 'd': 'ñ', 'T': '5',
         ',': '6', 'a': '7', 'x': '0', 'H': 'C', '7': 'X', 'k': 'Ñ', '1': '.', 'f': ' ', 'g': '1', 'e': 'P', 'F': 'S',
         'z': 'U', 'Ç': 'W', 'l': 'l', 'Q': 'Q', '4': 'Z', 'K': ',', 'm': 'q', '9': 'v', 'C': 'G', 'I': 'Ç', 'E': 't',
         'A': 'O', 'u': 'R'}
in_a3 = {'q': 'a', '1': 'b', 'r': 'c', 'Q': 'd', 'F': 'e', '8': 'f', 'U': 'g', '0': 'h', 'j': 'i', 'l': 'l', 'X': 'm',
         'f': 'n', 'I': 'p', 'c': 'q', 'W': 't', 'Y': 'u', 'v': 'v', '3': 'w', 'u': 'y', ',': 'z', 'i': 'ç', 'w': 'ñ',
         'P': '2', 'h': '3', ' ': '4', '9': '6', 'o': '8', 'S': '9', 'e': '0', 'T': 'D', '.': 'E', 'z': 'G', 'd': 'H',
         't': 'L', 'k': 'M', 'O': 'O', 'K': 'P', 'ñ': 'R', 'H': 'U', 'B': 'W', 'Ç': 'X', '4': 'Z', 'E': 'Ñ', 'M': 'k',
         'A': 'r', 'C': 'x', 'R': '5', 'V': '7', 'J': 'C', 'Z': 'F', 'Ñ': 'J', 'y': 'S', 'D': 'T', '7': ' ', 'a': '1',
         'ç': 'A', 'g': 's', 'L': 'B', '6': 'V', 'G': 'Q', '5': 'o', 'x': 'I', 'b': '.', 'p': 'j', 'n': ',', 'm': 'Ç',
         's': 'K', '2': 'Y'}
in_b1 = {',': 'a', 's': 'b', 'Q': 'c', 'p': 'd', 'L': 'e', 'H': 'f', 'r': 'g', ' ': 'h', 'M': 'i', 'K': 'j', 'I': 'k',
         'v': 'l', 'n': 'm', 'j': 'n', 'f': 'o', '.': 's', 'V': 't', 'B': 'u', 'u': 'v', 'W': 'x', 'a': 'y', '3': 'z',
         'S': 'ñ', 'J': '1', 'e': '2', 'h': '3', 'x': '4', '9': '5', 'G': '6', 'C': '8', 'A': '9', 'ç': '0', '8': 'F',
         'E': 'G', 'R': 'J', '5': 'O', '2': 'Ç', 'P': 'Ñ', 'g': ',', 'l': 'p', 'Z': 'w', 'T': '7', 'w': 'B', 'X': 'C',
         'd': 'D', 'q': 'E', 'F': 'H', 'b': 'K', 'o': 'M', 'm': 'W', '4': 'X', 'Ç': 'Z', 'D': 'q', '6': 'A', 'i': 'Y',
         '0': 'ç', 'O': 'L', '1': 'R', 'ñ': 'r', 't': 'P', 'y': 'I', 'U': ' ', 'Y': 'Q', 'k': 'S', 'Ñ': 'V', 'z': 'T',
         '7': 'U', 'c': '.'}
in_b2 = {'z': 'a', 'W': 'b', 'D': 'c', 'x': 'd', 'F': 'e', '8': 'f', 'J': 'g', ',': 'h', '0': 'i', 'C': 'j', 'p': 'k',
         'K': 'l', 'ñ': 'n', '2': 'o', 'e': 'p', 'V': 'q', 'P': 'r', '5': 'w', '7': 'x', '.': 'z', 'r': 'ç', '1': 'ñ',
         'I': '1', 'Ç': '2', ' ': '3', 'l': '4', 'k': '6', 'd': '7', 'S': 'A', 'T': 'B', 'h': 'C', 'i': 'D', 'm': 'E',
         'a': 'K', 'n': 'O', '3': 'T', 'b': 'U', 'j': 'X', 'ç': 'Y', 'g': 'Ñ', 'w': ' ', '6': '9', 'Q': '0', 'A': 'H',
         'u': 'L', 's': 'M', 'Y': 'S', 'f': 'Ç', 'O': 'm', 't': 'v', 'E': 'I', 'c': 'P', 'G': 'Q', 'v': '8', '9': 'W',
         'M': 'u', 'H': ',', 'q': 'F', 'L': 'Z', 'Ñ': '.', 'U': 'G', 'R': 'V', 'Z': '5', 'X': 'y', 'B': 's', '4': 't',
         'y': 'R', 'o': 'J'}
in_b3 = {'g': 'a', 'D': 'b', 'Z': 'c', 'c': 'd', 'H': 'e', 'j': 'f', 'f': 'g', 'K': 'h', 'x': 'j', 'F': 'k', 'O': 'l',
         'l': 'm', 'G': 'n', '8': 'o', ',': 'p', 'M': 'q', 'n': 'r', '1': 's', 'ç': 't', 'Y': 'u', 'ñ': 'v', 'e': 'w',
         '3': 'x', 'h': 'y', 'R': 'z', 'Q': 'ç', 'B': 'ñ', '0': '1', ' ': '2', '7': '5', '4': '7', 'm': '8', 'P': 'C',
         'W': 'D', 'U': 'G', 'L': 'I', 'J': 'J', 'p': 'L', 'A': 'M', 's': 'U', 'w': 'W', 'S': 'Y', '6': '.', 'C': ' ',
         'o': 'i', 'u': '6', 'y': '0', 'i': 'B', 't': 'F', 'I': 'P', 'a': 'T', 'd': 'Q', 'V': 'S', '.': '3', 'Ç': 'K',
         '5': 'O', 'T': 'X', 'k': 'A', 'r': 'Ç', 'Ñ': 'Ñ', 'b': 'V', 'z': 'Z', '2': 'R', 'v': '9', 'X': '4', 'q': 'E',
         'E': ',', '9': 'H'}
in_c1 = {'w': 'a', 'q': 'b', 'W': 'c', '9': 'd', '7': 'e', '3': 'f', 'H': 'g', 'j': 'h', 'B': 'i', 'r': 'j', 'y': 'k',
         'R': 'l', '0': 'm', 'a': 'n', 'e': 'o', 'ç': 'r', '2': 's', 'l': 't', 'Y': 'u', 'ñ': 'x', 'Q': 'y', 'b': 'z',
         'S': 'ç', 'E': 'ñ', 'O': '1', 'h': '2', 'Z': '3', 'T': '4', '8': '6', 'd': '7', 'K': 'A', 'z': 'E', '5': 'F',
         'V': 'H', 'x': 'K', 'D': 'M', 'G': 'P', 'X': 'S', 'i': 'T', 'u': 'V', ',': 'Y', '.': 'Z', 'P': 'Ç', 'Ç': '.',
         'k': 'p', '6': 'v', 'A': '9', '1': 'J', 'Ñ': 'O', 'n': 'U', 'f': '0', 'g': 'I', 'o': '5', 'F': 'C', 's': 'L',
         ' ': 'Q', 'm': 'W', '4': ',', 'J': 'w', 'p': '8', 't': 'D', 'M': 'q', 'c': ' ', 'C': 'R', 'I': 'G', 'U': 'Ñ',
         'v': 'X', 'L': 'B'}
in_c2 = {'ñ': 'a', 'n': 'b', 'l': 'c', 'M': 'd', 'r': 'e', 'Ç': 'f', 'D': 'g', 'J': 'h', 'F': 'j', 'S': 'k', 'q': 'l',
         '0': 'm', '2': 'n', 'v': 'p', 's': 'q', 'o': 'r', 'C': 's', 'P': 't', 'R': 'u', '5': 'x', 'Q': 'y', 'E': 'z',
         '4': '4', 'Ñ': '5', 'u': '7', ' ': '8', 'W': '9', 'A': 'A', 't': 'B', 'f': 'C', 'h': 'D', 'B': 'E', '6': 'I',
         ',': 'K', '9': 'M', '8': 'Q', 'g': 'R', 'b': 'V', 'O': 'X', 'z': 'Z', 'e': 'Ñ', 'K': ' ', 'ç': 'o', 'k': 'w',
         'a': 'ñ', 'T': '3', 'm': '6', 'j': 'G', 'V': 'L', 'X': 'S', '7': 'W', 'd': 'Ç', '.': ',', 'c': '0', 'L': 'F',
         'G': 'U', 'w': 'i', 'x': 'v', 'Y': 'ç', 'H': '1', 'Z': 'P', 'i': 'H', '3': '.', 'I': 'T', 'p': 'J', 'y': 'Y',
         '1': '2', 'U': 'O'}
in_c3 = {'7': 'a', 'A': 'b', '1': 'c', 'T': 'd', 's': 'e', 'Z': 'f', 'q': 'g', 'r': 'h', 'z': 'i', 'l': 'j', 'n': 'k',
         'ç': 'l', 'V': 'm', 'a': 'n', 'F': 'p', 'c': 'r', 'd': 's', 'b': 't', '0': 'u', 'D': 'v', 'x': 'x', 'G': 'z',
         'g': 'ñ', 'Y': '1', 'X': '2', '4': '3', 'f': '4', '3': '5', 'H': '6', 'J': '7', '2': '8', 'j': 'C', 'I': 'D',
         'L': 'G', '.': 'H', '9': 'I', 'y': 'J', 'p': 'K', 'e': 'P', 'h': 'Q', 'O': 'T', 'w': 'Z', 'K': 'Ñ', '6': ',',
         'o': '.', 'Ç': 'y', 'Ñ': '0', 'k': 'E', 'M': 'S', '8': 'U', ',': 'X', ' ': 'M', '5': 'O', 't': 'W', 'B': 'q',
         'Q': 'w', 'm': 'V', 'U': 'Ç', 'E': 'ç', 'i': '9', 'S': ' ', 'W': 'o', 'P': 'F', 'C': 'A', 'v': 'B', 'R': 'R',
         'u': 'L', 'ñ': 'Y'}


# Select the first Rotor
def rot1():
    """

    :return: This function returns the selection of the user for the first rotor for encryption
    """
    while True:
        rotor1 = input("Select the position of the first rotor: A/B/C :")
        if rotor1 in ['a', 'A']:
            return a1
        elif rotor1 in ['b', 'B']:
            return b1
        elif rotor1 in ['c', 'C']:
            return c1
        else:
            print("Invalid input. Choose A, B or C")


# Select the second rotor
def rot2():
    """

    :return: This function returns the selection of the user for the second rotor for encryption
    """
    while True:
        rotor2 = input("Select the position of the second rotor: A/B/C :")
        if rotor2 in ['a', 'A']:
            return a2
        elif rotor2 in ['b', 'B']:
            return b2
        elif rotor2 in ['c', 'C']:
            return c2
        else:
            print("Invalid input. Choose A, B or C")


# Select the third rotor
def rot3():
    """

    :return: This function returns the selection of the user for the third rotor for encryption
    """
    while True:
        rotor3 = input("e the position of the third rotor: A/B/C :")
        if rotor3 in ['a', 'A']:
            return a3
        elif rotor3 in ['b', 'B']:
            return b3
        elif rotor3 in ['c', 'C']:
            return c3
        else:
            print("Invalid input. Choose A, B or C")


# user inputs the message
def text():
    """

    :return:
    """
    message = input("Write your message: ")
    return message


# Encrypt the message using the selected dictionary
def crypto(msg, dictionary):
    """

    :param msg: Message for encryption or decryption
    :param dictionary: Dictionary(rotor) to use to change each character
    :return: Returns message encrypted or decrypted
    """
    comp_mes = []
    for i in msg:
        i = dictionary[i]
        comp_mes.append(i)
    return ''.join(comp_mes)


# Select first rotor
def in_rot1():
    """

    :return: This function returns the selection of the user for the first rotor for decryption
    """
    while True:
        rotor1 = input("Select the position of the first rotor: A/B/C :")
        if rotor1 in ['a', 'A']:
            return in_a1
        elif rotor1 in ['b', 'B']:
            return in_b1
        elif rotor1 in ['c', 'C']:
            return in_c1
        else:
            print("Invalid input. Choose A, B or C")


# Select second rotor
def in_rot2():
    """

    :return: This function returns the selection of the user for the second rotor for decryption
    """
    while True:
        rotor2 = input("Select the position of the second rotor: A/B/C :")
        if rotor2 in ['a', 'A']:
            return in_a2
        elif rotor2 in ['b', 'B']:
            return in_b2
        elif rotor2 in ['c', 'C']:
            return in_c2
        else:
            print("Invalid input. Choose A, B or C")


# Select the third rotor
def in_rot3():
    """

    :return: This function returns the selection of the user for the third rotor for decryption
    """
    while True:
        rotor3 = input("Select the position of the third rotor: A/B/C :")
        if rotor3 in ['a', 'A']:
            return in_a3
        elif rotor3 in ['b', 'B']:
            return in_b3
        elif rotor3 in ['c', 'C']:
            return in_c3
        else:
            print("Invalid input. Choose A, B or C")


def in_text():
    """

    :return:
    """
    in_message = input("Write your message: ")
    return in_message

