import csv

class Parse_CSV:

    def __init__(self):

        data = []
        with open('data/result.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        raw_data = [item[2:] for item in data[1:]]
        for item in raw_data:
            if len(item) != 4:
                print(item)
        self.article_data = []
        self.notes_data = []
        for item in raw_data:
            if item[0] == '' and item[1] == '' and item[2] == '':
                self.notes_data.append(item[3])
            else:
                self.article_data.append(item)

    def get_article_data(self):
        return self.article_data

    def get_note_data(self):
        return self.notes_data

# p = Parse_CSV()
# for item in p.get_note_data():
#     print('------------------')
#     print(item)
#     print('------------------')

# data = p.get_csv_data()[1:]
# data = [item[2:] for item in data]
# print(data[:5])
# print(type(data))
