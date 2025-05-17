import datetime
from app.errors import (
    NotVaccinatedError,
    NotWearingMaskError,
    OutdatedVaccineError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor.get("name", "Visitor")} is not vaccinated"
            )

        vaccine_info = visitor["vaccine"]
        if "expiration_date" in vaccine_info:
            if vaccine_info["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError(
                    f"{visitor.get("name", "Visitor")}'s vaccine is outdated"
                )

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor.get("name", "Visitor")} is not wearing a mask"
            )

        return f"Welcome to {self.name}"
