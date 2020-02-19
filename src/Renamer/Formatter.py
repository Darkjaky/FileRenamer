from guessit import guessit


def filename_parsing(files):
    parsed_files = []
    for file in files:
        parsed_files.append(guessit(file))
    return parsed_files


def format_filename(file):
    file_dict = guessit(file)
    episode = str(file_dict['episode']) if file_dict['episode'] >= 10 else "0" + str(file_dict['episode'])
    return ("%s - %s [%s].%s" % (file_dict['title'], episode,
                                 file_dict['screen_size'], file_dict['container']))


def get_all_formatted_filenames(parsed_files):
    format_files = []
    for file_dict in parsed_files:
        format_files.append(format_filename(file_dict))
    return format_files
