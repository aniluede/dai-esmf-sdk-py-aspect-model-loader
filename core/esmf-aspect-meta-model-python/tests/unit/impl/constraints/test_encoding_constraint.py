"""DefaultEncodingConstraint class unit tests suit."""

from unittest import mock

from esmf_aspect_meta_model_python.impl import DefaultEncodingConstraint


class TestDefaultEncodingConstraint:
    """DefaultEncodingConstraint unit tests class."""

    meta_model_mock = mock.MagicMock(name="meta_model_base_attributes")

    @mock.patch("esmf_aspect_meta_model_python.impl.constraints.default_encoding_constraint.DefaultConstraint.__init__")
    def test_init(self, super_mock):
        result = DefaultEncodingConstraint(self.meta_model_mock, "value")

        super_mock.assert_called_once_with(self.meta_model_mock)
        assert result._value == "value"

    @mock.patch("esmf_aspect_meta_model_python.impl.constraints.default_encoding_constraint.DefaultConstraint.__init__")
    def test_value(self, _):
        encoding_constraint = DefaultEncodingConstraint(self.meta_model_mock, "value")
        result = encoding_constraint.value

        assert result == "value"
