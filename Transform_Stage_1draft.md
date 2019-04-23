# Working with MLA Data -- First Steps

## Previously, on Project TRIKE: American Literature...

I identified the data I wanted to use for this project.  I knew I wanted to look at records from the _Modern Language Association International Bibliography_, but also needed to limit the amount of data I worked with, so I chose one journal (_American Literature_) and three evenly-spaced years (1950, 1980, and 2010). I used the EBSCO version of the MLA database to download these records in two separate file formats.

Where We Start:

For each year, I have two different documents:

* A CSV file, downloaded from the EBSCO interface for _MLAIB_ using the "export" function in the folder and the "Download as CSV" option there.
* A plain text file. This data was obtained via the "Save As File" option in the folder and copied into a file.

Each CSV file provides a compilation of all the records for a year, making it easy to see the data included in each record and how the fields relate to each other. However, while the CSV does an admirable job of splitting out the bibliographic information, such as title, author, and issue, it lumps all the different types of subject heading into a single "subjects" field.

The text file is much less easy to work with as data, but it does make these distinctions. As we saw on the prior page, Subject Author, Subject Work, Period, and Classification are separate from the subject terms that describe the content of the article. This information exists in the database as it's provided to the database vendors, and can be searched as such, but it isn't reflected in the downloadable CSV file.  

It's useful to remember that the data that exists in a resource may be different from what end-users are allowed to access! While it's a little frustrating to spend time reconstructing a structure that already exists in the database, we do have the data and the tools to do it.

## Technical Stuff: Extracting Subject Terms

Before I can analyze the subject terms, I need to put them into a more tractable format.  The CSV file isn't much help, because it doesn't make those distinctions.  However, I also don't want to spend the time to go through each record and pulling out the information manually, even for a small dataset.

This is where a little bit of programming knowledge can come in handy. I used Python to extract the subject terms, and copied them into CSV files. 

Getting the Subject Terms from the Text File

Please see my Jupyter Notebook for a more complete explanation of the technical details of this process. 

mla_metadata_queries.ipynb

In short, my Python script turned the text file into a list, like this:

infile = open('1950_readable.txt')
metadata = infile.read()
metadata_list = metadata.split("\n")

Then, it searched each line in the list for the words that signaled the types of metadata that I wanted and used the indexing function of Python to print out the terms I wanted.  For example, the code:

for line in metadata_list:
    if "Period:" in line:
        print(line[8:])

printed out a list of century ranges, which I then copied and pasted into a CSV file. 

In some cases, a line might contain more than one term, separated by semicolons. I dealt with this by turning all the terms into a string again, and then splitting on the semicolons; please see the code linked above for more. 

The subject terms describing the content of the article were the most difficult, because the records as I obtained them had the field label ("Subject Terms") on one line, and the content of the field on the next. Ultimately, I settled on this:

line_number = 0
subject_list = ""
while line_number < len(metadata_list):
    if "Subject Terms" in metadata_list[line_number]:
        subject_term = metadata_list[line_number + 1]
        subject_list = subject_list + "; " + str(subject_term)
    line_number = line_number + 1
print(subject_list)

After iterating, copying, and pasting, I ended up with these three CSV files:

* 1950_subjects.csv
* 1980_subjects.csv
* 2010_subjects.csv

However, for the purposes of actually working with the data, I split it out into several different files, as follows:

* subject_dates_compiled.csv
* subject_authors_compiled.csv
* subject_works_compiled.csv
* work_classification_compiled.csv
* subject_terms_compiled.csv

In this context, the word "subject" means that the characteristics described belong to the work under analysis, not the article analyzing them. Let's walk through each of these:

* "Subject date" is my rephrasing of the field "Period", which specifies the century in which the work was published (for instance, 1800-1899).
* "Subject authors" are the authors of works being analyzed (for instance, Phillis Wheatley).
* "Subject works" are the works of literature being analyzed (for instance, Leaves of Grass).
* The "work classification" tells us which type of work is being analyzed -- drama, poetry, novel, etc.  
* Finally, the "subject terms," while also a phrase applied to the broader list, is used here to refer to the list of descriptive subject terms that bring out the main concerns of the critic in analyzing the work. These can be very varied, but for example, words like "poetic form" or "electricity" or "innocence" might be used. 

## Evaluating the Data

I'd succeeded in getting my data into a workable format! That's great, but it might still have some errors or just some incompatibilities with the methods I have planned. 

This is the part of the process that's often referred to as "data cleaning." I avoid this language because it implies that the perfect dataset exists underneath the flaws that I'll be removing.  In fact, I'm creating a new version of the data that works for my purposes, and as I do so, I'm making decisions about what the data will be.  

Thus, it's important for me to give a full account of this process, in order to be honest and clear about what my dataset is!

### Extra Words

A few of the fields contained some extra material.  For instance, the 1950 data on subject work classification included some fields called "prose" or "poetry," but also some that read "and prose." This is an artifact of the way the data was originally presented as the second of two types of works analyzed in the same article ("poetry; and prose"). I can imagine a situation in which I'd want to keep the "and" so that I could keep track of which were considered the primary works and which were considered additional, but that is much more subtle than the work I'm doing, so I removed the extra word.

Similarly, many of the author's names and subject terms began with contextualizing words, like "as," "of," "in," or "and." These slightly change the meaning of the terms, so I decided to leave them in for the time being, although I may not use them. I can always remove them later. We'll see some examples as we go along. 

Other extra parts were more systemic.  The convention in the bibliography is to include an author's birth and death dates alongside their name. This rule has changed; in the past, it was used for some authors and not others, so the data I have is inconsistent.  If I were working with a larger dataset, this could create a major problem. Suppose, for instance, I relied on software to collapse all the instances of Melville's name.  Those that included his dates and those that didn't would be separate. However, I'm not doing that kind of analysis, either. I'm not working with the dates, but I chose to leave them, because I have no pressing need to get rid of them. 

### Data in the Wrong Field

Prior to my creation of this dataset, MLA created and published the records that comprise it; they subsequently sent it to EBSCO, where it was reformatted to fit the schema that EBSCO applies to its databases.  If errors were introduced at any point in this process, they would persist into my dataset.  For instance, an observation about the work could be put into the wrong field.  In the subject date list, you may notice that one of the periods listed in the 2010 data is:

"role of Child, Lydia Maria (1802-1880); in editions (1865)"

This definitely doesn't belong in "period" field, which has a specific format and should have read "1800-1899".  Judging by the phrasing ("role of"), these are both part of the "subject terms" field and should have been included there.  This affects the record in two ways: the subject data is missing from the subject field, and the date is missing from the period field. 

As I work with the data, should I correct this in either field, neither, or both? 

I consulted the original record.  It seemed clear to me that these headings belonged in the subject terms, so I moved them there. However, I also noticed that there was a duplicate field for the subject period! Thus, I didn't replace it. 

This error stands out because of the uniform formatting of this particular field. Errors in other fields may be more difficult for me to catch, especially in a larger dataset. Addtionally, I want to be careful about correcting errors, to avoid creating new inconsistencies. 

### Duplicate Data

The previous error made me suspicious. Upon checking, I noticed that the number of dates listed did not match the number of records.  I checked more carefully against the original dataset and realized that, in some cases, there were duplicate entries for a field within the same record. Other records did not include thsi data, because if there is no data in a field, MLA silently omits it, which means that the duplicate entries could not be found simply by comparing the number of records to the amount of data.

This process was not glamorous or sophisticated! I searched through each of my original text files for signal words like "Period: " or "Primary Subject Author: " and noted which record each one belonged to; in cases where there was more than one idential piece of data listed for the same record, I went to my CSV files and deleted the duplicate. 

There were some similar duplications in other fields. The descriptive subject terms were particularly difficult. Some records have multiple lists of subject terms with many terms in common; this seems to happen when a work is an adaptation. I would like to do more research into the reasons that this exists, but I suspect that there are multiple sets of subject terms getting applied to the same work, one for itself and one for the work as an adaptation.  In any case, I felt that this gave undue weight to these subject terms, so I removed any subject terms that were repeated within the same heading. The most difficult decision of this sort that I had to make was for a record with two sets of subject headings that looked like this:

Subject Terms:
imagery; of happiness; despair; treatment of Xochiquetzal; sources in Mexican legend

Subject Terms:
treatment of Xochiquetzal; relationship to imagery; of happiness; despair; in Porter, Katherine Anne (1890-1980); Hacienda (1934); 'The Children of Xochitl'

I kept the unique terms and deleted the duplicates, but hesitated over "imagery" and "relationship to imagery." Are these the same, or different? It's very clear that they're occupying the same place in these subject headings, but they aren't exactly the same. Keeping both would make it look like there's more discussion of imagery in this dataset than there actually is, but removing one will change how I read the headings.  In any case, if I do remove one, which one should it be? Ultimately, I decided to keep "relationship to imagery," because I'm interested in how the headings with modifiers of this sort work, and to discard "imagery" to avoid counting it twice, but I could certainly have made a different decision. 

In a larger dataset, I might not be able to detect these duplicates as easily, likely resulting in a dataset with more errors.

### Extra Fields

In the process of checking my data, I discovered the existence of the field "Genre," which appears to substitute for "Category;" it often has the same values (for instance, "novel"), and the records that include "Genre" don't include "Category." However, in some cases, it is more specific than "Category," including terms like "popular poetry" and "historical novel." I don't understand this distinction, but it is much more common in 2010 than it is in the other two years.  For now, I wrote a script to extract this data and put it in a new column.  

Some data, too, exists in some years but not in others. The 1980 and 2010 records include a field called "Group," which identifies various characteristics of the author or authors under consideration in the article: for instance, "African American novelists," "Native American writers," "Puritan poets," etc. None of the records in the 1950 data include this field, and it's rarely used in the 1980 data but common in 2010. This is data that would have been useful to me, but because it isn't applied consistently, I didn't capture it. This is another example of how data is not neutral. Information about "groups" of this sort is only applied when the authors are "marked" in some way -- that is, when they differ from the percieved norm. The articles about African-American literature are labeled as such because it is considered to be a subset of American literature, whereas white authors are seldom "grouped" in this way unless they belong to some other group that's percieved as markable. Note that this isn't necessarily caused by any personal bias on the part of the indexers who applied the subject headings; rather, it may be "baked in" to the subject vocabulary itself. 

### Missing Nulls

As noted above, there are some cases in which an article might not have data for every field, and the database deals with this by not returning the field at all for that record. Since the script I used to extract the data relies on the field labels, it is difficult for me to know when a record is missing a field! I went back and checked for that as well, and added rows in my CSV file with notes like "No Period Listed." This will be important when I want to find the frequencies of certain results. 

## Data Gathered!

Of course, in the activities I've outlined so far, there is already plenty of scope for me to introduce my own errors and oversights into the data.  I've handled it a lot; the more I handle the data, the more likely it is that I'll get something wrong, either through an error in the code I'm using to extract the data or simply through missing something as I corrected errors. I've also done a lot of copying and pasting, which creates the potential that I could make an error, missing part of the list. Although a more streamlined process may reduce (or increase!) some of these risks, it's difficult to avoid them entirely.  

[Second_Transformation](Transform_Stage_2.md)
[Back](Base_Dataset.md)