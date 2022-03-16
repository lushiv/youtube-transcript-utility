#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'janak'
__version__ = "0.0.0.1"

import os, sys
import json
from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeTranscriptHelper:
		"""
		Class For Fetch YouTube Subtitles
		"""

		def __init__(self, video_id,lang):
			self.video_id = video_id
			self.lang = lang


		def transcript_of_particular_language(self):
				return(YouTubeTranscriptApi.get_transcript(self.video_id,languages=[self.lang])) #TODO: json converting

		def getting_list_of_all_transcripts(self):
    			transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)
				for transcript in transcript_list:
    					properties = {
								transcript.video_id,
								transcript.language,
								transcript.language_code,
								transcript.is_generated,
								transcript.is_translatable,
								transcript.translation_languages,

						}

						actual_transcript_data = transcript.fetch()
						transcript_object = transcript.translate(self.lang).fetch()

				transcript = transcript_list.find_transcript([self.lang])
				manually_created_transcripts = transcript_list.find_manually_created_transcript([self.lang])

				return manually_created_transcripts



		def writing_subtitles_to_text_file(self):
    			srt = YouTubeTranscriptApi.get_transcript(self.video_id)
				with open("subtitles.txt", "w") as f:
					for i in srt:
						f.write("{}\n".format(i))




    					

video_1 = YoutubeTranscriptHelper("SW14tOda_kI", "en")

# print(video_1.video_id)
# print(video_1.lang)
video_1.transcript_of_particular_language()
