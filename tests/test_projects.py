import uuid


class TestCreateProject:

    def test_create_project_positive(self, project_api):

        title = f"Autotest project {uuid.uuid4()}"

        response = project_api.create_project(title)

        assert response.status_code == 201

        body = response.json()

        assert "id" in body
        assert body["id"]

    def test_create_project_negative_empty_title(self, project_api):

        response = project_api.create_project("")

        assert response.status_code in (400, 422)


class TestUpdateProject:

    def test_update_project_positive(self, project_api):

        create_title = f"Autotest project {uuid.uuid4()}"
        update_title = f"Updated project {uuid.uuid4()}"

        create_response = project_api.create_project(create_title)

        assert create_response.status_code == 201

        project_id = create_response.json()["id"]

        update_response = project_api.update_project(
            project_id,
            update_title
        )

        assert update_response.status_code == 200

        body = update_response.json()

        assert body["id"] == project_id

    def test_update_project_negative_invalid_id(self, project_api):

        invalid_project_id = str(uuid.uuid4())

        response = project_api.update_project(
            invalid_project_id,
            "Updated project"
        )

        assert response.status_code in (400, 404)


class TestGetProject:

    def test_get_project_positive(self, project_api):

        title = f"Autotest project {uuid.uuid4()}"

        create_response = project_api.create_project(title)

        assert create_response.status_code == 201

        project_id = create_response.json()["id"]

        response = project_api.get_project(project_id)

        assert response.status_code == 200

        body = response.json()

        assert body["id"] == project_id
        assert body["title"] == title

    def test_get_project_negative_invalid_id(self, project_api):

        invalid_project_id = str(uuid.uuid4())

        response = project_api.get_project(invalid_project_id)

        assert response.status_code in (400, 404)
