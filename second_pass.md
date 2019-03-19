# This Stage

Now that we have our data in a relatively workable format, it's time to see what we can do with it! From this point on, it's worthwhile to think about each of the pieces of our data separately; the things we can do with each are going to be different. 

## American Literature by Century

Our collection of subject dates is the easiest to work with. In the records, each article has metadata indicating the century to which the literature it analyzes belongs -- the subject dates.  These are relatively easy to analyze because:

* They include a relatively small number of values
* The dates are comparable to each other in an obvious, straightfoward fashion.
* It's easy to know what questions we want to ask.

I'm making the data available here as a CSV file, but it's probably easiest to use some sort of spreadsheet software to tabulate the data and create simple visualizations. I used Microsoft Excel for this purpose, but you could do the same with GoogleSheets or a free and open source spreadsheet alternative (true?).  

The software I used has a function allowing me to count the number of occurences for a specific string in a set of cels, so I organized the cels by publication year of the article (1950, 1980, or 2010) and made a table for each subject period and one for the data overall, as below:

Table 1	All data	
Overall coverage of literature by century		
Century	Number of articles	% of articles
1600-1699	3	3%
1700-1799	5	5%
1800-1899	59	61%
1900-1999	27	28%
2000-2099	0	0%
No Period Listed	3	3%
Total	97	100%

(link to other data)

Note that even at this point, I still needed to double-check my data against the dataset.  The number of periods listed did not match the number of records, so I needed to see why that was. I discovered that a few records listed the period twice, so I deleted those entries from my data. Additionally, I found a few records which did not list any subject period.  These were bibliographies of work published in other journals. I can easily imagine a work of criticism that compares works from multiple centuries, but the particular dataset featured here did not include any such works.

I used the visualization tools in my spreadsheet software to create some bar charts illustrating the coverage of literature by century. Now, the data is boiled down to a point where we can begin to make inferences about the focus of this journal! It is very clear that some time periods are more important to the readership of _American Literature_ than others. 

(insert bar charts)

## American Literature by Type of Work

The "work classification" -- dividing works into fiction, poetry, etc is a little more complicated than the dates, but not as complicated as some of the other metadata we'll consider later. Once again, I made a table of the different types of works appearing in the metadata, checking for duplicates as descibed above: 

Type of Work	Cited in 1950	Cited in 1980	Cited in 2010	Total
autobiography	0	0	2	2
criticism	1	1	0	2
fiction	0	0	1	1
manuscript note	2	2	0	4
novel	6	6	4	16
poetic cycle	0	0	1	1
poetry	4	4	3	11
prose	9	9	5	23
short story	1	1	2	4
source study	1	1	0	2
translation	1	1	0	2
Total	25	25	18	68

Looking at this table, a few problems become obvious. First, this is a much larger number of possible categories than the last dataset! There are eleven categories in this list; not a huge number, but also not a number that lends itself to the visualizations of the type we've tried above. Additionally, some of the distinctions made seem a little arbitrary -- for instance, why are some works classified as "novels" or "short stories," while others are classified simply as "prose"?

A quick glance shows us that most of these categories include fewer than five items.  Items in three categories, "novel," "poetry," and "prose," make up most of the list. One way of dealing with this kind of data is to look only at the items that dominate the list, so for instance, I could visualize just these three:

[insert graph]

But this doesn't seem right to me. What if the categories I've discarded actually add up to something important? Are we underestimating the amount of criticism published about prose if we leave out short stories and autobiographies?  

My answer to this problem was to sort each type of work into a larger category. The typical "genres" that literary criticism often uses as starting points are poetry, prose, and drama, so that seemed like a good place to start. However, I also wanted to acknowledge the difference between novels and manuscript notes, works of criticism, and the like. Therefore, I introduced into my categories a distinction between creative prose works, like novels and short stories, and critical prose works, such as criticism. 

work_classification_grouped.csv

I was not sure that my new groupings would reveal anything about the data, but they did! The new table looked like this:

Type of Work	Cited 1950	Cited 1980	Cited 2010	Total
Creative Prose Works	16	16	14	46
Critical Prose Works	5	5	0	10
Works of Poetry	4	4	4	12
Total	25	25	18	68

At first, I was suspicious of these results! The numbers were so consistent that I feared I had made an error in counting them up. However, checking my work confirmed that these numbers are accurate.  In fact, their consistency is so great that it suggests we have discovered one of the editorial policies of _American Literature_. 

This also makes it much easier to notice the absence of any articles focusing on drama!  

## American Literature by Authors

In this section, I'm looking at the authors who are the subject of the articles in _American Literature_, not the authors who wrote the articles. 

This is a _much_ longer list! To figure out exactly how much, I made a table that consolidated my list of authors by year cited. Sixty-two different subject authors were included in the metadata for these three years; only 11 were mentioned more than once.  The only two mentioned more than three times were Nathaniel Hawthorne (4 times) and Herman Melville (12 times). 

subject_authors_by_year.csv

This isn't very useful, because we don't have a large enough sample to draw conclusions about the extent to which _American Literature_ features certain authors in their articles. Melville is clearly important, but the much larger group of authors analyzed in at least one article includes authors like Emily Dickinson and Robert Frost along with much more obscure authors like Bret Harte and primarily non-literary authors like Thomas Jefferson. With a broader look at the work published in _American Literature_, we would likely see much more work on Dickinson than on Harte. There are so many authors in play that it isn't especially surprising for any one author, even an important one to be only cited once in a year, or not cited at all.  

So, what kinds of questions can we ask about data like this?  If we can't identify the authors most important to this journal's readership, what might we be able to find about the focus of this journal? 

I tried an approach similar to the one I used for type of work -- I put the authors into groups, specifically by race and gender.  I put all the author names in a spreadsheet, along with the year in which that author was referenced, and I did my best to find out the race and gender for each of them. This approach is problematic [insert analysis from prior document]  

The advantage of this approach, however, is that we can use it to begin to think about the extent to which _American Literature_ has a dead white men problem [rephrase but I don't want to get distracted by it right now].  

subject_authors_coded.csv

From here, I made some tables breaking down the numbers of articles about works by the gender and race of the author.  This analysis does _not_ take into account that some authors are the subject of multiple articles!  Thus, it does not evaluate (for instance) the number of women whose work was analyzed -- only the number of articles about literature by women.  Collapsing the works about the same author would produce different (though likely also interesting) results.

subject_authors_race_gender_table.csv

## American Literature by Works

When I began, I thought this would be an important category of metadata. However, we run into the same problems we do with many of the other categories: this is a list of sixty-nine items, with sixty-six different entries! For the curious, the works analyzed more than once are: Mark Twain's _Roughing It_ (mentioned in 1950 and 1980), _The Confidence Man_(mentioned in 1950 and 1980), and _The Grandissimes_(mentioned in 1980 and 2010).

If we were to break the works into groups, we might get interesting results -- but much of this work is already done in the rest of the metadata! We already have data about types of work, centuries published, and the authors. 

Thus, while I made a list of works, I've done no other analysis on this material.

subject_works_list_compiled.csv

## American Literature by Subject

The above data tells us a lot about the publication practices of _American Literature_, but now we are coming to the subject terms describing the articles, which are assigned by MLA field indexers.  The subjects tell us a lot about the journal and its content, but also about the bibliography and which aspects of an article are considered notable.

subject_terms_list_compiled.csv

The first thing we can do with this list is calculate the number of terms assigned in each year.  In 1950, a total of 44 subject terms were assigned to articles in _American Literature_. In 1980, that number rose to 95, and in 2010, 112. However, fewer articles were published in 2010 than in those other years!  Pulling from the data provided above, I as able to calculate the average number of terms per article:

	1950	1980	2010
Number of Subject Terms	44	95	112
Number of Articles Published	37	35	24
Subject Terms per Article	1.189189189	2.714285714	4.666666667

This is worth  keeping in mind during our analysis!  Since articles published in 2010 have nearly four times as many subject terms on average as those published in 1950, it won't necessarily be meaningful to show that a particular term or set of terms were used more often in 2010.  

However, aside from the sheer number of terms, this list of subject terms doesn't offer any obvious, immediate path to analytical conclusions -- much like many of the other datasets we've looked at here. I made a decision to code the subject terms, breaking them into groups for analysis. Under ideal circumstances, I could cross-check these with another person, but the constraints of the current project prevented that approach.

Note that this is very different from the kinds of coding we've done on previous iterations of this data, because here, I am making up my own categories. Thus, my analysis will depend very heavily on what kinds of categories I assign and how I understand those categories.  Note that it isn't always necessary to make up your own terms. Often, vocabularies have already been developed and documented by other researchers; other times, it may be possible to access the categories into which the terms were originally understood.*

Nobody should trust my analysis without taking a good look at the categories I developed!  This is where a data dictionary comes in handy. It helps the future users of my data to understand the decisions I made, and, as an added benefit, writing it helped me to develop my thinking further, and eliminate the categories I couldn't explain well. 

subject_terms_data_dictionary.txt
subject_terms_coded.csv

Of course, these categories are deeply rooted in my own point of view; there is no reason to think someone else looking at this data would come up with the same analysis. However, it's worth noticing that some of them, like those I've labeled "philosophical concepts" or "rhetorical techniques" are about the aspects of the work being analyzed, while others are about the author, or relationships _among_ works, or even the article itself. 

Visualizing any set of data with this many categories is likely to be difficult. In this case, a year-by-year graph can give us some indication of where it would be most useful to look, because it allows us a quick glance into how the number of headings of each type has changed relative to the others of its year. 

[chart from subject_terms_analysis.xml]

*Subject terms, in many cases, are part of a hierarchical vocabulary with their own implied context. However, these are not always visible or legible to the enduser, in this case me.