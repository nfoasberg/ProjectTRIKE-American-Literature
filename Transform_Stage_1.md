# Data Transformation Stage 1

In this section, I’ll explain the technical methods I used to extract the subject terms and the process through which I evaluated the data. Finally, I reflect briefly on the data I’ve gathered and the mistakes it might still include, or new ones I could have introduced.

* [Extracting Subject Terms](#extracting)
    * [Types of Subjects](#subjects)
* [Evaluating the Data](#evaluating)
    * [Extra Words](#extrawords)
    * [Wrong Field](#wrongfield)
    * [Duplicate Data](#duplicate)
    * [Extra Fields](#extrafields)
* [Data Gathered](#data)

## <a name="extracting">Technical Stuff: Extracting Subject Terms</a>
Before I could analyze the subject terms, I needed to put them into a more tractable format.

In order to avoid having to pull out the terms manually, I used Python to extract the subject terms, and copied the results into CSV files.

Getting the Subject Terms from the Text File
Python is very handy for identifying and extracting specific fields from a text file. Please see my [Jupyter Notebook](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/MLA_Metadata_Queries.ipynb) for a more complete explanation of the technical details of this process.

After iterating, copying, and pasting, I ended up with these three CSV files:

* [1950_subjects.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/1950_subjects.csv) 
* [1980_subjects.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/1980_subjects.csv)
* [2010_subjects.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/2010_subjects.csv)

There are some aspects of the records I couldn’t capture in this way. For instance, this script did not include information about which subjects belonged to which record. Additionally if a field had no data, it wasn’t included in the results returned. Fields without data are called nulls and often pose a problem in datasets, including this one!  I later went back and added the nulls back in manually, in order to give a more accurate impression of the proportions in my data.

### <a name="subjects"Types of Subjects</a>
For the purposes of actually working with the data, I split it into several different files, as follows:

* [Subject_dates_compiled.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/subject_dates_compiled.csv)
* [Subject_authors_compiled.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/subject_authors_compiled.csv) 
* [Subject_works_compiled.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/subject_works_compiled.csv) 
* [Work_classification_compiled.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/work_classification_compiled.csv) 
* [Subject_terms_compiled.csv](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/csv/subject_terms_compiled.csv)  

In this context, the word “subject” means that the characteristics described belong to the work under analysis, not the article analyzing them. Let’s walk through each of these:

* “Subject date” is my rephrasing of the field “Period”, which specifies the century in which the work was published (for instance, 1800-1899).
* “Subject authors” are the authors of works being analyzed (for instance, Phillis Wheatley).
* “Subject works” are the works of literature being analyzed (for instance, _Leaves of Grass_).
* The “work classification” tells us which type of work is being analyzed — drama, poetry, novel, etc.
* Finally, the “subject terms,” while also a phrase applied to the broader list, is used here to refer to the list of descriptive subject terms that bring out the main concerns of the critic in analyzing the work. These can be very varied, but for example, words like “poetic form” or “electricity” or “innocence” might be used.

## <a name="evaluating">Evaluating the Data</a>
I succeeded in getting my data into a workable format! That’s great, but it could still have some errors or just some incompatibilities with the methods I wanted to use to analyze it.

Identifying and correcting these errors constituted the part of the process often referred to as “data cleaning.” I avoid this language because it implies that the perfect dataset exists underneath the flaws that I carefully removed. In fact, I creating a new version of the data that worked for my purposes, and as I did, I made decisions about what the data was.

Thus, it’s important for me to give a full account of this process!

### <a name="extrawords">Extra Words</a>
A few of the fields contained some extra material. For instance, the 1950 data on subject work classification included some fields called “prose” or “poetry,” but also some that read “and prose.” This was an artifact of the way the data was originally presented as the second of two types of works analyzed in the same article (“poetry; and prose”). I could imagine a situation in which I’d want to keep the “and” so that I could keep track of which were considered the primary works and which were considered additional, but that is much more subtle than the work I actually did in this project, so I removed the extra word.

Similarly, many of the author’s names and subject terms began with contextualizing words, like “as,” “of,” “in,” or “and.” These slightly changed the meaning of the terms, so I decided to leave them in for the time being.

The convention in the bibliography is to include an author’s birth and death dates alongside their name. This rule has changed; in the past, it was used for some authors and not others, so the data presented here is inconsistent. If I were working with a larger dataset, this could create a major problem. Suppose, for instance, I relied on software to collapse all the instances of Melville’s name. Those that included his dates and those that didn’t would be separate. However, this project did not include that kind of analysis, either. I chose to leave the dates there, because I had no pressing need to get rid of them.

### <a name="wrongfield">Data in the Wrong Field</a>
Prior to my creation of this dataset, MLA created and published the records that comprise it; they subsequently sent it to EBSCO, where it was reformatted to fit the schema that EBSCO applies to its databases. If errors were introduced at any point in this process, they would persist into my dataset. For instance, an observation about the work could be put into the wrong field. In the subject date list, one of the periods listed in the 2010 data was:

    role of Child, Lydia Maria (1802-1880); in editions (1865)

This definitely didn’t belong in “period” field, which has a specific format and should have read “1800-1899”. Judging by the phrasing (“role of”), these are both part of the “subject terms” field and should have been included there. This affected the record in two ways: the subject data was missing from the subject field, and the date was missing from the period field.

I had to decide: should I correct this in either field, neither, or both?

I consulted the original record. It seemed clear to me that these phrases belonged in the subject terms, so I moved them there. However, I also noticed that there was a duplicate field for the subject period! Thus, I didn’t replace the date.

This error stands out because of the uniform formatting of this particular field. Errors in other fields may be more difficult to catch, especially in a larger dataset. I tried not to make too many changes to the data, in order to avoid creating new inconsistencies.

### <a name="duplicate">Duplicate Data</a>
The previous error made me suspicious. Upon checking, I noticed that the number of dates listed did not match the number of records. I checked more carefully against the original dataset and realized that, in some cases, there were duplicate entries for a field within the same record.

I manually searched through each of my original text files for signal words like “Period: ” or “Primary Subject Author: ” and noted which record each one belonged to; in cases where there was more than one identical piece of data listed for the same record, I deleted the duplicate from the CSV file.

Repetitions in the descriptive subject terms were particularly difficult. Some records have multiple lists of subject terms with many terms in common; this seems to happen when a work is an adaptation. I would like to do more research into the reasons that this exists, but I suspect that there are multiple sets of subject terms getting applied to the same work, one for itself and one for the work as an adaptation. In any case, I felt that this gave undue weight to these subject terms, so I removed any subject terms that were repeated within the same heading. The most difficult decision of this sort that I had to make was for a record with two sets of subject terms that looked like this:

    Subject Terms: imagery; of happiness; despair; treatment of Xochiquetzal; sources in Mexican legend

    Subject Terms: treatment of Xochiquetzal; relationship to imagery; of happiness; despair; in Porter, Katherine Anne (1890-1980); Hacienda (1934); ‘The Children of Xochitl

I kept the unique terms and deleted the duplicates, but hesitated over “imagery” and “relationship to imagery.” Were these the same, or different? It’s very clear that they occupied the same place in the list of subject terms, but they weren’t exactly the same. Keeping both would make it look like there’s more discussion of imagery in this dataset than there actually is, but removing one would change how I read the terms. In any case, if I were to remove one, which one should it be? Ultimately, I decided to keep “relationship to imagery,” because I was interested in how the terms with modifiers of this sort work, and to discard “imagery” to avoid counting it twice, but I could certainly have made a different decision.

In a larger dataset, I might not have been able to detect these duplicates as easily, likely resulting in a dataset with more errors.

### <a name="extrafields">Extra Fields</a>
In the process of checking my data, I discovered the existence of the field “Genre,” which appears to substitute for “Category;” it often has the same values (for instance, “novel”), and the records that include “Genre” don’t include “Category.” However, in some cases, it is more specific than “Category,” including terms like “popular poetry” and “historical novel.” I don’t understand this distinction, but it is much more common in 2010 than it is in the other two years. For now, I wrote a script (much like the ones linked earlier) to extract this data and put it in a new column.

The 1980 and 2010 records include a field called “Group,” which identifies various characteristics of the author or authors under consideration in the article: for instance, “African American novelists,” “Native American writers,” “Puritan poets,” etc. None of the records in the 1950 data include this field, and it’s rarely used in the 1980 data but common in 2010. This is data that would have been useful to me, but because it isn’t applied consistently, I didn’t capture it. This is another example of how data is not neutral. This category is only applied when the authors are “marked” in some way — that is, when they differ from the perceived norm. The articles about African-American literature are labeled as such because it is considered to be a subset of American literature, whereas white authors are seldom “grouped” in this way unless they belong to some other group that’s perceived as markable (like the Puritans). Note that this isn’t necessarily caused by any personal bias on the part of the indexers who applied the subject terms; rather, it may be “baked in” to the subject vocabulary itself.

## <a name="data">Data Gathered!</a>
Of course, in the activities I’ve outlined so far, there was already plenty of scope for me to introduce my own errors and oversights into the data. I handled it a lot; the more I handled the data, the more likely it was that I would get something wrong. I also did a lot of copying and pasting, which creates the possibility that I could have missed part of the list. Although a more streamlined process may have reduced some of these risks, it’s difficult to avoid them entirely.

[Continue on to the next section...](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/Transform_Stage_2.md)

[Return to the table of contents...](https://github.com/nfoasberg/ProjectTRIKE-American-Literature/blob/master/table_of_contents.md)