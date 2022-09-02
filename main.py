from os.path import exists
from pygame import mixer
import time

alphabetic_morse_dict = {
    'a': '. _',
    'b': '_ . . .',
    'c': '_ . _.',
    'd': '_ . .',
    'e': '.',
    'f': '. . _ .',
    'g': '_ _ .',
    'h': '. . . .',
    'i': '. .',
    'j': '. _ _ _',
    'k': '_ . _',
    'l': '. _ . .',
    'm': '_ _',
    'n': '_.',
    'o': '_ _ _',
    'p': '. _ _ .',
    'q': '_ _ . _',
    'r': '. _ .',
    's': '. . .',
    't': '_',
    'u': '. . _',
    'v': '. . . _',
    'w': '. _ _',
    'x': '_ . . _',
    'y': '_ . _ _',
    'z': '_ _ . .'
}
alphabetic_morse_sound_dict = {
    'a': './sounds/sounds_morse_letter_a.mp3',
    'b': './sounds/sounds_morse_letter_b.mp3',
    'c': './sounds/sounds_morse_letter_c.mp3',
    'd': './sounds/sounds_morse_letter_d.mp3',
    'e': './sounds/sounds_morse_letter_e.mp3',
    'f': './sounds/sounds_morse_letter_f.mp3',
    'g': './sounds/sounds_morse_letter_g.mp3',
    'h': './sounds/sounds_morse_letter_h.mp3',
    'i': './sounds/sounds_morse_letter_i.mp3',
    'j': './sounds/sounds_morse_letter_j.mp3',
    'k': './sounds/sounds_morse_letter_k.mp3',
    'l': './sounds/sounds_morse_letter_l.mp3',
    'm': './sounds/sounds_morse_letter_m.mp3',
    'n': './sounds/sounds_morse_letter_n.mp3',
    'o': './sounds/sounds_morse_letter_o.mp3',
    'p': './sounds/sounds_morse_letter_p.mp3',
    'q': './sounds/sounds_morse_letter_q.mp3',
    'r': './sounds/sounds_morse_letter_r.mp3',
    's': './sounds/sounds_morse_letter_s.mp3',
    't': './sounds/sounds_morse_letter_t.mp3',
    'u': './sounds/sounds_morse_letter_u.mp3',
    'v': './sounds/sounds_morse_letter_v.mp3',
    'w': './sounds/sounds_morse_letter_w.mp3',
    'x': './sounds/sounds_morse_letter_x.mp3',
    'y': './sounds/sounds_morse_letter_y.mp3',
    'z': './sounds/sounds_morse_letter_z.mp3',
}
punctuation_morse_dict = {
    ',': '_ _ . . _ _',
    '?': '. . _ _ . .',
    ':': '_ _ _ . . .',
    '-': '_ . . . . _',
    '"': '· −· · −·',
    '--': '−· · · −',
    '.': '. _ . _. _',
    ';': '_ . _ . _ .',
    '/': '_ . . _.',
    "'": '. _ _ _ _.',
    '$': '···−··−',
    '+': '. _ . _.',
    '@': '·−−·−·',
    '_': '··−−·−'
}

punctuation_morse_sound_dict = {
    ',': './sounds/sounds_morse_punctuation_comma.mp3',
    '?': './sounds/sounds_morse_punctuation_question_mark.mp3',
    ':': './sounds/sounds_morse_punctuation_colon.mp3',
    '-': './sounds/sounds_morse_punctuation_dash.mp3',
    '"': './sounds/sounds_morse_punctuation_quotation_mark.mp3',
    '--': './sounds/sounds_morse_punctuation_double_dash.mp3',
    '.': './sounds/sounds_morse_punctuation_period.mp3',
    ';': './sounds/sounds_morse_punctuation_semicolon.mp3',
    '/': './sounds/sounds_morse_punctuation_slash.mp3',
    "'": './sounds/sounds_morse_punctuation_single_quote.mp3',
    '$': './sounds/sounds_morse_punctuation_dollar_sign.mp3',
    '+': './sounds/sounds_morse_punctuation_plus_sign.mp3',
    '@': './sounds/sounds_morse_punctuation_at_sign.mp3',
    '_': './sounds/sounds_morse_punctuation_underscore.mp3'
}

number_morse_dict = {
    '1': '. _ _ _ _',
    '2': '. . _ _ _',
    '3': '. . . _ _',
    '4': '. . . . _',
    '5': '. . . . .',
    '6': '_ . . . .',
    '7': '_ _ . . .',
    '8': '_ _ _ . .',
    '9': '_ _ _ _ .',
    '0': '_ _ _ _ _'
}

number_morse_sound_dict = {
    '1': './sounds/sounds_morse_number_1.mp3',
    '2': './sounds/sounds_morse_number_2.mp3',
    '3': './sounds/sounds_morse_number_3.mp3',
    '4': './sounds/sounds_morse_number_4.mp3',
    '5': './sounds/sounds_morse_number_5.mp3',
    '6': './sounds/sounds_morse_number_6.mp3',
    '7': './sounds/sounds_morse_number_7.mp3',
    '8': './sounds/sounds_morse_number_8.mp3',
    '9': './sounds/sounds_morse_number_9.mp3',
    '0': './sounds/sounds_morse_number_0.mp3'
}

space_between_letters_dict = {'space_letter': '   '}
space_between_letters_sound_dict = {'space_letter': './sounds/sounds_morse_letter_space.mp3'}
space_between_words_dict = {'space_word': '       '}
space_between_words_sound_dict = {'space_word': './sounds/sounds_morse_word_space.mp3'}
new_line_dict = {'\n': '\n'}
new_line_sound_dict = {'\n': './sounds/sounds_morse_new_line.mp3'}


def normal_to_morse(regular):
    morse_list = []
    if regular:
        for i in regular:
            if i in alphabetic_morse_dict:
                morse_list.append(alphabetic_morse_dict[i])
                morse_list.append(space_between_letters_dict['space_letter'])
            if i in punctuation_morse_dict:
                morse_list.append(punctuation_morse_dict[i])
                morse_list.append(space_between_letters_dict['space_letter'])
            if i in number_morse_dict:
                morse_list.append(number_morse_dict[i])
                morse_list.append(space_between_letters_dict['space_letter'])
            if i.isspace():
                morse_list.append(space_between_words_dict['space_word'])
            if i in new_line_dict:
                morse_list.append(new_line_dict[i])
    return morse_list


def normal_to_morse_sounds(regular):
    morse_sound_list = []
    j_count = 0
    space_on = False
    if regular:
        for j in regular:
            if j_count < 1:
                pass
            else:
                if j.isspace():
                    pass
                else:
                    if space_on is True:
                        pass
                    else:
                        morse_sound_list.append(space_between_letters_sound_dict['space_letter'])
            if j.isspace():
                morse_sound_list.append(space_between_words_sound_dict['space_word'])
                space_on = True
            else:
                if j in alphabetic_morse_sound_dict:
                    morse_sound_list.append(alphabetic_morse_sound_dict[j])
                    space_on = False
                elif j in punctuation_morse_sound_dict:
                    morse_sound_list.append(punctuation_morse_sound_dict[j])
                    space_on = False
                elif j in number_morse_sound_dict:
                    morse_sound_list.append(number_morse_sound_dict[j])
                    space_on = False
                if j in new_line_sound_dict:
                    morse_sound_list.append(new_line_sound_dict[j])
                    space_on = False
            j_count += 1
        return morse_sound_list


data = exists('./documents.txt')
if data:
    with open('documents.txt', encoding='utf-8') as file:
        new_data = file.read()
more_result = normal_to_morse(regular=new_data)
print(''.join(more_result))
user_input = input('Do you want to play morse code sound?  Type "y" for yes and "n" for no:  ')
if user_input == 'y':
    play_morse = normal_to_morse_sounds(regular=new_data)
    for k in play_morse:
        mixer.init()
        mixer.music.load(k)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)