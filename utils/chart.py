from matplotlib import pyplot as plt
from wordcloud import WordCloud


def create_plot(sorted_input_data: dict):
    len_input_data = len(sorted_input_data)
    chars = list(sorted_input_data.keys())
    chars_repeated = list(sorted_input_data.values())
    plt.figure(figsize=(30, 10))
    plt.plot(chars, chars_repeated)
    plt.savefig("output/result_freq_plot.png", dpi=100)


def world_plt(input_data, word_cloud=None, word_freq=None):
    _wordcloud = WordCloud(width=500, height=500, max_font_size=200, max_words=len(input_data),
                           background_color="white")
    if word_cloud:
        _wordcloud.generate(str(input_data))
    if word_freq:
        _wordcloud.generate_from_frequencies(frequencies=input_data)
    plt.figure()
    plt.imshow(_wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
