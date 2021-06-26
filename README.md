# Persian-Arabic Search in elastic search

Search multi-language in elasticseach index

[Colab Demo is available](https://colab.research.google.com/drive/1hAS83QhveLlh2sx7JkNPtYEeVjSLw4tj?usp=sharing)

Use `sampleIndex.buildindex` to generate a sample index with 500 multi-language documents (Farsi and Arabic).

Use `databaseRefactor.separate_languages` to separate Farsi and Arabic parts of a string.
The output will be a python dictionary.

Use `databaseRefactor.rebuild_index` to separate Farsi and Arabic parts of an input index.


look at `notebook.ipynb` for more information.