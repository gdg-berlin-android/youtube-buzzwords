if __name__ == '__main__':
    from lib import transcribe_and_count as doit
    import sys
    import json
    from argparse import ArgumentParser

    name="YouTube Word Counter"
    parser = ArgumentParser(
        prog=name,
        description="Count words in a YouTube video using it's transcription.",
        epilog="~ Thanks to GDG Berlin Android ~"
    )

    parser.add_argument('-c','--char-count', default=3, type=int, help='add words with this minimum character count')
    parser.add_argument('-r','--repeat-count', default=10, type=int, help='consider words repeated this often')
    parser.add_argument('-v','--videos', nargs='*', default=['eIUqw3_YcCI'], help='YouTube video ids to parse')
    args = parser.parse_args(sys.argv[1:])

    print(f'~~{name}~~\n\nlisting all words with more then {args.char_count} characters occuring more then {args.repeat_count} times.\n', file=sys.stderr)

    print(
        json.dumps(
            dict(
                sorted(
                    [(x,doit(x,min_char_count=args.char_count,min_repeat_count=args.repeat_count)) for x in args.videos],
                    key=lambda x: x[1]
                ),
            ),
            indent=2
        )
    )
