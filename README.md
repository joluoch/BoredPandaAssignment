# BoredPandaAssignment
# Technical question : 
  Design a DB structure to store video data. We need video titles, category names, and subcategory names. 
  Write a query for this structure to fetch last month's most popular subcategories in which it would show the name of the subcategory and how many times it appeared.
# Simple Schema :
  ![alt text](https://github.com/joluoch/BoredPandaAssignment/blob/master/OutputImages/schema.png?raw=true)
  
  The Schema has 4 tables, 
  ## video tables:
    The table contains the video id , video url, video duration and published date. 
    This table has a relationship with table video-subcategory 
  ## Category tables:
    The table has the category id and name of the category.
    It has a one to many relationship between category and subcategory table 
  ## Subcategory table:
    The table contains the subcategory id , subcategory name and the category id it belongs to.
  ## Video_Subcategory table:
    This table contains the id's of video and subcategory as foreign keys. 
    Logic: one video can have many subcategories and one subcategory can have many videos. thus if you want 
            to query the category table you will have to go through the subcategory table
# Scripts:
  MakeDb.py - cnotains queries to make the database and insert data into it \n
  PopularSubcategory.py - contains scripts to show the popular sub category of between given date.
# Outputs :
  We have queried the database to show most popular subcategory in the month of january below are the outputs.
  # Non - Graphical 
  ![alt text](https://github.com/joluoch/BoredPandaAssignment/blob/master/OutputImages/nongraphical.png?raw=true)
  # Graphical 
