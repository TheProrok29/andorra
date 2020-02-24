from dataclasses import dataclass

from characters.models import Character


@dataclass
class JourneyEvent:
    duration: int
    description: str


class JourneyDefinition():
    slug: str
    name: str

    def proceed(self, character: Character) -> JourneyEvent:
        raise NotImplementedError()


class FirstJourney(JourneyDefinition):
    slug = 'first_journey'
    name = 'Enter the realm'

    def proceed(self, character: Character) -> JourneyEvent:
        yield JourneyEvent(5, 'first')
        yield JourneyEvent(10, 'fight')
        yield JourneyEvent(5, 'second')


class SecondJourney(JourneyDefinition):
    slug = 'second_journey'
    name = 'Enter the dark forest'

    def proceed(self, character: Character) -> JourneyEvent:
        yield JourneyEvent(5, 'first')
        yield JourneyEvent(10, 'fight')
        yield JourneyEvent(5, 'second')


journey_list = [
    FirstJourney(),
    SecondJourney(),
]
