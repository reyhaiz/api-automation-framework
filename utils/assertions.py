import jsonschema

class Assertions:

    @staticmethod
    def assert_status_code(response, expected):
        actual = response.status_code
        assert actual == expected, (
            f"\n❌ Status Code salah!"
            f"\n   Expected : {expected}"
            f"\n   Actual   : {actual}"
            f"\n   URL      : {response.url}"
        )

    @staticmethod
    def assert_response_time(response, max_ms=2000):
        elapsed = response.elapsed.total_seconds() * 1000
        assert elapsed <= max_ms, (
            f"\n❌ Response terlalu lambat!"
            f"\n   Max      : {max_ms}ms"
            f"\n   Actual   : {elapsed:.0f}ms"
        )

    @staticmethod
    def assert_content_type(response, expected="application/json"):
        ct = response.headers.get("Content-Type", "")
        assert expected in ct, (
            f"\n❌ Content-Type salah!"
            f"\n   Expected : {expected}"
            f"\n   Actual   : {ct}"
        )

    @staticmethod
    def assert_json_schema(data, schema):
        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.ValidationError as e:
            raise AssertionError(f"\n❌ Schema tidak valid: {e.message}")

    @staticmethod
    def assert_field_exists(data, field):
        assert field in data, f"\n❌ Field '{field}' tidak ada di response"

    @staticmethod
    def assert_field_value(data, field, expected):
        Assertions.assert_field_exists(data, field)
        assert data[field] == expected, (
            f"\n❌ Nilai field '{field}' salah!"
            f"\n   Expected : {expected}"
            f"\n   Actual   : {data[field]}"
        )

    @staticmethod
    def assert_list_not_empty(data):
        assert isinstance(data, list) and len(data) > 0, \
            "\n❌ Response list kosong atau bukan list!"

    @staticmethod
    def assert_list_length(data, expected_length):
        assert len(data) == expected_length, (
            f"\n❌ Panjang list salah!"
            f"\n   Expected : {expected_length}"
            f"\n   Actual   : {len(data)}"
        )