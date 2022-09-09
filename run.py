from db.session import session_scope
from db.tables.genres import Genres
from db.tables.persons import Persons

if __name__ == '__main__':
    with session_scope() as db_session:

        # Вставка в таблицу
        new_person = Persons(
            id=1,
            name='Maksim',
            surname='Sazanovich',
            birth_date='1989-03-01'
        )
        db_session.add(new_person)
        db_session.commit()

        new_person_2 = Persons(
            id=2,
            name='Delete',
            surname='Deletovich',
            birth_date='2000-01-01'
        )
        db_session.add(new_person_2)
        db_session.commit()

        # Редактирование элемента
        change = db_session.query(Persons).filter(Persons.id == 1)
        change.update({Persons.surname: 'MAKSIM'})
        change.update({Persons.surname: 'SAZANOVICH'})
        db_session.commit()

        # Удаление элемента
        del_person = db_session.query(Persons).filter(Persons.id == 2).first()
        db_session.delete(del_person)
        db_session.commit()

        # Выборка с условием
        genres = db_session.query(Genres).all()
        for element in genres:
            print(element.name)
