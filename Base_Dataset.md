#The Data

This dataset consists of the records for three years of metadata describing articles from the journal _American Literature_, downloaded from _MLA International Bibliography_. For each year, I have a human-readable .txt file I copied from the HTML page produced by EBSCO's "Save" function, as well as CSV file listing each record. Because I am working only with the metadata, I used only the .txt files in this analysis, but the CSV file is useful for other kinds of analysis, as explained below.

Although each file covers a year's worth of articles published in this journal, they are not equal in number.  The number of articles is as follows:
* 1950: 37 articles
* 1980: 35 articles
* 2010: 24 articles

I plan to extract the subject terms for further examination.  The rest of the metadata (article titles, author names, etc) will probably not be used in this project.

## Structure of the Data

Although I cannot share the dataset as I downloaded it due to copyright restrictions, I can explain exactly how to access it, or others like it. 

My search in _MLAIB_ captures metadata about this journal, rather than the text of the journal itself. Thus, I am already at one remove from the articles themselves.  While the _Bibliography_ indexes all the scholarly articles published in _American Literature_, it does not capture all the journal's content, since it excludes book reviews. It also does not capture the distinctions made within the journal's structure between longer articles and what the journal calls "Notes and Queries." Thus, while _MLAIB_ represents the scholarly content of this journal, it doesn't represent everything published there. 

More subtly, however, the way that the data is structured is also a representation by the _Bibliography_. _MLAIB_ is a database with a graphic user interface (GUI). GUIs are relatively user-friendly and often straightforward, but they also limit what data a user is able to access. As we shall see below, I spent some time and effort teasing out the various types of metadata; if I had access to the back end of the bibliography, I could have accessed the structured data directly. Furthermore, the variation among searchable fields in different vendor platforms suggest that there are differences between the fields that exist in the database and the fields made available for users to view and search. 

Above, we looked at the structure of a record in the _Bibliography_.  Each piece of information gathered about the article is slotted into a particular category, like "author" or "subject term."  These categories are called "fields." 

Records in the bibliography constitute data for us, but looking at this record, it's clear that many choices have already been made.  When selecting which fields to include in a record, the editors of the bibliography decided which characteristics of an item are important enough to include in its description, and have structured the database around these decisions. This is why it's easy to ask questions about which authors are the subjects of articles, but much more difficult, for instance, to ask questions about which authors had mental illnesses. Please note that I am not necessarily making an argument for more comprehensive descriptions of articles here! There might be good reasons to make certain searches available and not others. However, it is always important to be cognizant of how data's tractability is shaped by the decisions made when it was originally made available. 

The vendor platforms also make choices as they add their own structure to the metadata; note that the Gale and EBSCO search interfaces use different language to describe the fields, and may in fact yield different results.*** This results in subtle differences in the records. Most notably for our purposes, EBSCO breaks out the different types of subject terms, while Gale simply presents an unstructured list. The structure behind the subject terms exists and can be searched in Gale, but their structure is not visible to endusers in the record itself. In short, when working with a GUI, not all the data is visible or available! In this case, the EBSCO  interface is desirable because it makes the structure visible, allowing me to use it to analyze subject authors and works separately from the descriptive subject terms. 

## Collecting the Data

As stated above, the scope of this project required that I retrieve the records for all the articles published in _American Literature_ for three separate years. 

I did three separate searches, one for each year. Because other journal titles may include the phrase "American literature," I searched by ISSN (0002-9831), and for each search, I limited by date to the appropriate year.  The EBSCO interface includes a "Share" button, which allows the user to add one (20-item) page of results to the folder at a time, so I clicked through and added each page.  From the folder, it is possible to save up to fifty results at a time. This limitation presents another strong argument against working with a large dataset.   

For each year, I obtained:

* A CSV file, which can be downloaded by using the "export" function in the folder and the "Download as CSV" option there.
* A plain text file. This data was obtained via the "Save As File" option in the folder and copied into a text file.

[First_Transformation](Transform_Stage_1.md)
[Back](Introduction.md)