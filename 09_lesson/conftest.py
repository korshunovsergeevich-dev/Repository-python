import pytest
from sqlalchemy import text


@pytest.fixture
def created_student(db_session):
    user_id = 888888

    # Удаляем студента, если он уже существует
    db_session.execute(
        text("""
            DELETE FROM student
            WHERE user_id = :user_id
        """),
        {"user_id": user_id}
    )
    db_session.commit()

    # Создаём студента
    db_session.execute(
        text("""
            INSERT INTO student
            (user_id, level, education_form, subject_id)
            VALUES
            (:user_id, :level, :education_form, :subject_id)
        """),
        {
            "user_id": user_id,
            "level": "beginner",
            "education_form": "online",
            "subject_id": 888888
        }
    )
    db_session.commit()

    yield user_id

    # Удаляем студента после теста
    db_session.execute(
        text("""
            DELETE FROM student
            WHERE user_id = :user_id
        """),
        {"user_id": user_id}
    )
    db_session.commit()
