from guessit import guessit


def filename_parsing(files):
    parsed_files = []
    for file in files:
        parsed_files.append(guessit(file))
    return parsed_files


def format_filename(parsed_files):
    output_filenames = []
    for file_dict in parsed_files:
        output_filenames.append("%s - %d [%s].%s"
                                % (file_dict['title'], file_dict['episode'],
                                   file_dict['screen_size'], file_dict['container']))
    return output_filenames
