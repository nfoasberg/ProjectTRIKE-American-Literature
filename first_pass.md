# Working with MLA Data -- First Steps

## Previously, on Project TRIKE: _American Literature_...

I identified the data I wanted to use for this project.  I knew I wanted to look at records from the Modern Language Association International Bibliography, but also needed to limit the amount of data I worked with, so I chose one journal (_American Literature_) and three evenly-spaced years (1950, 1980, and 2010). I used the EBSCO version of the MLA database to download these records in two separate file formats.

## Where We Start:

For each year, I have two different documents:

* A CSV file, downloaded from the EBSCO interface for MLAIB using the "export" function in the folder and the "Download as CSV" option there.
* A plain text file. This data was obtained via the "Save As File" option in the folder and copied into a file.

Each CSV file provides a compilation of all the records for a year, making it easy to see the data included in each record and how the fields relate to each other. However, while the CSV does an admirable job of splitting out the bibliographic information, such as title, author, and issue, it lumps all the different types of subject heading into a single "subjects" field.

The text file is much less easy to work with as data, but it does make these distinctions. As we saw on the prior page, Subject Author, Subject Work, Period, and Classification are separate from the subject terms that describe the content of the article. This information exists in the database as it's provided to the database vendors, and can be searched as such, but it isn't reflected in the downloadable CSV file.  

It's useful to remember that the data that exists in a resource may be different from what end-users are allowed to access! While it's a little frustrating to spend time reconstructing a structure that already exists in the database, we do have the data and the tools to do it.

## Technical Stuff: Extracting Subject Terms

Before I can analyze the subject terms, I need to put them into a more tractable format.  The CSV file isn't much help, because it doesn't make those distinctions.  However, I also don't want to spend the time to go through each record and pulling out the information manually, even for a small dataset.

However, Python and regular expressions are useful for this purpose. I wrote a little script to help me extract the relevant data.  (Make the Jupyter Notebook available)

### Getting the Subject Terms from the Text File

My script went a little like this: 

import re
from re import findall
records_1950 = open('1950_readable.txt')
metadata = records_1950.read()
print(metadata)

infile_period = re.findall(r"Period\W+\S+",metadata)
for entry in infile_period:
    print(entry)

This identifies all the instances of a specific line of text in a file. In this case, I looked for the word "Period." However, I didn't just want that tag; I wanted to following text that it indicates. In other words, I wanted a result like this: 

Period: 1900-1999

...not just this:

Period:

So I used the regular expression flags (insert appropriate link) to return the word that follows, and used a similar strategy for the rest of the fields. (give more explanation of these particular flags) In some cases, I needed more flags than others; the subject author search was more like this:

infile_author = re.findall(r"Primary Subject Author\W+\S+\s+\S+\s+\S+",metadata)

Note that this strategy relies on retrieving a certain number of words, where words are defined as sets of alphanumeric characters bounded by spaces.  Thus, it doesn't work as well for fields with a varying number of words in them, such as Subject Work, which finds the titles of the works under consideration. The Subject Terms field is even worse; the number of words in each subject term varies, as does the number of subject terms applied to each article.  

I am not very sophisticated when it comes to regular expressions, so I used a number of flags that seemed to get most of the data that I wanted, copied it into a CSV file, and deleted the extraneous words that came along with it. So for instance, one of my results for subject terms in the 1950 data looked like this:

Subject Terms:
relationship to textual errors; in chapters
Document Information:
Publication Type: Journal Article
Language of

...so I manually trimmed it down to just the part I wanted, which was this: 

Subject Terms:
relationship to textual errors; in chapters

In some cases, the opposite also happened; I cut off part of the subject term and had to search the text document for the part I'd missed and add it in.  

These strategies would have been impractical with a larger dataset, so if I were working with full decades or multiple journals, I would have had to found a better way to do it. However, with the dataset that I had, it was annoying but not impossible to do some manual editing.  

For each year, I created a CSV file breaking out each type of subject term for each year. I called these files, respectively:

1950_subjects.csv
1980_subjects.csv
2010_subjects.csv

(link them)

### Compiling and Reformatting 

This is a good moment to take stock. In addition to the CSV downloads and the text files that I downloaded from the MLA database, I now have one CSV file for each of the three years that looks like this:

(insert screenshot)

I wanted to examine each of the types of subject, but I also wanted to compare across the three years, so I needed to reorganize the data while retaining information about the year in which each entry had been published.  Additionally, the field labels ("Period", "Primary Subject Author", "Primary Subject Work", and "Classification") were still stuck to the terms they defined, and I needed to remove them before I could analyze the terms. 

The more formal problem of field labels is another one that I used Python to solve. I defined my list of subject authors as a string in Python via copying and pasting, like this:

subject_authors_1950 = '''
Primary Subject Author: Lowell, James Russell
Primary Subject Author: Ingraham, Joseph Holt
Primary Subject Author: Irving, Washington (1783-1859)
Primary Subject Author: Melville, Herman (1819-1891)
Primary Subject Author: James, Henry, Jr.
Primary Subject Author: Emerson, Ralph Waldo
'''

...etc. The triple quotation marks allowed me to copy and paste without any additional formatting. Once I had the data in there as a string, I used Python's split function to turn it into a list, like so: 

neat_authors_1950 = subject_authors_1950.split("Primary Subject Author:")
for author in neat_authors_1950:
    print(author)

This printed out a list of authors, which I copied and pasted into an additional CSV file.  I followed the same pattern with each type of subject heading, except the subject terms proper, which didn't include the field label but were separated by semicolons; in their case, I split on semicolon instead of on the field label. 

There are more sophisticated ways to use Python to work with this kind of data. (so why didn't I use them? or maybe I should?? Write more about this)

In any case, I used this technique to create a spreadsheet for each of the types of subject terms and added a column specifying the date. Actually, I created two spreadsheets: one to store the data just as I'd retrieved and formatted it, and another for further manipulations and analysis.  Thus, I ended up with a long list of files:

subject_date_list.csv
subject_date_analysis.xlsx
subject_authors_list.csv
subject_authors_analysis.xlsx
subject_works_list.csv
subject_works_list_compiled.csv
work_classification_list.csv
work_classification_analysis.xlsx
subject_terms_list.csv
coded_subject_terms.csv

(I'll adjust the file names once I get this into more universal formats.)

"Subject" means that the characteristics described belong to the work under analysis, not the article analyzing them. Let's walk through each of these:
"Subject date" is my rephrasing of the field "Period", which specifies the century in which the work was published (for instance, 1800-1899).
"Subject authors" are the authors of works being analyzed (for instance, Phillis Wheatley).
"Subject works" are the works of literature being analyzed (for instance, _Leaves of Grass_).
The "work classification" tells us which type of work is being analyzed -- drama, poetry, novel, etc.  
Finally, the "subject terms," while also a phrase applied to the broader list, is used here to refer to the list of descriptive subject terms that bring out the main concerns of the critic in analyzing the work. These can be very varied, but for example, words like "poetic form" or "electricity" or "innocence" might be used. 

### Errors, Gaps and Decisions

The dataset we're working with has changed a lot since we began, so I want to take a moment here to point out how errors can creep in. 

First, errors may have been part of the data before I downloaded it.  Prior to my creation of this dataset, MLA created and published the records that comprise it; they subsequently sent it to EBSCO, where it was reformatted to fit the schema that EBSCO applies to its databases.  If errors were introduced at any point in this process, they would persist into my dataset.  For instance, an observation about the work could be put into the wrong field.  In the subject date list, you may notice that one of the periods listed in the 2010 data is:

"role of Child, Lydia Maria (1802-1880); in editions (1865)"

This definitely doesn't belong in "period" field, which has a specific format and should have read "1800-1899".  Judging by the phrasing ("role of"), these are both part of the "subject terms" field and should have been included there.  This affects the record in two ways: the subject data is missing from the subject field, and the date is missing from the period field. 

As I work with the data, should I correct this in either field, neither, or both? 

This error stands out because of the uniform formatting of this particular field. Errors in other fields may be more difficult for me to catch, especially in a larger dataset. If I correct all the errors that I notice, I may be giving myself more data to work with, but there is also a risk I may create inconsistencies -- and those inconsistencies will be mine, not MLA's.

Of course, in the activities I've outlined so far, there is already plenty of scope for me to introduce my own errors into the data.  I've handled it a lot; the more I handle the data, the more chance I'll get something wrong. I've describe my process for extracting the subject terms using regular expressions; it would be very easy to miss some data in the case of a long string.  I've combed back through to correct each of those cases that I could find -- but I could certainly miss something. I've also done a lot of copying and pasting, which creates the potential that I could make an error, missing part of the list. So as I work with the data, I could add errors both through my use of scripts and through my manual processing of the data. Although a more streamlined process may reduce (or increase!) some of these risks, it's difficult to avoid them entirely.  

Of course, the relationship between the way the data is structured and the work that I'm doing with it could also cause some problems.  For instance, I am looking at this data longitudinally, so I need to work with older records as well as more recent ones. The 1980 and 2010 records include a field called "Group," which identifies various characteristics of the author or authors under consideration in the article: for instance, "African American novelists," "Native American writers," "Puritan poets," etc. None of the records in the 1950 data include this field, and it's rarely used in the 1980 data but common in 2010. This is data that would have been useful to me, but because it isn't applied consistently, I didn't capture it. On the other hand, some records have multiple lists of subject terms with many terms in common; this seems to happen when a work is an adaptation. I would like to do more research into the reasons that this exists, but I suspect that there are multiple sets of subject terms getting applied to the same work, one for itself and one for the work as an adaptation.  In any case, I felt that this gave undue weight to these subject terms, so I removed any subject terms that were repeated within the same heading. 

The most difficult decision of this sort that I had to make was for a record with two sets of subject headings that looked like this:

Subject Terms:
imagery; of happiness; despair; treatment of Xochiquetzal; sources in Mexican legend

Subject Terms:
treatment of Xochiquetzal; relationship to imagery; of happiness; despair; in Porter, Katherine Anne (1890-1980); Hacienda (1934); 'The Children of Xochitl'

I kept the unique terms and deleted the duplicates, but hesitated over "imagery" and "relationship to imagery." Are these the same, or different? It's very clear that they're occupying the same place in these subject headings, but they aren't exactly the same. Keeping both would make it look like there's more discussion of imagery in this dataset than there actually is, but removing one will change how I read the headings.  In any case, if I do remove one, which one should it be? Ultimately, I decided to keep "relationship to imagery," because I'm interested in how the headings with modifiers of this sort work, and to discard "imagery" to avoid counting it twice, but I could certainly have made a different decision. 

## Coding and Preliminary Analysis

At this point, I had broken the original data into several different miniature datasets containing materials on which I wanted to do a few different types of analysis.

The dates and classification are the most straightforward kinds of data and the easiest to analyze quantitatively.  How many articles were published on 18th, 19th, and 20th century literature? How many were about poetry, prose, or drama? How did this vary over time?  I created some simple tables which laid out these values and left further analysis until later in the process.  

The list of subject works is quite difficult to work with, because very few of them were repeated.  It's possible, of course, to group works together, but I realized that the most obvious characteristics on which to base this sort of analysis were type of work, characteristics of the author, the time period during which it was published, the type of work it represented -- in other words, data captured in other files or better worked with elsewhere. At this point, then, I am keeping this as a reference only. However, I may find other uses for it later!

The other two sets required more careful analysis to prepare them to be useful.  The subject authors gave me an opportunity to partially answer one of my research questions: How had the canon of American literature changed in the twentieth century? Are scholars writing about different authors now than they did previously? Is more attention being paid to women authors and authors of color? 

To answer that question, I needed to be able to identify authors by gender and race. This is problematic for several reasons! 

First, it requires me to slot people into reductive, simplistic categories, which may or may not match their own sense of their identity.  I've classified Willa Cather as a woman here; I'm not completely certain that this is how she identified, and since I'm not a Cather scholar, I'm aware that there are questions about this, but I'm ill-suited to make a strong argument for any particular gender. This is one problem with projects that cover multiple authors; it's very likely to come across researchers with whom one isn't familiar.  Race is also complex. Because I'm working with a small dataset, I looked up each author in an attempt to find the most appropriate way to identify them. Note that the "Group" category I left out of the analysis might have been helpful here, since it often identified authors in this way (for instance, as "African American woman poets").  However, it was also inconsistently applied. In fact, because the white supremacy ingrained in American culture views whiteness as the unmarked default, it is much easier to find out whether an author is of color than it is to confirm that an author is white, both in MLA and elsewhere. I tried not to make too many assumptions, but it's entirely possible that I'm incorrect in some places. Two of the authors in this sample were also biracial; in this case, they were Native and white, and I counted them as Native because I wanted to see to what extent the journal was publishing criticism on Native American authors. (Is there a better way to do this??)

In addition to the problems of who might fit in which categories for the purpose of this analysis, there are also some problems with using these categories in an apparently straightforward, unquestioning way. Miriam Posner argues convincingly that identity is more complex than crude data models such as those used in the US Census, and that the Census's simplifications don't give us the most accurate picture of the United States. When we don't acknowledge complexity, we run the risk of reinforcing these simplified and "official" categories. *

However, I do need to include information on both gender and race in order to identify underreprensentation.  It's worth thinking about better and more nuanced ways I could have accomplished this.

The final dataset is that of the descriptive subject terms.  There are so many of these, and they cover a lot of different aspects of the text and the criticism. It seemed impractical to analyze the list as a whole, so I coded them, using a list of topics that I generated as I read through them.  (Read about topic coding and put some information about it here.) Many terms duplicated the subject author and subject title information found elsewhere in the record; unless I find that there is some difference between them, I will not consider these in later analysis. However, many of the other terms gave some description of the topics covered in the article.  

Please see the data dictionary for an explanation of each term. Here, I'll simply point out that some referred to the context in which a work was published or the topics that it covered, while others dealt with concepts important in the work under consideration, or the rhetorical strategies employed in those works. 

As a hastily-constructed, ad hoc list of categories, it could easily be improved upon, and I invite you to do so. However, it did help me to describe some of the patterns that I percieve in the subject terms.

I'll note here, too, that many similar projects use vocabularies already developed and tested by other scholars. This is a useful strategy where it exists.

*Posner, Miriam. "What's Next: The Radical, Unrealized Potential of Digital Humanities." Debates in the Digital Humanities: 2016, edited by Lauren F. Klein and Matthew K. Gold, University of Minnesota Press, 2016, p. 54.