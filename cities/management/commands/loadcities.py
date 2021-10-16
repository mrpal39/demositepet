from django.core.management import BaseCommand

from cities import utils


class Command(BaseCommand):
    """
    Load cities and states in the correct models, only available for Brazil at the moment
    """

    def handle(self, *args, **options):
        country = "India"
        utils.load_states_from_file(utils.get_states_filename(country))
        # utils.load_cities_from_file(utils.get_cities_filename(country))
        # utils.load_post_cities_from_file(utils.get_postcode_cities_filename(country))
