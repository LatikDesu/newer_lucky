from loguru import logger


def get_subtitles(data):
    subtitles = {}

    for record in data:
        start_time = record['start']
        end_time = record['end']
        text = record['text']

        subtitles.update({
            record['id']: {
                'start': start_time,
                'end': end_time,
                'text': text
            }
        })

    return subtitles


def get_timecodes(text_lines, subtitles):
    timecodes = {}

    for each in text_lines:
        code = []
        for key in subtitles:
            if subtitles[key]['text'].strip() in text_lines[each]['text'].strip() \
                    or text_lines[each]['text'].strip() in subtitles[key]['text'].strip():
                code.append(int(key))
        timecodes.update({each: {'code': code}})

    for index in timecodes:
        if timecodes[index]['code']:
            timecodes[index]['start'] = subtitles[timecodes[index]['code'][0]]['start']
            timecodes[index]['end'] = subtitles[timecodes[index]['code'][-1]]['end']

    return timecodes


def timecode_to_text(timecodes, text_lines):
    for index in text_lines:
        text_lines[index].update({
            "id": index,
            "start": timecodes[index]['start'],
            "end": timecodes[index]['end'],
        })
    return text_lines


def get_text_timecodes(text_paragraphs, text_sentences, data):
    logger.info("Получаем субтитры...")
    subtitles = get_subtitles(data)

    logger.info("Получаем время параграфов...")
    p_timecodes = get_timecodes(text_paragraphs, subtitles)

    logger.info("Получаем время предложений...")
    s_timecodes = get_timecodes(text_sentences, subtitles)

    logger.info("Создаем субтитры к параграфам...")
    pwt = timecode_to_text(p_timecodes, text_paragraphs)

    logger.info("Приделали субтитры к предложениям...")
    swt = timecode_to_text(s_timecodes, text_sentences)

    return pwt, swt
