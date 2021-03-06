import argparse
import sys
import os
import moviepy.editor as mp


def main():
    input_filename, output_filename, codec = get_filenames()
    movie_clip = mp.VideoFileClip(input_filename)
    movie_clip.audio.write_audiofile(output_filename, codec=codec)


def get_filenames() -> (str, str, str):
    # List of supported audio file formats
    codec_choices = ["mp3", "aac", "wma", "wav", "ac3"]

    # Setting up the CL-args parser
    parser = argparse.ArgumentParser(
        'audio_convt', description="Extractors the audio from a given video file.")

    parser.add_argument('filename', metavar='filename')
    parser.add_argument('-o', '--output', metavar='Output file path', type=str,  default="", required=False,
                        help="Specifies the output filename name w/o it's directory.")
    parser.add_argument('-p', '--prefix', metavar='Name Prefix', type=str,  default="", required=False,
                        help="If any string is to be prefixed to the name")
    parser.add_argument('-c', '--codec', metavar='Audio File Format', type=str, default='mp3', required=False, choices=codec_choices,
                        help="The audio file format. eg, mp3, wav etc.")

    args = parser.parse_args()

    # The source video file.
    input_filename = args.filename

    # The output audio file.
    output_filename = input_filename

    # Checking whether the provied input file is a valid file.
    if not os.path.isfile(output_filename):
        print("%s is an invalid filename." % output_filename)
        exit(1)

    # If the output filename is provided, then inferring the audio type according to the provided filename.
    output_filename, ext = os.path.splitext(output_filename)

    # Setting up the codec
    codec = args.codec

    string_prefix = args.prefix

    # Checking for the output string
    path, file = os.path.split(args.output.strip())
    # In case the filename is not provided
    if file != '':
        output_filename, ext = os.path.splitext(file)
        if ext[1:] in codec_choices:
            codec = ext[1:]
        else:
            print("This audio file format is not supported")

    return input_filename, os.path.join(path, "%s%s.%s" % (string_prefix, output_filename, codec)), codec if 'w' not in codec else None


if __name__ == "__main__":
    main()
