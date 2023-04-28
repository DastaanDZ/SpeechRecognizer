def read_file(filename):
    strings = []

    for file in filename:
        with open(f'federallist_{file}.txt') as f:
            strings.append(f.read())

    return ('\n'.join(strings))

federallist_by_author = {}

for author, files in papers.items():
    federallist_by_author[author] = read_file(files)

authors = ('Hamilton', 'Madison', 'Jay')

author_tokens = {}
length_distribution = {}

for author in authors:
    tokens = nltk.word_tokenize(federallist_by_author[author])
    author_tokens[author] = ([token for token in tokens if any(c.isalpha() for c in token)])
    token_length = [len(token) for token in author_tokens[author]]
    length_distribution[authors] = nltk.FreqDist(token_length)
    length_distribution[authors].plot(15, title=author)

