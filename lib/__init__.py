def transcribe_and_count(video_id='eIUqw3_YcCI', min_char_count=3, min_repeat_count=10):
    import re
    import youtube_transcript_api
    yt = youtube_transcript_api.YouTubeTranscriptApi()
    ts = yt.fetch(video_id)
    
    text = "\n".join([x.text for x in ts.snippets])
    words=[re.sub('\\W','',x).lower() for x in re.split('\\s', text)]
    filtered = list(
        filter(
            lambda x: len(x[1]) > min_char_count and x[0] > min_repeat_count, 
            sorted(
                set(
                    [(words.count(word),word) for word in words]
                ), 
                key=lambda x:x[0]
            )
        )
    )

    mapped = dict((x[1],x[0]) for x in filtered)
    return mapped

if __name__ == '__main__':
    import sys
    import json
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog="YouTube Word Counter",
        description="Count words in a YouTube video using it's transcription.",
        epilog="~ Thanks to the GDG Berlin Android ~"
    )

    parser.add_argument('-c','--char-count')
    parser.add_argument('-r','--repeat-count')
    parser.add_argument('-v','--videos', nargs='*')
    args = parser.parse_args(sys.argv[1:])
    print(args)
    sys.exit(-1)

    vids = sys.argv[1:]
    if len(vids) == 0:
        vids = ['eIUqw3_YcCI']

    print(
        json.dumps(
            dict([(x,transcribe_and_count(x)) for x in vids]),
            indent=2
        )
    )
