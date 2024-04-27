import itertools

# حروف ورودی
firsts = ['گ','ن','ب','د']


# تولید کلمات
generated_words = [''.join((first, second, third, fourth))
                   for first in firsts
                   for second in firsts
                   for third in firsts
                   for fourth in firsts]

# نمایش کلمات تولید شده
for word in generated_words:
    print(word)
