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

