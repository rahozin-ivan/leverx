tables = {
    'rooms':
        """
        create table if not exists rooms(
        id int primary key,
        name varchar(30))
        """,
    'students':
        """
        create table if not exists students(
        birthday DATE,
        id int primary key,
        name varchar(30),
        room int,
        sex CHARACTER,
        FOREIGN KEY (room) REFERENCES rooms(id),
        CHECK(sex in ('M', 'F')))
        """}

queries = {
    'number_of_students_in_the_room':
        """
        select rooms.name, count(*) as number_of_students
        from rooms join students on rooms.id = students.room
        group by rooms.id
        """,
    'top_rooms_with_smallest_average_age':
        """
        select rooms.name, avg(datediff(now(), students.birthday)) as average_age
        from rooms join students on rooms.id = students.room
        group by rooms.id order by average_age limit 5
        """,
    'top_rooms_with_biggest_age_difference':
        """
        select rooms.name, max(students.birthday) - min(students.birthday) as age_difference
        from rooms join students on rooms.id = students.room
        group by rooms.id order by age_difference desc limit 5
        """,
    'rooms_with_different_sex_students':
        """
        select rooms.name
        from rooms join students on rooms.id = students.room
        group by rooms.id having count(distinct students.sex) = 2
        """
}
