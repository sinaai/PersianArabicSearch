from sampleIndex.sampleIndex import buildindex
from databaseRefactor import rebuild_index


# make a sample index with 500 arabic and farsi contents
buildindex(name="sample-index", field="body")


# seperate arabic and farsi sentences and added as new fields to database
input_index = 'sample-index'
output_index = 'my-index'
text_field = 'body'

rebuild_index(input_index, output_index, text_field, language_detection_library='voting')



