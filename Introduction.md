# Introduction

The process of creating the dataset involved a series of decisions that determined the kinds of analysis that were possible.

This introduction will state my research questions and walk through the decisions I made in the process of selecting the data.

* [Research Questions](#questions)
* [Selecting the Data](#data)
    * [Choosing the Data Type](#datatype)
        * [_MLA International Bibliography_](#mlaib)
    * [Scope of the Inquiry](#scope)
        * [American Literature](#AmLit)
        * [Narrowing by Date](#date)
 
## <a name="questions">Research Questions</a>
I began with some general questions I wanted to address:

1. Does literary criticism offer evidence of a more inclusive canon of American literature over time?
2. Criticism changed drastically over the course of the twentieth century. Are these differences visible from the metadata and subject indexing of journals?
3. How has the indexing in the _MLA International Bibliography_ (a tool used to identify and describe literary criticism)  shifted over time?

Note that one research project can’t fully answer any of these questions. However, I can create a dataset that will at the very least tell us where to look for the answers.

## <a name="data">Selecting the Data</a>
I obviously couldn’t consider all the criticism ever published about American literature. I needed to make some decisions about the nature and amount of data I could use.

### <a name="datatype">Data Type: Metadata vs Full Text</a>

I chose to look at the subject terms that indexers used to describe criticism (metadata), rather than using textual analysis techniques to consider a corpus of criticism published in the journal _American Literature_. Textual analysis is fascinating, but putting together a corpus in a useful format introduces potential difficulties in accessing, downloading, and formatting the materials. Subject terms, in contrast, are readily available to download. They are useful because they capture information about what the articles cover, including the details about which authors and works are analyzed and which themes figure strongly. Additionally, they provide information not only about the journal, but about resources that help scholars identify materials they want to use.

#### <a name="mlaib">A Source for the Data: _MLA International Bibliography_</a>

There is really only one source for metadata describing literary criticism, and that is the _MLA International Bibliography_.

_MLAIB_ is a database/index maintained by the Modern Language Association, a scholarly association for the study of language and literature. Coverage goes back to the 1920s and includes metadata for each item, including title, author, source, and ISSN or ISBN, and some additional information.

Additionally, each record includes a number of subject terms, which describe the content of the item described. These subject terms, too, are structured. Possible categories of subject terms include: subject literature (that is, national literature), period (by century), subject author, subject work, and subject terms describing the ideas and themes which the work describes.

One more note on _MLAIB_: The MLA develops the database, but to grant access to end users, it relies on vendors — commercial companies which provide platforms for searching and viewing content. As of this writing, in March 2019, the _Bibliography_ is available via three different vendors: Gale, EBSCO, and ProQuest. However, in 2018, MLA made a decision to make the _Bibliography_ available exclusively through EBSCO in the future. Thus, I used the EBSCO interface for this research.

### <a name="scope">Data Scope: How Much Data Do We Want?</a>
There are several ways I could have limited the scope of this dataset. I could have focused on specific time periods, or specific authors, or articles that used a particular subject term. I chose to focus on a single journal, because:

* Issues of a journal are likely to be similar in both subject matter and length.
* Changes in a journal reflect what’s happening between a journal and its readership.  If the number of journals on a topic changed over time (as it certainly did), that will affect what sorts of articles are available in the database, but won’t affect the content in a single journal.
* This narrows down the number of records in a very predictable way.

Of course, because this project focused on a single journal, it could not compare publications across journals in the same field, and I was not able to draw conclusions about the field as a whole. This was a necessary limitation resulting from working with a manageable amount of data.

Looking at only American Literature, we could identify changes in a well-known journal with a large readership, and perhaps some changes in the ways that articles are indexed.  Furthermore, the trends we noticed can inspire research questions for future projects with larger datasets.

Other projects using this approach could look at a group of journals to make broader inferences about a field, or the criticism on a particular work or author (or a group of works or authors). It would be possible to choose other years, or a larger number of years. In each case, however, it is necessary to think about how much data a researcher can work with, considering the time and tools available to her, and choose the data that is most likely to answer that researcher’s questions.

#### <a name="AmLit">_American Literature: A Journal of Literary History, Criticism, and Bibliography_</a>
The journal I chose was _American Literature_, which is published by Duke University Press and is indexed in many databases, including those that cover literature and history. The journal is published quarterly, with new issues appearing in March, June, September and December. _American Literature_ has been published since 1929.

Almost any scholarly journal could be appropriate for the kind of analysis this project will perform. However, _American Literature_ is a good choice because:

* It has a long publication history, which allowed me to consider several different time periods.
* _American Literature_ publishes a relatively high number of articles per issue, thus providing more data for my analysis.
It is a well-known and well-respected journal with a broad focus and large readership, so it is likely more reflective of concerns in the broader field of American literature than a more specialized journal.
* It is indexed in _MLAIB_.

#### <a name="date">Data Scope: Narrowing by Year</a>
Initially, I had hoped to look at decades rather than years. However, this proved to be more data than I could work with easily for a project of this scope. Thus, I chose three sample years, 1950, 1980, and 2010.

These sample years are thirty years apart, allowing time for shifts in the discipline to take place.

Additionally, they fall in the middle of _American Literature_'s publication history: well after their first issue, which was published in 1929, but also well before the present day, which as of this writing is 2019.

Regardless of the specific years chosen, I wanted to avoid working with current data, since current data is more likely to change in the future. I hoped that future users of this resource would be able to access the same data that I use here.

[Continue on to the next section...](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/Base_Dataset.md)

[Return to table of contents...](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/table_of_contents.md)