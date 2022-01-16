Create table video  (
  idvideo int NOT NULL,
  video_url varchar(50) NOT NULL,
  video_duration int NOT NULL,
  publish_date date NOT NULL,
  PRIMARY KEY (idvideo)
);


create table category(
     idcategory int NOT NULL,
     category_name varchar(30) NOT NULL,
     PRIMARY KEY (idcategory)
     
);

     
CREATE TABLE subcategory (
      idsubcat int NOT NULL,
      subcategory_name varchar(14) NOT NULL,
      idcategory int NOT NULL,
      PRIMARY KEY (idsubcat),
      CONSTRAINT FK_category FOREIGN KEY (idcategory)
    REFERENCES category(idcategory)
      
);


CREATE TABLE vidcat (
     idvideo int NOT NULL,
     idsubcat int NOT NULL,
    CONSTRAINT FK_video FOREIGN KEY (idvideo)
    REFERENCES video(idvideo),
    CONSTRAINT FK_subcat FOREIGN KEY (idsubcat)
    REFERENCES subcategory(idsubcat)
    );