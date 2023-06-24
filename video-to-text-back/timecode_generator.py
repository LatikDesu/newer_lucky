
def get_subs(dictionary):
    subs_dictionary = {}
    for record in dictionary:
        start_time = record['start']
        end_time = record['end']
        text = record['text']

        subs_dictionary.update({
            record['id']: {
                'start': start_time,
                'end': end_time,
                'text': text
            }
        })

    return subs_dictionary


def timecode_generator(result, subs):
    subs_dict = get_subs(subs)

    timecode = {}

    for items in result:
        code = []
        for key in subs_dict:
            if subs_dict[key]['text'] in items:
                code.append(int(key))
        timecode.update(
            {
                result.index(items): {
                    'code': code
                }
            }
        )

    for index in timecode:
        mini = min(timecode[index]['code'])
        maxi = max(timecode[index]['code'])

        timecode[index]['start'] = subs_dict[mini]['start']
        timecode[index]['end'] = subs_dict[maxi]['end']

    return timecode
