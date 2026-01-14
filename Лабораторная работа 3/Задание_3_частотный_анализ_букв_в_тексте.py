from collections import Counter

def count_letters(text):
    text = text.lower()
    letters = [char for char in text if char.isalpha()]
    return dict(Counter(letters))

def calculate_frequency(letter_counts):
    total = sum(letter_counts.values())
    if total == 0:
        return {}
    return {letter: count / total for letter, count in letter_counts.items()}

if __name__ == "__main__":
    text = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

    letter_counts = count_letters(text)
    letter_frequency = calculate_frequency(letter_counts)

    seen = set()
    letters_order = []
    for char in text.lower():
        if char.isalpha() and char not in seen:
            seen.add(char)
            letters_order.append(char)

    for letter in letters_order:
        print(f"{letter}: {letter_frequency.get(letter, 0):.2f}")