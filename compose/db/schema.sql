\c fast_posts

CREATE TABLE user_accounts (
    id SERIAL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(60) NOT NULL,
    password VARCHAR(60) NOT NULL,

    CONSTRAINT user_account_pk PRIMARY KEY (id)
);


CREATE TABLE posts (
    id SERIAL,
    title VARCHAR(200) NULL,
    content TEXT NOT NULL,
    author_pk INT NOT NULL,

    CONSTRAINT post_pk PRIMARY KEY (id),
    CONSTRAINT author_fk FOREIGN KEY (author_pk) REFERENCES user_accounts
                  ON DELETE CASCADE ON UPDATE CASCADE
);