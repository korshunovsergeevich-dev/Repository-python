import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql://postgres:123441Korshun@localhost:5432/postgres"
)


engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)


@pytest.fixture
def db_session():

    session = Session()

    yield session

    session.close()


@pytest.fixture
def test_create_student(db_session):

    student_data = {
        "user_id": 888888,
        "level": "beginner",
        "education_form": "online",
        "subject_id": 888888
    }

    # Удаляем данные от предыдущего запуска
    db_session.execute(
        text("""
            DELETE FROM student
            WHERE user_id = :user_id
        """),
        {
            "user_id": student_data["user_id"]
        }
    )
    db_session.commit()

    try:
        # Создаём студента
        db_session.execute(
            text("""
                INSERT INTO student
                (user_id, level, education_form, subject_id)
                VALUES
                (:user_id, :level, :education_form, :subject_id)
            """),
            student_data
        )
        db_session.commit()

        # Получаем созданного студента
        student = db_session.execute(
            text("""
                SELECT
                    user_id,
                    level,
                    education_form,
                    subject_id
                FROM student
                WHERE user_id = :user_id
            """),
            {
                "user_id": student_data["user_id"]
            }
        ).mappings().first()

        # Проверки
        assert student is not None
        assert student["user_id"] == 888888
        assert student["level"] == "beginner"
        assert student["education_form"] == "online"
        assert student["subject_id"] == 888888

    finally:
        # Удаляем тестовые данные
        db_session.execute(
            text("""
                DELETE FROM student
                WHERE user_id = :user_id
            """),
            {
                "user_id": student_data["user_id"]
            }
        )
        db_session.commit()


def test_update_student(db_session, created_student):

    user_id = created_student

    # Изменяем данные студента
    db_session.execute(
        text("""
            UPDATE student
            SET
                level = :level,
                education_form = :education_form
            WHERE user_id = :user_id
        """),
        {
            "level": "advanced",
            "education_form": "offline",
            "user_id": user_id
        }
    )
    db_session.commit()

    # Получаем обновлённого студента
    student = db_session.execute(
        text("""
            SELECT
                level,
                education_form
            FROM student
            WHERE user_id = :user_id
        """),
        {
            "user_id": user_id
        }
    ).mappings().first()

    # Проверяем изменения
    assert student is not None
    assert student["level"] == "advanced"
    assert student["education_form"] == "offline"


def test_delete_student(db_session, created_student):

    user_id = created_student

    # Удаляем студента
    db_session.execute(
        text("""
            DELETE FROM student
            WHERE user_id = :user_id
        """),
        {
            "user_id": user_id
        }
    )
    db_session.commit()

    # Проверяем удаление
    student = db_session.execute(
        text("""
            SELECT user_id
            FROM student
            WHERE user_id = :user_id
        """),
        {
            "user_id": user_id
        }
    ).first()

    assert student is None
