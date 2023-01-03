from writer.writer import Writer


class ErrorWriter(Writer):

    def __init__(self, file_name):
        super(ErrorWriter, self).__init__(file_name)

    def write(self, errors):
        result = ''
        for i in errors.keys():
            result += f'{i}.\t'
            for error in errors[i]:
                if error[1] == 'Unclosed comment':
                    result += f'({error[0][0:7]}..., {error[1]}) '
                else:
                    result += f'({error[0]}, {error[1]}) '
            result += '\n'

        if len(errors) == 0:
            result = 'There is no lexical error.'

        self.file.write(result)
        self.close_file()




