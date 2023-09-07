create table mysql.subscribers
(
    subscriber_id bigint unsigned auto_increment       primary key,
    first_name    text                                 not null,
    email         text                                 not null,
    created_on    datetime   default CURRENT_TIMESTAMP not null,
    is_active     tinyint(1) default 1                 not null,
    modified_on   datetime                             null,
    constraint subscriber_id
        unique (subscriber_id)
);

