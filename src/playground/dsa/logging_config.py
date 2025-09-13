import logging


class OptionalExtraFormatter(logging.Formatter):
    def format(self, record):
        # Check for 'my_extra_field' and provide a default if not present
        record.my_extra_field = getattr(record, "my_extra_field", "N/A")
        # Check for 'another_extra_field' and provide a default if not present
        record.another_extra_field = getattr(
            record, "another_extra_field", "DEFAULT_VALUE"
        )
        return super().format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


handler = logging.StreamHandler()
formatter = OptionalExtraFormatter(
    "%(asctime)s - %(levelname)s - %(message)s - my_extra_field: %(my_extra_field)s - another_extra_field: %(another_extra_field)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


__all__ = ["logger"]
