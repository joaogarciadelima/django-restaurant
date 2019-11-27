import pytest
from restaurant.food.models import Restaurant


@pytest.fixture
def restaurantes(db):
    restaurantes = Restaurant(name='Copacabana',
                              address='Avenida Getúlio Vargas, 830',
                              photo=None,
                              menu='Pizza',
                              tags='Pizza'
                              )

    restaurantes.save()
    return [restaurantes]
