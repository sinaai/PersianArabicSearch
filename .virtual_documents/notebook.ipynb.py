from sampleIndex.sampleIndex import buildindex
from databaseRefactor import rebuild_index, separate_languages


# make a sample index with 500 arabic and farsi contents
buildindex(name="sample-index", field="body")


# seperate arabic and farsi sentences and added as new fields to database
input_index = 'sample-index'
output_index = 'my-index'
text_field = 'body'

rebuild_index(input_index, output_index, text_field, language_detection_library='voting')


# to build a dictionary of farsi and arabic part of a string
string = 'کیست که بتواند آتش بر کف دست نهد و با یاد کوه های پر برف قفقاز خود را سرگرم کند؟ من يستطيع أن يشعل النار في يده؟'
separate_languages(string)



